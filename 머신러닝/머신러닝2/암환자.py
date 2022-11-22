#이진분류 악성이냐 아니냐 
from asyncio import threads
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

cancer = load_breast_cancer()
cancer_data = cancer['data']
cancer_target= cancer['target']
X_train, X_test, y_train, y_test = train_test_split(cancer_data, 
cancer_target, test_size=0.3, random_state=11)

model = LogisticRegression()
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)

#혼동행렬 
from sklearn.metrics import confusion_matrix
print( confusion_matrix(y_test, y_pred) )

from sklearn.metrics import accuracy_score, precision_score, recall_score

print("정확도 ", accuracy_score(y_test, y_pred))
print("정밀도",  precision_score(y_test, y_pred))
print("재현율 ", recall_score(y_test, y_pred))
print(y_pred) #예측값 0 또는 1을 출력 - 예측 결과

#확률을 가져온다 
y_preda = model.predict_proba(X_test)
import numpy as np 
print( np.round(y_preda,2)  )

print(cancer["target_names"])#0-암환자, 1-양성 
#앞의 부분의 확률이 0.5보다 크면 암환자이다. 
#앞의 확률이 암환자일 확률, 뒤에 있는게 암환자가 아닐확률 
#softmax 함수 - 연산결과를 다 더하여 1이 되도록 확률로 바꿔주는 함수 


#정밀도/재현율의 trade off 

from sklearn.preprocessing import Binarizer, binarize
#y_preda 를 2차원으로 바꾸자
#1.컬럼을 
y_preda1 = y_preda[:, 0]
y_preda1 = y_preda1.reshape(-1, 1)
#print( np.round(y_preda1, 2)) #암환자일 확률을 별도로 빼냄 

binarizer = Binarizer(threshold=0.5)
y_preda2 = binarizer.fit_transform(y_preda1)
#print( y_preda2) #0.4보다 크거나 같으면 1로 0.4보다 작으면 0으로 본다 

print("정확도 ", accuracy_score(y_test, y_preda2))
print("정밀도",  precision_score(y_test, y_preda2))
print("재현율 ", recall_score(y_test, y_preda2))

#ROC 커브그리기 - 성능 측정, 최대한 면적을 채울수록 성능이 좋은 모델이다
#성능을 시각적으로 보여줄 수 있다 

from sklearn.metrics import roc_curve
y_pred = model.predict_proba(X_test) #예측값 얻기 
#확률을 얻으면 2차원 배열 , 
y_pred = y_pred[:, 1]  #1번 열의 데이터를 가져간다 

fprs, tprs, thresholds = roc_curve(y_test, y_pred) 
print(thresholds )

#차트그리기
import matplotlib.pyplot as plt 
def roc_curve_plot(y_test, y_pred):
    fprs, tprs, thresholds = roc_curve(y_test, y_pred) 
    plt.plot(fprs, tprs, label="ROC")
    plt.plot([0,1], [0,1], 'k--', label='Random')
    plt.show()

roc_curve_plot(y_test, y_pred)













