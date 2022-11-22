from re import T
from tokenize import Triple
from turtle import title
import pandas as pd

titanic = pd.read_csv("./train.csv")
print(titanic.head())
"""
    파이썬은 가상 환경 = 자기만의 가상환경을 만들어서 그 공간 안에서 작업이 가능하다.
    파이썬 버전을 여러개 쓰려면( 웹 개발시 보통 가상환경을 많이 사용한다. )
    아나콘다는 conda 라는 가상한경을 스스로 만들고 아나콘다 버전만 설치하면 없지만
    보통 python이 설치되어 있는 경우에는 pip가 어떤 경로를 보고 있는지 확실하지 않다.
    conda activate라고 치면 아나콘다 가상환경이 작동된다.
    명령 프롬프트 창 맨 첫번째 이름에 (base)가 나와야 한다. 
""" # ex) (base) C:\Users\ASUS\Desktop\Aiplatform
# Rstring  - 문자열로 경로를 작성하고 이 경로에 \ 가 있으면 특별한 기능의 제어 문자로 파악한다.
# \에 부여된 기능을 일시적으로 해제한다.
# ex) C:\Desktop\Aiplatform\titanic.csv
# ex) C:탭Desktop탭Aiplatform\titanic.csv
# 이걸 방지하려면 ex) C:\\Desktop\\Aiplatform\\titanic.csv
# ex)  r"C:\Desktop\Aiplatform\titanic.csv"
print(titanic.info())
"""
     Cabin 컬럼 탈락
     탈락이나 추가를 하면 새로운 데이터 집합을 리턴하는 구조
     내부적으로 처리속도가 빨라서, 요즘에 나오는 대부분의 데이터 타입들이
     반환값을 받아야 변경된 데이터를 가질수 있다.
     drop 함수가 행 또는 열 다 삭제 가능 axis=0 행, 1이면 열이다.
"""
t1 = titanic.drop("Cabin", axis=1)
print(t1.columns)
print(t1.isna().sum())

# 행을 삭제하자 = NaN 값이 있으면 그 행 전체를 삭제해야 한다.
t1 = t1.dropna(axis=0) # 행 안에 컬럼중에 NaN값이 있으면 무조건 삭제 된다.
print(t1.info())

# 비 범주형 자료애 대한 통계값만 보여준다.
print( t1.describe() )

# PassengerId - 쓸모없는 필드
# t1 = t1.drop("PassengerId", axis=1)
t1 = t1.iloc[:, 1:]
print(t1.head())

# 범주형 자료의 경우 분석에 가장 유용한 함수는 value_counts()
print(t1["Pclass"].value_counts())

pclass = t1["Pclass"]
print(pclass.head())
print(type(pclass))


# 데이터 프레임은 행과 열로 구성된다.
# 각 행을 레코드라고 표현한다 , 각 열을 속성( attribute ) 라고 표현한다,
# 데이터베이스가 레코드 - 한명분(1인분)의 데이터

# index 확인
print(t1.index)
print(t1.index.values)

# 새로운 index를 부여한 객체를 반호나
t2 = t1.reset_index(inplace=False, drop=True)

# 자기 자신의 값을 바꾸면서 새로운 index컬럼이 만들어진다. 귀찮음
# t1.reset_index(inplace=True) # 새로운 index 컬럼이 만들어진다.
# print(t1.index.values)
# print(t1.head())

print(t2.head())
# print(t2.index.values)
#print(t2["survived"].head())
#print(t2[["survived", "pclass"]].head())

# 행은 선택 할 수 있다.
print(t2[0:3])
# t2["pclass"]==3 : 데이터 프레임이나 넘파이가 벡터연산을 수행한다.
# t2["pclass"][0] == 3    True
# t2["pclass"][1] == 3    False
# t2["pclass"][2] == 3    True
# 데이터 개수 만큼 True 또는 False의 집합이 만들어지고 그 결과에서 True 인 데이터만 반환한다.
# 행을 필터링 할 수 있다.
print(t2[t2["Pclass"]==3].head())

# t2.shpe = tuple로 행과 열을 반환 [0]이 행이고 [1] 열의 개수이다.
for i in range(0, t2.shape[0]):
    for j in range(0, t2.shape[1]):
        print(t2.iloc[i,j], end=",")
    print()

# iloc 와 loc 사용법 

# 데이터프레임이 2차원 행과 열로 구성 : iloc[행, 열]
print( t1.iloc[0, 0] ) # 0번행에 0번 칼럼
print( t1.iloc[2, 3] ) # 2번행에 3번 칼럼

# numpy, dataframe이 되었던 슬라이싱 - 인덱스를 어디부터 어디까지
print( t1.iloc[0:5, 0] ) # 0~5행, 0번 열에

# 슬라이싱 시작:종료:증가 마지막 증가 부분은 생략하면 1로 받아들인다.
print( t1.iloc[0:5:1, 0] ) # 0~5번행, 0번열에

# 슬라이싱은 행 또는 열 양쪽에 지정할 수 있다.
print( t1.iloc[:, 0:2] ) # 행 전체 열은 0과 1만
 
print( t1.iloc[:, 0::2] ) # 행 전체\, 열은 0, 2, 4, 6

print( t1.iloc[:, [1,0,3] ] )

# 행의 이름이나 열의 이름, 보통 행은 이름이 없음 그래서 인덱스 대신 사용
# 열은 이름으로

print( t1.loc[:, ["Pclass", "Sex"] ] )

titanic = pd.read_csv("./train.csv")
# 불리한 인덱싱 = 연산 수행 결과가 True  또는 False의 벡터로 나타난다.

t20 = titanic[0:20] # 데이터 20개만 자르자(추출)
print(t20)

# 생존자만 유출하기
print(t20['Survived']==1) # 생존자 정보

survived = t20 [t20['Survived']==1] # 값이 True인 행만 반환
print(survived.loc[:, ["Survived", "Pclass", "Sex"]])

print(t20 [ t20['Survived']==1][
    ["Survived", "Pclass", "Sex"]].head(3))

print(titanic[(titanic["Age"]>=60) & (titanic["Pclass"]==1) & (titanic["Sex"]=="female")])

cond1 = titanic["Age"]>=60
cond2 = titanic["Pclass"]==1
cond3 = titanic["Sex"]=="female"
print(titanic[cond1 & cond2 & cond3])

# 정렬
titanic.sort_values(by=['Sex', 'Name'], ascending=[False, True])
print(t1.head())