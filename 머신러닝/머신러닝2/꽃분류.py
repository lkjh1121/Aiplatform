#1.파일을 읽어서 numpy 배열로 만들어야 한다 
#2.폴더별로 labeling 을 해야 한다 

import numpy as np 
import os 
import PIL.Image as pilimg #이미지 파일을 읽어서 numpy 배열로 바꾼다
import imghdr #이미지의 종류를 알아내고자 할때 사용
import pandas as pd 

def makeData(folder, label):
    data = [] #이미지 피처를 저장 
    labels =[]
    path = "./data/flowers/" + folder
    for filename in os.listdir(path): #해당 폴더의 파일명을 다 들고 온다
        try:
            print(path + "/" +filename)
            kind = imghdr.what(path + "/" +filename)
            #파일에 대한 정보를 준다 
            if kind in ["gif", "png", "jpg", "jpeg"]:
                img = pilimg.open(path + "/" +filename)
                #이미지 크기가 다 다르다. 이미지 크기를 맞춘다 
                resize_img = img.resize( (150, 150) ) #tuple로 줘야 한다
                pixel = np.array(resize_img) #ndarray로 전환
                if pixel.shape==(150,150,3):
                    data.append(pixel)
                    labels.append(label)
        except:
            print(filename + " error")

    #파일로 저장하자 
    np.savez("{}.npz".format(folder), data=data, targets=labels)
    print("파일저장완료")

# makeData("daisy", "0")
# makeData("sunflower", "1")
# makeData("rose", "2")
# makeData("dandelion", "3")
# makeData("tulip", "4")

#모든 npz를 읽어서 합친다. concatenate
daisy = np.load("daisy.npz")
sunflower = np.load("sunflower.npz")
rose = np.load("rose.npz")
dandelion = np.load("dandelion.npz")
tulip = np.load("tulip.npz")

data1 = daisy["data"]
target1 = daisy["targets"]
data2 = sunflower["data"]
target2 = sunflower["targets"]
data3 = rose["data"]
target3 = rose["targets"]
data4 = dandelion["data"]
target4 = dandelion["targets"]
data5 = tulip["data"]
target5 = tulip["targets"]

data = np.concatenate((data1, data2, data3, data4, data5), axis=0)
target = np.concatenate((target1, target2, target3, target4, target5), axis=0)

print( data.shape ) #4차원
print( target.shape )


#1. 4차원 -> 2차원 
data = data.reshape( data.shape[0], 150*150*3)
print( data.shape )


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split(data, 
    target, test_size=0.3, random_state=11)

model = LogisticRegression()
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)
print("로지스틱 회귀 분석-------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)
print("의사결정트리 분석-------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=0, 
       max_depth=5, 
       n_estimators=100)
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)
print("랜덤포레스트 분석-------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))


#랜덤포스트의 하이퍼 파라미터 튜닝 
from  sklearn.model_selection import GridSearchCV
grid_params = {
    "max_depth":[8,16, 24],
    "min_samples_leaf":[1,6,12],
    "min_samples_split":[2,8,16],
    "n_estimators":[10, 50, 100]
}
#n_jobs : 시스템 내의 프로세서(cpu를)최대한으로 -1  
model = RandomForestClassifier(random_state=0, n_jobs=-1)
grid_cv = GridSearchCV(model, param_grid=grid_params, cv=2, n_jobs=-1)
grid_cv.fit(X_train, y_train)

print( "최적의 파라미터 ", grid_cv.best_params_)
print( "최고 예측 정확도 ", grid_cv.best_score_)

#{'max_depth': 8, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
model = RandomForestClassifier(max_depth=8, 
min_samples_leaf=1,min_samples_split=2,  n_estimators=50,
random_state=0, n_jobs=-1)
model.fit(X_train, y_train)
print("---------------------------------")
print("훈련셋 : ", model.score(X_train, y_train))
print("테스트셋 : ", model.score(X_test, y_test))
