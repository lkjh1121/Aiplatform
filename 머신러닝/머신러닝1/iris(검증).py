# K-fold 검증

from cgi import test
from random import random
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.keys()) # sklearn 라이브러리가 제공하는 데이터셋

# data , taget, featyre_names, target_names

input_data = iris["data"]
output_data = iris["target"]

# 현재 이 데이터 셋은 데이터가 한 개도 섞여 있지 않다.
print(input_data[:5])
print(output_data[:100])
"""
     머신러닝, iris라는 꽃이 있는데 이 꽃이 꽃 받침의 크기가 150건의 데이터를 갖고온다.
     4가지 속성의 길이를 재고 종류 
     setosa, vesicolor, versinica
     학습을 모의 고사와 실전고사 데이터를 6:4, 7:3, 8:2 비율로 쪼갠다
     train_test_split의 test_size=0.3 7:3으로 데이터를 쪼갠다.
     train_test_split 데이터를 골고루 섞는다. (shuffle)
     섞을때 인덱스를 추출해낸다. random_state를 이용해서
     random_state 값을 고정시켜주지 않으면 결과가 계속 바뀐다.
     1 ~ 65535 중에 아무거나 내 마음대로 지정할 수 있다.W@
"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.3, random_state=0) # ★☆

# iris 분류 = 품종 맞추기(분류)
from sklearn.linear_model import LogisticRegression

# 선형회귀 모델처럼 직선 방정식으로 구함
model = LogisticRegression()
model.fit(X_train, y_train) # 학습을 하고 학습 내용은 model에 저장

print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

from sklearn.tree import DecisionTreeClassifier

# 트리의 깊이를 3까지를 맥시멈으로
model2 = DecisionTreeClassifier(max_depth=3, random_state=156)
model2.fit(X_train, y_train) # 학습을 하고 학습내용은 model에 저장
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

print("===============================================================================")

# K-fold 검증기법 : 여러개로 나누어서 돌아가면서 test set을 만들어준다.
from sklearn.model_selection import KFold

kfold = KFold(n_splits=5) # 쪼갤 개수 : 전체를 5개의 구간으로 나누겠다.


i=1
train_score=[]
test_score=[]

for train_index, test_index in kfold.split( input_data ):
    # print("훈련셋 인덱스 : ", train_index)
    # print("테스트셋 인덱스 : ", test_index)

    X_train, X_test = input_data[train_index], input_data[test_index]
    y_train, y_test = output_data[train_index], output_data[test_index]
    model.fit(X_train, y_train)
    # print(f"{i} --------")
    # print("훈련셋", model.score(X_train, y_train))
    # print("테스트셋", model.score(X_test, y_test))
    i = i+1
    train_score.append(model.score(X_train, y_train))
    test_score.append(model.score(X_test, y_test))

print("훈련셋 : ", train_score)
print("테스트셋 : ", test_score)
print("===============================================================================")
# 품종2개만 훈련셋으로 가고 테스트셋에는 앞에 2개 하고 관계없는 종류
# X_train, X_test, y_train, y_test = input_data[:100],
# input_data[100:], output_data[:100], output_data[100:]
X_train = input_data[0:100, :] # ndarray 타입 = 2차원
X_test = input_data[100:, :]
y_train = output_data[:100]      # 1차원
y_test = output_data[100:]

import pandas as pd
print(pd.Series(y_train).value_counts() )
print(pd.Series(y_test).value_counts() )

model.fit(X_train, y_train)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

# KFold 문제점은 데이터를 섞지를 않아서, 분류하고자하는 데이터셋이 균등하게 들어가야하는데
# 그렇지 않을 경우 위험하다.
# StratifiedFold를 써서 바꾸자

from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=3)

train_scores=[]
test_scores=[]
for train_index, test_index in skf.split(input_data, output_data):
    X_train, X_test = input_data[train_index], input_data[test_index]
    y_train, y_test = output_data[train_index], output_data[test_index]
    print(test_index)
    model.fit(X_train, y_train)
train_scores.append(model.score(X_train, y_train))
test_scores.append(model.score(X_test, y_test))

# cross_val_score 간단 검증 함수
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, input_data, output_data, scoring='accuracy',cv=3)
import numpy as np
print("교차검증 정확도", np.round(scores, 4))