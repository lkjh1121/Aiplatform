from sklearn.datasets import load_digits 
from sklearn.datasets import load_wine
digits = load_digits()
print( digits["feature_names"])
print( digits["target_names"])
print( digits["data"].shape)



