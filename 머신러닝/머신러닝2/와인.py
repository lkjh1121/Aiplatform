from unittest import result
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

wine = load_wine()
print( wine["feature_names"])
print( wine["target_names"])
print( wine["data"].shape)

X_train, X_test, y_train, y_test = train_test_split(wine['data'], wine['target'], 
    test_size=0.3, random_state=12) 

grid_parmaters = {"max_depth":[1,2,3,4,5]}

model = DecisionTreeClassifier()
grid_search = GridSearchCV(model, param_grid=grid_parmaters, cv=3, refit=True)
result = grid_search.fit(X_train, y_train)
import pandas as pd
df_res = pd.DataFrame(result.cv_results_)
print( df_res [["params", "mean_test_score", "rank_test_score"]])