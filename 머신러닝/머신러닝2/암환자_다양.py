#이진분류 악성이냐 아니냐 
from asyncio import threads
from regex import P
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
print("로지스틱 회귀 분석-------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)
print("의사결정트리 분석-------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=0, 
       max_depth=5, 
       n_estimators=100)
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)
print("랜덤포레스트 분석-------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))


#랜덤포스트의 하이퍼 파라미터 튜닝 
from  sklearn.model_selection import GridSearchCV
grid_params = {
    "max_depth":[8,16, 24],
    "min_samples_leaf":[1,6,12],
    "min_samples_split":[2,8,16],
    "n_estimators":[10, 50, 100]
}
#n_jobs : 시스템 내의 프로세서(cpu를)최대한으로 -1  
model = RandomForestClassifier(random_state=0, n_jobs=-1)
grid_cv = GridSearchCV(model, param_grid=grid_params, cv=2, n_jobs=-1)
grid_cv.fit(X_train, y_train)

print( "최적의 파라미터 ", grid_cv.best_params_)
print( "최고 예측 정확도 ", grid_cv.best_score_)

#{'max_depth': 8, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
model = RandomForestClassifier(max_depth=8, 
min_samples_leaf=1,min_samples_split=2,  n_estimators=50,
random_state=0, n_jobs=-1)
model.fit(X_train, y_train)
print("---------------------------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

#그라디언트 부스팅 
from sklearn.ensemble import GradientBoostingClassifier 

model = GradientBoostingClassifier(random_state=0, max_depth=1)
model.fit(X_train, y_train)
print("그라디언트부스팅 --------------------------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

import xgboost as xgb
from xgboost import XGBClassifier 
model = XGBClassifier(random_state=0, max_depth=1)
model.fit(X_train, y_train)
print("XGBoost --------------------------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

from sklearn.svm import SVC
model = SVC(random_state=0)
model.fit(X_train, y_train)
print("서포트벡터머신 --------------------------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", m                                                         ㅊ ㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊ ㅊ   ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    odel.score(X_test, y_test))
