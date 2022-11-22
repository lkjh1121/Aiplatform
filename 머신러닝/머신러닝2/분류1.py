from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris() 

X_train, X_test, y_train, y_test = train_test_split(
    iris["data"], iris["target"], test_size=0.3, 
    random_state=1234
)

model = DecisionTreeClassifier(max_depth=4)
model.fit( X_train, y_train)

#graphviz   : https://graphviz.org/download 에서 다운받아 설치 후 
#cmd - 관리자 권한으로 실행   conda install python-graphviz 

from sklearn.tree import export_graphviz
export_graphviz(model, out_file="tree.dot", 
    class_names=iris["target_names"], 
    feature_names = iris["feature_names"],
    impurity=True,
    filled=True)

import graphviz 

#파일을 열고 읽고 닫는다 
#with 구문을 사용하면 파일을 알아서 닫는다
with open("tree.dot") as f:
    dot_graph = f.read()  

graphviz.Source(dot_graph).view() 

#중요도 그리기 
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt 
sns.barplot(x=model.feature_importances_, 
         y=iris["feature_names"])
plt.show()

 







