from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, precision_score, roc_auc_score 
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.metrics import precision_recall_curve, roc_curve

from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sympy import solve 

#1.데이터 확인하기
diabetes = pd.read_csv("./data/diabetes.csv")
print( diabetes.head() )

#데이터 부분과 타겟으로 쪼개자 
data = diabetes.iloc[:, :-1] #-1 : 
target = diabetes.iloc[:, -1] 

print( data.head(3) )
print( target.head(3))

#데이터를 훈련셋과 테스트셋으로 나눈다
X_train, X_test, y_train, y_test = train_test_split( 
    data, target, test_size=0.2, random_state=156, 
    stratify=target 
    #균등정도, 실제 데이터의  0과 1의 배분율에 맞춰서 데이터를 쪼개도록
) 

#모델만들기 
model = LogisticRegression(solver='liblinear')
#학습하기
model.fit( X_train, y_train)
#예측하기
y_pred = model.predict(X_test)
y_preda = model.predict_proba(X_test)
y_preda = y_preda[:, 1]

def get_clf_eval( y_test, y_pred=None, y_pred_proba=None):
    confusion = confusion_matrix(y_test, y_pred)#교차행렬
    accuracy = accuracy_score(y_test, y_pred) #정확도
    precision = precision_score(y_test, y_pred) #정밀도 
    recall = recall_score(y_test, y_pred) #재현율 
    f1 = f1_score(y_test, y_pred) # f1 스코어 
    roc_auc = roc_auc_score(y_test, y_pred_proba)

    print("오차행렬")
    print(confusion)

    print("정확도 : {:.4f}  정밀도 : {:.4} 재현율 :{:.4} \
          F1:{:.4} AUC:{:.4}".format(accuracy, precision, 
          recall, f1, roc_auc))


get_clf_eval(y_test, y_pred, y_preda)

#01090837981  백현숙





