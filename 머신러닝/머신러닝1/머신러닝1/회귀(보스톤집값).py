from sklearn.datasets import load_boston
boston = load_boston()
print( type(boston))
print( boston.keys() )

input_data = boston["data"]
output_data = boston["target"]
print( input_data.shape)
print( output_data.shape)

#피처 - 13개 
print( input_data[:10])
print( output_data[:10])

#1. 데이터를 훈련셋과 테스트셋으로 나눈다
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(
    input_data, output_data, train_size=0.7, 
    random_state=1234
)

print( X_train.shape )
print( X_test.shape )

#선형회귀모델을 만든다
from sklearn.linear_model import LinearRegression
model = LinearRegression() #하이퍼 파라미터 없음 
#학습효과를 높이거나, 과대적합을 해결할 방법도 없다 

#학습을 한다 - 훈련데이터 셋으로 학습을 한다 
model.fit( X_train, y_train ) 

#테스트셋을 주어서 예측을 해본다 
y_pred = model.predict( X_test )

#기울기와 절편이 존재한다. - 이 모델은 내부적으로 기울기와 절편을 구한다 
print("기울기 : ", model.coef_)
#각 특성별로 가중치가 얻어진다. 가중치 = 기울기 
print("절편 : ",  model.intercept_)

# y_pred2 = model.coef_*(X_test) + model.intercept_
# print(y_pred[:10])
# print(y_pred2[:10])


print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))


