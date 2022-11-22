from sklearn.datasets import load_files 
import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer 
import matplotlib.pyplot as plt 

#파일 불러오기 
reviews_train = load_files("./data/aclImdb/train")
print( reviews_train.keys )


text_train = reviews_train.data
y_train = reviews_train.target 
print("타입 : ", type(text_train ) )
print("길이 : ", len(text_train ) )
print("text_train[:5]\n", text_train[:5])
print("y_train[:5]\n", y_train[:50])

#벡터화를 한다 
vect = CountVectorizer().fit(text_train) 
X_train = vect.transform( text_train ) #벡터화한다 

feature_names = vect.get_feature_names_out() 
print("특성의 개수 : ", len(feature_names)) 
print("앞에서 20개 특성만 확인 : ", feature_names[:20])

#쓸데없는 데이터들 제거하기
#컴프리핸션, 단축 리스트  
#b - binary 문자열 

#쓸데없는 문자열 제거하고 
text_train = [ doc.replace(b"<br />", b"") for doc in text_train ] #<br /> 태그제거
#다시벡터화 하고 
vect = CountVectorizer().fit(text_train) 
X_train = vect.transform( text_train ) #벡터화한다 
print( X_train.shape)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression() 
model.fit(X_train, y_train)
print("훈련셋 ", model.score(X_train, y_train) )

y_pred = model.predict(X_train) 
print( y_train[:50])
print( y_pred[:50])







