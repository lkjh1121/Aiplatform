from sklearn.datasets import load_sample_images
import matplotlib.pyplot as plt 
import PIL.Image as pilimg 
import numpy as np 

dataset = load_sample_images()
print( type(dataset) )
print(len( dataset.images)) 
img_rgb = dataset.images[0]
print(img_rgb.shape)

plt.imshow(img_rgb)
plt.show()
#pilimg- 이미지를 읽어서, numpy배열로 바꿀 수 있다 

flower = np.array( pilimg.open("./images/1.jpg"))
plt.imshow(flower)
plt.show() 

plt.figure(figsize=(20, 5)) #차트 크기를 키운다 
plt.subplot(1,4,1)  
plt.imshow(flower[0:500, 0:500, :])

plt.subplot(1,4,2)  
plt.imshow(flower[0:500, 0:500, 0])

plt.subplot(1,4,3)  
plt.imshow(flower[0:500, 0:500, 1])

plt.subplot(1,4,4)  
plt.imshow(flower[0:500, 0:500, 2])

plt.show() 

#개를 각각 5장씩 저장한다 
#파일을 읽어서 numpy 배열로 바꾸어서 , npz파일 만들기 
