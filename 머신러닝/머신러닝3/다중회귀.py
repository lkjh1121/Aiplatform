from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

#1.데이터 가져오기 
boston = load_boston()
df1 = pd.DataFrame( boston['data'], columns=boston['feature_names'])
df1["target"] = boston["target"]

print( df1.head() )

#상관계수 행열 
print( df1.corr() )

#산포도 
# sns.set_style()
# sns.pairplot(data=df1,palette='dark')
# plt.show()
#관계성 있는 필드가 선택해서 그려야 한다 

X_train, X_test, y_train, y_test = train_test_split(boston['data'], 
   boston['target'], test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

#score 
print("----------- Linear Regression -------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))


#L2규제 - 가중치의 값을 0에 가깝게 해서 규제를 가한다 
from sklearn.linear_model import Ridge 
model = Ridge(alpha=0.01) #일반적으로 alpha값이 높아질수록 과대적합이 줄어든다.(반드시그런건아님) 
model.fit(X_train, y_train)

#score 
print("----------- Ridge -------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

from sklearn.linear_model import Lasso 
model = Lasso(alpha=0.01)  
model.fit(X_train, y_train)

#score 
print("----------- Lasso -------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))


#pip install mglearn 

