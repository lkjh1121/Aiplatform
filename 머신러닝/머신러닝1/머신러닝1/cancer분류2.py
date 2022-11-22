#데이터를 사이킷런에서 가져온다 

from sklearn.datasets import load_breast_cancer 
#사이킷런에서 제공하는 데이터셋 

data = load_breast_cancer() 
print( data.keys() )

print( data["filename"])
print( data["data"][:10] )
#입력데이터 : 2차원 배열 , numpy 
#출력데이터 : 1차원 배열 , numpy 

print( data["target"][:10])
print( data["feature_names"]) #특성의 이름 
print( data["target_names"]) #결과의 이름  0.이 악성, 1.양성 

#1.데이터를 적당한 비율로 나눈다. 7:3, 8:2, 6:4 정도로 나누어서 
#  훈련셋과 테스트셋으로 나누자 
#  훈련셋을 이용해 학습모델을 만들고 테스트셋을 통해서 학습모델을 테스트한다

print( data["target"])

#데이터를 랜덤으로 섞어서 분리해주는 함수가 있다 
from sklearn.model_selection import train_test_split
#train_test_split  y= aX+b
X_train, X_test , y_train, y_test = train_test_split(data["data"], 
      data["target"], test_size=0.3, random_state=1)
#test_size:테스트셋을 자르는 비율,  8:2, 7:3, 6:4
#random_state: 섞을때 랜덤으로 섞는다. 냅두면 할때마다 다른 데이터셋이 
#              나와서 결과가 미묘하게 바뀐다. 같은 데이터셋이 나오길 
#              원할때 정수값을 준다 1~65535 중에 값 하나를 주면 된다. 

print( X_train.shape )  #2차원 - ndarray
print( X_test.shape )   #2차원 - ndarray
print( y_train.shape)   #1차원 - ndarray
print( y_test.shape)    #1차원 - ndarray

print( y_train[:20])

from sklearn.neighbors import KNeighborsClassifier
train_score=[]
test_score=[]
for i in range(1, 11): #이웃숫자를 1,10까지 바꿔가면서 테스트셋과 
    #훈련셋의 학습성취도를 모아보자 
    model = KNeighborsClassifier(n_neighbors=i) 
    model.fit(X_train, y_train)
    #예측안해도 훈련성과는 가져올 수 있다 
    train_score.append( model.score(X_train, y_train))
    test_score.append( model.score(X_test, y_test))
     
for i in range(0, 10):
    print(i,  train_score[i], test_score[i], 
            train_score[i]-test_score[i])


#conda activate 
#pip install tensorflow 




