from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, precision_score 
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.metrics import precision_recall_curve, roc_curve

from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#1.데이터 확인하기
diabetes = load_diabetes()
print( diabetes.keys() )
#print( diabetes["target_names"])
#print( diabetes["feature_names"])
print( diabetes["data"][:10, :])
print( diabetes["target"][:10])










