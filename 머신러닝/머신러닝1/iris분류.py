#데이터를 사이킷런에서 가져온다 

from sklearn.datasets import load_iris 
#사이킷런에서 제공하는 데이터셋 

data = load_iris() 
print( data.keys() )

print( data["data"][:10] )
#입력데이터 : 2차원 배열 , numpy 
#출력데이터 : 1차원 배열 , numpy 

print( data["target"][:10])
print( data["feature_names"]) #특성의 이름 
print( data["target_names"]) #결과의 이름  

#1.데이터를 적당한 비율로 나눈다. 7:3, 8:2, 6:4 정도로 나누어서 
#  훈련셋과 테스트셋으로 나누자 
#  훈련셋을 이용해 학습모델을 만들고 테스트셋을 통해서 학습모델을 테스트한다

print( data["target"])

#데이터를 랜덤으로 섞어서 분리해주는 함수가 있다 
from sklearn.model_selection import train_test_split
#train_test_split  y= aX+b
X_train, X_test , y_train, y_test = train_test_split(data["data"], 
      data["target"], test_size=0.3, random_state=1)
#test_size:테스트셋을 자르는 비율,  8:2
#random_state: 섞을때 랜덤으로 섞는다. 냅두면 할때마다 다른 데이터셋이 
#              나와서 결과가 미묘하게 바뀐다. 같은 데이터셋이 나오길 
#              원할때 정수값을 준다 1~65535 중에 값 하나를 주면 된다. 

print( X_train.shape )  #2차원 - ndarray
print( X_test.shape )   #2차원 - ndarray
print( y_train.shape)   #1차원 - ndarray
print( y_test.shape)    #1차원 - ndarray

print( y_train[:20])

#의사결정트리 - 스무고개찾기, 날르냐 안날르냐? 트리형태로 데이터를 쪼개간다
#이 알고리즘의 단점은 백프로 과대적합(과도하게 학습되어서 모델이 훈련셋에만
#맞춰져서, 테스트셋이나 다른 데이터셋 넣으면 예측력이 떨어진다.)
#예측보다는 특성중에 중요한 특성과 중요하지 않은 특성이 있다 . 
#중요한 특성을 알아내고자 할때 주로 사용한다. 
#-> 업그레이드 : 랜덤포레스트, 그라디언트부스팅(굉장히 뛰어남)
#그라디언트부스팅 - xgboot 라이브러리, 사이킷런에서 만든 그라디언트부스팅
#보다 뛰어나다  

#Regressor - 회귀분석(집값), Classifier(종류분륜)- 분류분석
from sklearn.tree import DecisionTreeClassifier

#객체 만들고 
dc = DecisionTreeClassifier(random_state=1)
dc.fit(X_train, y_train) #학습셋으로 학습을 한다 
#학습해서 결과를 리턴하지 않고 내부에 모델을 갖고 있다 

#결과 예측하기 
y_pred = dc.predict(X_test) #테스트 셋으로 결과를 예측한다 
for k in zip(y_test, y_pred):
    print(k)

from sklearn.metrics import accuracy_score

#훈련셋과 테스트셋간에 예측비율이 일치해야 한다 
print("훈련셋 정확도 {}".format(dc.score(X_train, y_train)))
print("테스트셋 정확도 {}".format(dc.score(X_test, y_test)))

print("데이터 정확도 {}".format(accuracy_score(y_test, y_pred)))


#의사결정트리에는 결과값안에 특성의 중요도 
#의사결정트리류 알고리즘에만 있다 
print("특성중요도 : ", dc.feature_importances_)

import matplotlib.pyplot as plt 
import numpy as np 
#수평차트 
def treeChart(model, feature_name):
    n_features = len(model.feature_importances_)#특성의 개수 
    #수평 막대 그래프 그리기 
    # x(0,1,2,3,4,5,..), y축:특성의 중요도
    plt.barh( np.arange(n_features), 
              model.feature_importances_, 
              align="center") #중앙정렬 
    plt.yticks(np.arange(n_features), feature_name) #축의 눈금 설정
    plt.ylim(-1, n_features) 
    plt.show() 

treeChart(dc, np.array(data['feature_names']))       






















