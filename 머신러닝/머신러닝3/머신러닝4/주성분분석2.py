import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import seaborn as sns 
import pandas as pd 

#차트한글 안깨지게 
plt.rcParams['axes.unicode_minus']=False 
plt.rcParams['font.family'] = 'Malgun Gothic'

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer['data'], 
   cancer['target'],  random_state=0) 

#데이터 프레임으로 만들자 (numpy 배열을 -> dataframe으로)
df1 = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
df1['target'] = cancer['target']
print(df1.head(5))

#주성분분석을 이용해서 특성들중에서 특별히 주가 되는 성분을 빼내서 
#새로운 특성을 만든다. 30개 -> 2개로 특성을 줄이자 

from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
scalar.fit(cancer['data'])
X_scaled = scalar.transform(cancer['data'])

from sklearn.decomposition import PCA 
#두개의 주성분만 추출한다 
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled) 
print("원본데이터 ", X_scaled.shape)
print("축소된 데이터 ", X_pca.shape)

import mglearn
plt.figure(figsize=(8, 8))
#X1, X2, Y 차트그리는걸 쉽게 하려고 sklearn개발자가 따로 만들었음
mglearn.discrete_scatter( X_pca[:, 0], X_pca[:,1], cancer['target'])
plt.legend(["악성", "양성"], loc='best')
plt.gca().set_aspect("equal") #앞에 축하고 동등하게 
plt.xlabel("첫번째 주성분")
plt.ylabel("두번째 주성분")
plt.show() 


# components_ : 주요성분만 여기 기록된다. 
print("주성분 형태")
print(pca.components_.shape)
print("주성분값")
print(pca.components_)


#히트맵을 그려보자 
plt.matshow(pca.components_, cmap="viridis")
plt.yticks( [0,1], ["첫번째주성분", "두번째주성분"])
plt.colorbar() 
plt.xticks(range(len(cancer['feature_names'])), 
              cancer['feature_names'], ha='left', rotation=60)
plt.ylabel("특성")
plt.xlabel("주성분")
plt.show()


X_train, X_test, y_train, y_test = train_test_split(cancer['data'], 
   cancer['target'],  random_state=0) 

X_train_scaled, X_test_scaled, y_train, y_test =  \
    train_test_split(X_scaled, 
   cancer['target'],  random_state=0) 

X_train_pca, X_test_pca, y_train, y_test =  \
    train_test_split(X_pca,  cancer['target'],  random_state=0) 


from sklearn.linear_model import LogisticRegression
model = LogisticRegression() 

model.fit( X_train, y_train)
print("--- 원본데이터 학습")
print("훈련셋 ", model.score(X_train, y_train))
print("테스트셋 ", model.score(X_test, y_test))

model.fit( X_train_scaled, y_train)
print("--- 스케일데이터 학습")
print("훈련셋 ", model.score(X_train_scaled, y_train))
print("테스트셋 ", model.score(X_test_scaled, y_test))

model.fit( X_train_pca, y_train)
print("--- 주성분 학습")
print("훈련셋 ", model.score(X_train_pca, y_train))
print("테스트셋 ", model.score(X_test_pca, y_test))










