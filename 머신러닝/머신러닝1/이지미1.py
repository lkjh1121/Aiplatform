import scipy.misc 

img_gray = scipy.misc.face(gray=True)
print(img_gray.shape)

import matplotlib.pyplot as plt 
plt.imshow(img_gray, cmp=plt.cm.binary)
plt.show()
