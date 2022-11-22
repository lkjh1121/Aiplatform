#결정트리1.py 

from sklearn.datasets import make_classification
import matplotlib.pyplot as plt 

#가짜 데이터 만들기 
#피처-2개, 클래스-3 
X_data, y_target = make_classification(n_features=2, 
 n_redundant=0, n_informative=2, 
 n_classes=3, n_clusters_per_class=1, random_state=0)

import seaborn as sns 
sns.set_style('darkgrid')
#darkgrid, whitegrid, dark, white, ticks 

#그래프 작성- 산포도 
plt.scatter(X_data[:,0], X_data[:,1], marker='o', 
   c=y_target, s=50, edgecolor='k')
plt.show()

#결정경계 - 클래스 세개를 분류하기 위한 경계선 그리기 
from sklearn.tree import DecisionTreeClassifier 

tree = DecisionTreeClassifier(min_samples_leaf=6, random_state=156)
tree.fit(X_data, y_target)

import numpy as np 
def visualize_boundary(model, X, y):
    fig,ax = plt.subplots()
    
    # 학습 데이타 scatter plot으로 나타내기
    ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow', edgecolor='k',
               clim=(y.min(), y.max()), zorder=3)
    ax.axis('tight')
    ax.axis('off')
    xlim_start , xlim_end = ax.get_xlim()
    ylim_start , ylim_end = ax.get_ylim()
    
    # 호출 파라미터로 들어온 training 데이타로 model 학습 . 
    model.fit(X, y)
    # meshgrid 형태인 모든 좌표값으로 예측 수행. 
    xx, yy = np.meshgrid(np.linspace(xlim_start,xlim_end, num=200),np.linspace(ylim_start,ylim_end, num=200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    
    # contourf() 를 이용하여 class boundary 를 visualization 수행. 
    n_classes = len(np.unique(y))
    contours = ax.contourf(xx, yy, Z, alpha=0.3,
                           levels=np.arange(n_classes + 1) - 0.5,
                           cmap='rainbow', clim=(y.min(), y.max()),
                           zorder=1)

visualize_boundary(tree, X_data, y_target)
plt.show()







