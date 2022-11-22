import pandas as pd 
titanic = pd.read_csv("./data/train_and_test2.csv")
print( titanic.head() )

#PassengerId 필드 삭제하기
titanic = titanic.drop( ["Passengerid", "Embarked"], axis=1)
print( titanic.head(3) )

#결측치 확인 
print( titanic.isna().sum() )
#결측치 제거하기 
titanic = titanic.dropna( axis=0 )  #0번째축(행)
#행중에 결측치가 하나라도 있는 열이 있으면 행을 삭제시킨다.
#반환값을 받아야 
# 
#열을 0~  
#X와 y로 쪼개자 
X = titanic.iloc[:, 0:5] 
y = titanic.iloc[:, -1] #타겟이 맨 뒤쪽에

print( X.head(3))
print( y.head(3))

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, 
    test_size=0.3, random_state=0)
print( X_train.shape )
print( X_test.shape )

from sklearn.linear_model import LogisticRegression

model = LogisticRegression() #객체를 만든다 

model.fit( X_train, y_train ) #내부에 변수로 연산을 한 결과를 갖고 있다

#예측값 자체는 보고서에 쓸 의미는 없다. 
y_pred = model.predict( X_test )

#소수점이하 2자리수 맞춰라 f - float 
# {  :자릿수지정}  자리수에 맞춰서 확보된다. 
print("훈련셋: {:.2f}".format(model.score( X_train, y_train )))
print("테스트셋: {:.2f}".format(model.score( X_test, y_test )))

#Knn 이웃알고리즘은 이웃의 숫자 지정가능 - 하이퍼파라미터 
from sklearn.neighbors import KNeighborsClassifier
#이 모델은 n_neighbors=3 를 조정해서 학습효과를 높일 수 있다 
model2 = KNeighborsClassifier(n_neighbors=6)
model2.fit(X_train, y_train) #학습하라
print("-- Knn 이웃 -------") 
print("훈련셋: {:.2f}".format(model2.score( X_train, y_train )))
print("테스트셋: {:.2f}".format(model2.score( X_test, y_test )))

#의사결정트리 
from sklearn.tree import DecisionTreeClassifier 
#무조건 과대적합 1이 될때까지 트리를 만들어가는데 트리의 깊이를 
#제약사항으로 준다. 트리의 깊이가 4까지만 가자 - 과대적합을 막는다
model3 = DecisionTreeClassifier(random_state=0, max_depth=4)
model3.fit(X_train, y_train) #학습하라
print("-- 의사결정트리 -------") 
print("훈련셋: {:.2f}".format(model3.score( X_train, y_train )))
print("테스트셋: {:.2f}".format(model3.score( X_test, y_test )))

#중요항목
import matplotlib.pyplot as plt
import numpy as np   
def treeChart(model, feature_names):
    #의사결정트리의 중요역할 - 중요항목을 찾아내는것 
    n_feature =  len(model.feature_importances_)
    #수평바차트  수직바차는 - bar
    plt.barh( 
        np.arange(n_feature), #y축()
        model.feature_importances_,#x축
        align="center"  
    )
    plt.yticks(np.arange(n_feature), feature_names)
    plt.ylim(-1, n_feature)
    plt.show()

treeChart(model3, np.array(X_train.columns))