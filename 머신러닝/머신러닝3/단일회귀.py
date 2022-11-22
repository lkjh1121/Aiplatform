
#키가크면 몸무게가 증가하는가 
#X가 독립변수 
X = [178, 153, 190, 178, 190, 192, 170, 171, 174, 178]
#y가 종속변수, 몸무게
y = [65, 48, 98, 85, 85, 100, 67, 64, 58, 65]
import numpy as np 
import pandas as pd 

X = np.array(X)
y = np.array(y)

print( X.shape )
print( y.shape )

#상관계수구하기 
df = pd.DataFrame({"X":X, "Y":y})

print(df)
print( df.corr(method='pearson') )

#산포도 그리기
import matplotlib.pyplot as plt 

plt.plot(df["X"], df["Y"], "o")
plt.show()

from sklearn.linear_model import LinearRegression
X = X.reshape(-1,1)

model = LinearRegression()
model.fit(X, y)
print( model.coef_)  #기울기 
print( model.intercept_) #절편   Y = X*1.31318859 -159.4596565132859

#예측치 
y_pred = X*1.31318859 -159.4596565132859

print("관측칙 : ", y )
print("기대치 : ", y_pred )
print("기대치 : ", model.predict(X) )


for item in zip( y,y_pred, model.predict(X )):
    print( item )











