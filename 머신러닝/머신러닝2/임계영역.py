from sklearn.preprocessing import Binarizer

x = [
    [1, -1, 2],
    [2, 0, 0],
    [0, 1.1, 1.2]
]

binarizer = Binarizer(threshold=1.1)
print( binarizer.fit_transform(x)) #fit와 transform을 동시에 진행한다 


