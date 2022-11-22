from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
scalar.fit(iris['data'])

iris_data = scalar.transform(   iris['data'])
print(iris_data[:10, :])

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model2 = DecisionTreeClassifier()

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=500)
model2 = LogisticRegression(max_iter=500)

from sklearn.model_selection import train_test_split
X_train1, X_test1, y_train1, y_test1 = train_test_split(iris["data"], 
    iris['target'],
    test_size=0.3, random_state=1234)

X_train2, X_test2, y_train2, y_test2 = train_test_split(iris_data, 
    iris['target'],
    test_size=0.3, random_state=1234)

model.fit(X_train1, y_train1)
model2.fit(X_train2, y_train2)

print("정규화 전 : ", model.score(X_train1, y_train1))
print("정규화 후 : ", model2.score(X_train2, y_train2))

