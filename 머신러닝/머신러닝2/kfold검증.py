from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 


#1.분류 데이터 셋을 가져온다. (1,2,3,4중에 어디 해당되느냐라고 하면 무조건 분류임)
iris = load_iris() 

#2.데이터에 대해 확인해 본다.
print( iris.keys() )

print( iris["data"][:10, :] ) #numpy - 데이터 10개만 확인해보자 
print( iris["data"].shape) #데이터 전체 크기 확인 
#150개 피처:4개 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print( df.head())
print( df.info() )
print( df.describe()) #기본 통계량 확인 

#3.데이터를 훈련셋과 테스트셋으로 나눈다 
X_train, X_test, y_train, y_test = train_test_split( 
    iris['data'], iris['target'], test_size=0.3, 
    random_state=11
) 

print( y_train[:20] )

#모델을 작성한다 
model = DecisionTreeClassifier() 

#학습한다 
model.fit( X_train, y_train)

#예측하기 
y_pred = model.predict(X_test)

#평가하기 
print( "훈련셋 {}".format( model.score(X_train, y_train)))
print( "테스트셋 {}".format( model.score(X_test, y_test)))

#Kfold 평가 
from sklearn.model_selection import KFold

kfold = KFold(n_splits=5) #전체 구간을 5개로 쪼갠다 
iris_data = iris["data"]
iris_target = iris["target"]
n_iter=0 


# train_score = []
# test_score = []

# for train_index, test_index in kfold.split(iris["data"]):
#     print(f"{n_iter}번째------------")
#     # print(train_index)
#     print(test_index)
#     n_iter+=1

#     #데이터 분할하기
#     X_train = iris_data  [train_index]
#     X_test  = iris_data  [test_index]
#     y_train = iris_target[train_index]
#     y_test  = iris_target[test_index]

#     model = DecisionTreeClassifier() #모델 만들고 
#     model.fit(X_train, y_train)#학습하고 
    
#     train_score.append(model.score(X_train, y_train))
#     test_score.append (model.score(X_test, y_test))
    # print( "훈련셋 {}".format( model.score(X_train, y_train)))
    # print( "테스트셋 {}".format( model.score(X_test, y_test)))

# print(train_score)
# print(test_score)

print("================================================================================================")


train_score = []
test_score = []
# StratifiedGroupKFold  
from sklearn.model_selection import StratifiedGroupKFold
skf = StratifiedGroupKFold(n_splits=3)

for train_index, test_index in kfold.split(iris["data"], iris["target"]):
    print(f"{n_iter}번째------------")
    # print(train_index)
    print(test_index)
    n_iter+=1

    #데이터 분할하기
    X_train = iris_data  [train_index]  
    X_test  = iris_data  [test_index]
    y_train = iris_target[train_index]
    y_test  = iris_target[test_index]

    model = DecisionTreeClassifier() # 모델 만들고 
    model.fit(X_train, y_train)# 학습하고
    
    train_score.append(model.score(X_train, y_train))
    test_score.append (model.score(X_test, y_test))
    # print( "훈련셋 {}".format( model.score(X_train, y_train)))
    # print( "테스트셋 {}".format( model.score(X_test, y_test)))

print(train_score)
print(test_score)
print("=====================================================================================")
# 교차 검증 3번째 #############################################
# cross_val_score

# 트리의 최대 깊이를 4로 해라 
from sklearn.model_selection import cross_val_score, cross_validate
model = DecisionTreeClassifier(max_depth=4, random_state=156)
result = cross_val_score(model, iris['data'], iris['target'], 
        scoring="accuracy", # 정확도로 모델 평가하기
        cv=3) # 3개 구간으로 나누겠다.
print(result)
print(np.round(np.mean(result), 2))



# 하이퍼 파라미터
X_train, X_test, y_train, y_test = train_test_split( 
    iris['data'], iris['target'], test_size=0.2, 
    random_state=121
) 

# 교차검증과 하이퍼파라미터 튜닝을 동시에 = GridSearchCV
from sklearn.model_selection import GridSearchCV
model = DecisionTreeClassifier()

grid_parmaters = {
    "max_depth":[1,2,3,4],
    "min_samples_split":[2,3]}

grid_search = GridSearchCV(model, param_grid=grid_parmaters, cv=3, refit=True)

# 내부적으로 검증셋을 따로 만듬
# 훈련셋만으로 다시 훈련셋과 검증셋을 나눔
grid_search.fit(X_train, y_train)

scores_df = pd.DataFrame(grid_search.cv_results_)

print( scores_df [["params", "mean_test_score", "rank_test_score"]])