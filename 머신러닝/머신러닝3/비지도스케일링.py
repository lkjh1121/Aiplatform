from matplotlib.pyplot import table
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer['data'], 
   cancer['target'], test_size=0.3, random_state=1) 

from sklearn.preprocessing import MinMaxScaler 
scalar = MinMaxScaler()
scalar.fit(X_train)

X_train_scaled = scalar.transform(X_train)
X_test_scaled = scalar.transform(X_test)

print("스케일 조정전 특성별 최소값 : ", X_train.min(axis=0))
print("스케일 조정전 특성별 최대값 : ", X_train.max(axis=0))

print("스케일 조정후 특성별 최소값(훈련셋) : ", X_train_scaled.min(axis=0))
print("스케일 조정후 특성별 최대값(훈련셋) : ", X_train_scaled.max(axis=0))
print("스케일 조정후 특성별 최소값(테스트셋) : ", X_test_scaled.min(axis=0))
print("스케일 조정후 특성별 최대값(태스트셋) : ", X_test_scaled.max(axis=0))

print( X_train[:1, :])
print( X_train_scaled[:1 :])


from sklearn.preprocessing import StandardScaler 
scalar = StandardScaler()
scalar.fit(X_train)

X_train_scaled = scalar.transform(X_train)
X_test_scaled = scalar.transform(X_test)

print( X_train[:1, :])
print( X_train_scaled[:1 :])
