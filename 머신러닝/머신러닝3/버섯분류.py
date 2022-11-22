from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # FutureWarning 제거

mushrooms = pd.read_csv("./data/mushrooms.csv")
print(mushrooms.shape)
print(mushrooms.columns)
mushrooms.head()

#타겟과 피쳐 분리하기 
data = mushrooms.drop('class', axis=1)
target = mushrooms['class']

# data는 원핫인코딩
oh_data = pd.get_dummies(data)

# target은 레이블인코딩
items=['e', 'p']
encoder = LabelEncoder()
encoder.fit(items)
l_target = encoder.transform(target)

print(oh_data.shape, l_target.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(oh_data, l_target, test_size=0.3, random_state=1)


# 알고리즘 분석
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print('----- 로지스틱회귀 분석 -----')
print("훈련셋 :", model.score(X_train, y_train))
print("테스트셋 :", model.score(X_test, y_test))

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print('----- 의사결정트리 분석 -----')
print('훈련셋 :', model.score(X_train, y_train))
print('테스트셋 :', model.score(X_test, y_test))

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=0, 
                               max_depth=4, n_estimators=100)
model.fit(X_train, y_train)
print('----- 랜덤포레스트 분석 -----')
print('훈련셋 :', model.score(X_train, y_train))
print('테스트셋 :', model.score(X_test, y_test))

from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(random_state=0, max_depth=1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print('----- 그라디언트 부스팅 -----')
print('훈련셋 :', model.score(X_train, y_train))
print('테스트셋 :', model.score(X_test, y_test))

import xgboost as xgb
from xgboost import XGBClassifier
model = XGBClassifier(random_state=0, max_depth=1,
                      eval_metric='mlogloss', 
                      use_label_encoder=False
                      )
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print('----- XGBoost -----')
print('훈련셋 :', model.score(X_train, y_train))
print('테스트셋 :', model.score(X_test, y_test))

from sklearn.svm import SVC
model = SVC(random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print('----- 서포트벡터머신 -----')
print('훈련셋 :', model.score(X_train, y_train))
print('테스트셋 :', model.score(X_test, y_test))