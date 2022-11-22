import tensorflow as tf 
import pandas as pd 
#손글씨를 0~9로 되어 있는걸 읽어서 numpy배열로 바꾸어서 
#60000개와 10000 개로 쪼개서 준다 
mnist = tf.keras.datasets.mnist 
fashion_mnist = tf.keras.datasets.fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# a = pd.DataFrame(y_train)
# print( a[0].unique() )


import matplotlib.pyplot as plt 
from PIL import Image   #numpy -> Image로 바꿀 수 있다.
def imageShow(image):
    plt.imshow( image, cmap=plt.cm.binary) 
    plt.show() 

    #numpy 배열 -> 이미지로 전환
    im = Image.fromarray( image )
    im.save("1.jpg") #파일명을 1.jpg로 저장해보자 

#imageShow( X_train[0] )

def imageSave(image, index):
    #numpy 배열 -> 이미지로 전환
    im = Image.fromarray( image )
    im.save(f"./images/fashion_mnist/{index}.jpg") #파일명을 1.jpg로 저장해보자 
#60000 개 다 저장하려면 힘들어서 1000개만 
for i in range(0, 1000):
    imageSave(X_train[i], i)

print( X_train.shape )
print( y_train.shape )

# 28 by 28 그림이 60000개가 있다 
#2차원으로 바꾸자 
X_train = X_train.reshape(60000, 28*28)
X_test = X_test.reshape(10000, 28*28)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit( X_train, y_train)
y_pred = model.predict(X_test)

print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

#원상복구 
X_test = X_test.reshape(10000, 28, 28)
falseList = [] #서로 다른거 인덱스만 저장한다 
for i in range(0, len(y_test)):
    if y_test[i] != y_pred[i]:
        falseList.append({"index":i, "data":X_test[i],
        "original":y_test[i], "predict":y_pred[i]})

if len(falseList)>0:
    print( falseList[0]["index"],falseList[0]["original"], 
        falseList[0]["predict"] )
    imageShow(falseList[0]["data"])



