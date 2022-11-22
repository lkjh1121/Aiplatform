#공부시간으로 시험점수를 예측해보자 
x = [[20], [19], [17], [18], [12], [14], [10], [9], [16], [6]] #2차원이어야한다
y = [ 100,100,90, 90, 60, 70, 40, 40,70,30] #1차원이어야 한다 

import numpy as np 
xx = np.array(x)
yy = np.array(y)

from sklearn.model_selection import train_test_split
#import sklearn
#sklearn.model_selection.train_test_split
#from 절을 사용해서 모듈을 import하는게 사용이 훨씬 편하다 
X_train, X_test, y_train, y_test = train_test_split(xx, yy, 
test_size=0.2, random_state=1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("기울기 : ", model.coef_)
print("절편 ", model.intercept_)

y = model.coef_*X_test + model.intercept_
print("원래값", y_test )
print("예측값1", y  )
print("예측값2", y_pred )

print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))
