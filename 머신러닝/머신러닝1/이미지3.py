import os 
import matplotlib.pyplot as plt 
import PIL.Image as pilimg 
import numpy as np 

path="./images/animal"
filenameList = os.listdir(path) 
print(filenameList ) #해당 폴더에서 파일 목록을 가져온다 
imgList=[] 
for filename in filenameList:
    filepath = path + "/" + filename 
    print(filepath )
    temp = pilimg.open(filepath) 
    print( type(temp) ) #이미지 크기변환
    img = temp.resize( (150, 150)) #크기를 자동으로 맞춘다. 
    #크기를 tuple타입으로
    img = np.array( img )
    print( img.shape )
    imgList.append( img )

#저장하기 
np.savez("data1.npz", data=imgList)
print("파일저장완료")

data1 = np.load("data1.npz")["data"] 
import matplotlib.pyplot as plt 

plt.figure(figsize=(20, 5)) #차트 크기를 키운다
for i in range(1, 11): 
    plt.subplot(1,10,i)  
    plt.imshow(data1[i-1])

plt.show()





