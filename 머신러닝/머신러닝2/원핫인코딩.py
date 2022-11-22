from calendar import prcal
from sklearn.preprocessing import OneHotEncoder
import numpy as np
items = ["TV", "냉장고", "컴퓨터", "선풍기", "냉장고", "믹서", "믹서"]

# 원 핫 인코딩 적용
encoder = OneHotEncoder()
print(items)

# 2차원 nd.array로 변환
items = np.array(items).reshape(-1, 1) # 차원이 늘어서 2차원
print(items)


encoder.fit(items) # 학습 후
# 원핫인코더로 변환한 결과는 희소행렬이므로 toarray()를 이용해 밀집 행렬로 변환
labels = encoder.transform(items)
print(labels)
print(labels.toarray())

import pandas as pd

df= pd.DataFrame({"itme":["TV", "냉장고", "컴퓨터", "선풍기", "냉장고", "믹서", "믹서"]})

df2 = pd.get_dummies(df)
print(df2)

