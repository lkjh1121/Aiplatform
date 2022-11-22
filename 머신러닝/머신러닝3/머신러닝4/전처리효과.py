import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer['data'], 
   cancer['target'],  random_state=0) 

print("스케일링(정규화, normalize) 전에 학습" )
from sklearn.svm import SVC #분류   SVR:회귀 
model = SVC(gamma="auto")
model.fit( X_train, y_train )
print("훈련셋 ", model.score(X_train, y_train))
print("테스트셋 ", model.score(X_test, y_test))

print("스케일링 후 ------------------")
from sklearn.preprocessing import MinMaxScaler 
scalar = MinMaxScaler()
scalar.fit(X_train)
X_train = scalar.transform(X_train)
X_test = scalar.transform(X_test)
model = SVC(gamma="auto")
model.fit( X_train, y_train )
print("훈련셋 ", model.score(X_train, y_train))
print("테스트셋 ", model.score(X_test, y_test))

