from email.mime import image
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd
import numpy as np
# 차트 한글 깨짐 
plt.rcParams['axes.unicode_minus']=False
plt.rcParams["font.family"] = "malgun Gothic"

from sklearn.datasets import fetch_lfw_people
# 처음에 호출 할 때 네트워크로 다운로드 받는다.
# 사진이 최소한 20장씩 있는 사람 정보만 다운받자.
people = fetch_lfw_people(min_faces_per_person=50, resize=0.7)
print(people.keys())
print(people['data'].shape)
print(people.images[0].shape) # 이미지를 2차원 => 색을 없앤 상태로 우리한테 전달
print(people.target[0])
print(people.target_names[11])

from PIL import Image
# plt.imshow(people.images[0])
# plt.show()

# 이미지를 여러개 출력해 보자
fig, axes = plt.subplots(2, 6, figsize=(15, 8),
                        subplot_kw={"xticks":(), "yticks":()}) # 축을 없앤다.
for target, image, ax in zip(people.target, people.images, axes.ravel()):
    ax.imshow(image)
    ax.set_title(people.target_names[target])
# plt.show()

# 사진이 최소한 50개는 되어야 학습을 한다.
counts = np.bincount(people.target)
print(counts) # 인덱스와 사진의 개수

# 50개 씩 있는 데이터 추출하기
X_people = people['data']
y_people = people['target']

print(X_people.shape)
print(y_people.shape)

# 스케일링 하기
X_people = X_people / 255   # 0~255 색상정보가 한계이다.

from sklearn.neighbors import KNeighborsClassifier
X_train, X_test, y_train, y_test = train_test_split(X_people, y_people, stratify=y_people, random_state=0)
# stratify - 데이터가 균일하게 분포하지 않았을때 실제 분포에 맞추어서 훈련셋과 테스트셋을 쪼개기 위해 사용하는 파라미터

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print("훈련셋", knn.score(X_train, y_train))
print("테스트셋", knn.score(X_test, y_test))

# 중요한 성분 100개만 5655개에서 100개만 빼보자
from sklearn.decomposition import PCA
pca = PCA(n_components=100, whiten=True, random_state=0)
pca.fit(X_train)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

knn.fit(X_train_pca, y_train)
print("훈련셋", knn.score(X_train_pca, y_train))
print("테스트셋", knn.score(X_test_pca, y_test))

# 결론 : 전체 성분으로 학습한 것 보다 주성분 학습이 오히려 효과가 좋을 수 도 있다.

# 주성분으로 이미지 그리기
fig, axes = plt.subplots(2, 6, figsize=(15, 8),
                        subplot_kw={"xticks":(), "yticks":()}) # 축을 없앤다.

# enumerate(list) => 인덱스와 데이터로 쪼개기
for i, (component, ax) in enumerate(zip(pca.components_, axes.ravel())):
    ax.imshow(component.reshape(87, 65), cmap="viridis")
    ax.set_title("주성분 {}".format((i+1)))
plt.show()