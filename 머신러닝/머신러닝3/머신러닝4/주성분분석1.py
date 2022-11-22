import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import seaborn as sns 
import pandas as pd 
cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer['data'], 
   cancer['target'],  random_state=0) 

#데이터 프레임으로 만들자 (numpy 배열을 -> dataframe으로)
df1 = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
df1['target'] = cancer['target']
print(df1.head(5))

#특성이 너무 많아서 시각화를 사용할 수 없다
# sns.set_style()
# sns.pairplot(df1, hue="target")
# plt.show()

#주성분분석없이, 악성과 양성 두 클래스에 대해서 각각 히스토그램을 그리는 
#방법도 있다 
fig, axes = plt.subplots(15, 2, figsize=(10, 20))
#subplot 함수는 플롯의 영역을 행과 열로 나누는 일을 한다. 
#15행과 2열로 나누고 플롯 전체의 크기는 figsize로 지정해서 10 by 20으로 키운다
#figsize의 정확한 단위는 설명서에 없음 
#반환값이 tuple 타입인데 fig - 플롯 크기, axes 는 축정보이다. 
#이 정보를 이용해 차트를 지정된 위치에 출력할 수 있다 

#악성, 양성데이터 추출 
cancer_data = cancer['data'] 
cancer_target = cancer['target']
malignant = cancer_data[cancer_target==0] 
benign =  cancer_data[cancer_target==1]

import numpy as np 

ax = axes.ravel() #축에 대한 정보 
for i in range(30):
    #np.histogram - 히스토그램을 그리기 위해서 구간을 나눈다 
    #구간의 개수를 50로 지정하면, 데이터 범위에 따라서 
    #각 구간을 나누고 구간 배열을 반환한다. tuple로 반환 
    #첫번째 값을 안쓰고 두번째 값을 사용한다. 
    #예) 1~100 : 구간을 20  [1,5,10,15,20.....]
    #각 열단위로 구간을 나누어서 출력한다 
    _, bins = np.histogram(cancer_data[:, i], bins=50)
    #첫번째 구간 인덱스, 두번째 구간값 첫번째값은 버림 
    #print( bins )
    #서브플롯이 15, 2로 만들면 30개 만들어진다. 
    #각 구간의 인덱스가 0,1,2,3,4,5,6,7, ......... 29개가 된다 
    ax[i].hist( malignant[:, i], bins=bins, color="purple", alpha=0.5)
    #alpha - 투명도 
    ax[i].hist( benign[:, i], bins=bins, color="green", alpha=0.5)
    ax[i].set_title(cancer['feature_names'][i])
    ax[i].set_yticks(()) #y축 눈금 없앰 

ax[0].set_xlabel("특성크기")
ax[0].set_ylabel("빈도")
ax[0].legend(["악성", "양성"], loc="best")
#범주를 놓는데 loc는 범주의 위치를 지정하는 값이다. 이때 best를 주면 
#스스로 차트를 분석해서 적당한 위치를 찾아 범주를 출력한다
fig.tight_layout()
plt.show()



#주성분분석을 이용해서 특성들중에서 특별히 주가 되는 성분을 빼내서 
#새로운 특성을 만든다. 30개 -> 2개로 특성을 줄이자 



