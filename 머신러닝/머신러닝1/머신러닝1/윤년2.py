
#[[1,2,3,4,5,6,7,8,9,10,11,12, .................]]
#[0,0,0,1,0,0,0,1,0, 0, 0, 1, .................]
#윤년은 4의 배수이고 100의 배수가 아니거나 400의 배수이어야 한다 
#입력데이터 : 2차원 ndarray, 결과데이터(label):1차원 ndarray 
def isLeap(year): #연도를 입력받아서 윤년이면 1, 윤년이 아니면 0을 반환
    if year %4==0 and year%100!=0 or year%400==0:
        return 1 
    else:
        return 0 

print( isLeap(2000) ) #1
print( isLeap(1900) ) #0

#입력, 결과데이터 만들기 
input_data=[] #비어있는 list타입 만들고 
output_data=[]#비어있는 list타입 만들고 
for i in range(1, 2023):
    input_data.append(i)
    output_data.append( isLeap(i) )

#타입전환 
import numpy as np 
input_data = np.array(input_data)
#차원하나 추가하기(무조건 2차원으로 맞춰야 한다. 현재 1차원이라 차원을 추가) 
input_data = input_data.reshape(-1, 1) 
print( input_data.shape )

output_data=np.array(output_data) #형전환 

from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split( input_data, 
   output_data, test_size=0.4, random_state=1)

print( X_train.shape )
print( X_test.shape )
print( X_train[:20] )
print( y_train[:20] )

#from sklearn.tree import DecisionTreeClassifier
#model = DecisionTreeClassifier(random_state=1)

#Knn 이웃알고리즘 : 유클리드 기하학(두 점사이의 거리를 젠다)
#비슷한 사람끼리 이웃에 한다 
#고구마밭에 심은건 고구마고 인삼밭에 심은건 인삼이다.
#옆에 이웃에 고구마가 보이면 나도 고구마다. 
#옆에 사는 이웃을 하나만, 2, 3, 4, 5, 선택가능하다. 
#이웃의 숫자가 계속 늘면 과대적합확률이 높아진다. 
#  
from sklearn.neighbors import KNeighborsClassifier

#학습을 시작한다 
model = KNeighborsClassifier(n_neighbors=3)
model.fit( X_train, y_train )

#예측을 한다 
y_pred = model.predict(X_test) #예측값을 가져온다 

for i in zip(y_test, y_pred):
    print(i, i[0]==i[1])

#예측률 출력하기 - 과대적합을 확인하기 위해 둘다 봐야 한다 
print( "훈련셋 {}".format( model.score(X_train, y_train)))
print( "테스트셋 {}".format( model.score(X_test, y_test)))

#  1, 0.5327564894932015
#  2, 
# 훈련셋 0.7724649629018961
# 테스트셋 0.723114956736712
# 3, 훈련셋 0.761747732893652
#테스트셋 0.6736711990111248













