import scipy.misc 

img_gray = scipy.misc.face(gray=True)
img_color = scipy.misc.face()
print(img_gray.shape)

#subplot(가로, 세로, 번호) 가로의 개수, 세로의개수 
import matplotlib.pyplot as plt 
plt.subplot(1,2,1)  #행은 하나 열은 2개로 쪼개서 1 번영역에 그림
plt.imshow(img_gray, cmap=plt.cm.binary)
plt.subplot(1,2,2)  #행은 하나 열은 2개로 쪼개서 2 번영역에 그림
plt.imshow(img_color)

plt.show()

import seaborn as sns 
#히트맵을 그려보자 
sns.heatmap( img_gray[:30, :30], 
 annot=True, #숫자를 표현해라 
 fmt="d", #숫자를 정수형태로 
 cmap=plt.cm.bone
)
plt.axis("off") #x축 y축 안보이게 
plt.show()

#칼라 히트맵 
sns.heatmap( img_gray[:20, :20], cmap="RdYlGn_r")
plt.show() 











