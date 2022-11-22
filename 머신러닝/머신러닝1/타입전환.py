import numpy as np 
import pandas as pd
from sqlalchemy import column 

list1 = [1,2,3,4,5]  #파이썬의 list타입 
a1 = np.array(list1) #ndarray

d1 = pd.DataFrame(list1, columns=["열1"])
print( d1 )

d2 = pd.DataFrame(a1, columns=["열1"])
print( d2 )


columns = [ "열1", "열2", "열3"]
data1 = [[1,2,3], [4,5,6]]

df1 = pd.DataFrame(data1, columns = columns)
print( df1 )

#속성임 - 괄호없음
a = df1.values
print(a)
print( type(a) )

b = df1.values.tolist()
print( b )
print( type(b) )

#데이터프레임을 dict(dictionary, hash)타입으로 바꾸고자 할떼
c = df1.to_dict('list')
print( c )






