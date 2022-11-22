#공부시간으로 시험점수를 예측해보자 
x = [[20], [19], [17], [18], [12], [14], [10], [9], [16], [6]] #2차원이어야한다
y = [ 1, 1, 1, 1, 0, 1, 0, 0,1,0] #1차원이어야 한다
#분류분석이 될때는 확률 1 또는 0 - 이진분류  

import numpy as np 
xx = np.array(x)
yy = np.array(y)

from sklearn.model_selection import train_test_split
#import sklearn
#sklearn.model_selection.train_test_split
#from 절을 사용해서 모듈을 import하는게 사용이 훨씬 편하다 
X_train, X_test, y_train, y_test = train_test_split(xx, yy, 
test_size=0.2, random_state=1)

#분류알고리즘이지만 Regression이 있다
from sklearn.linear_model import LogisticRegression
model = LogisticRegression() 
#파이썬의 로지스틱 회귀분석 2진분류,다중분류도 된다. 단 R언어는 이진분류
#만 가능하다. R과 파이썬은 다르다 

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print( y_pred )

print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))
