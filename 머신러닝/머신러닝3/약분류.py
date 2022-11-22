from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
drug = pd.read_csv('./data/drug200.csv')
print(drug)

def encode(df):
    df['Drug'] = df['Drug'].str[4]
    features = ['Sex', 'BP', 'Cholesterol', 'Drug']
    for feature in features:
        lb = LabelEncoder()
        lb = lb.fit(df[feature])
        df[feature] = lb.transform(df[feature])
    return df

encode(drug)
data = drug.iloc[:, :-1]
target = drug.iloc[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=11)

from sklearn.linear_model import LogisticRegression
log = LogisticRegression(solver = 'liblinear')
log.fit(X_train, y_train)
y_pred = log.predict(X_test)
print('--------------------------------------LogisticRegression----------------------------------')
print('훈련셋 : ', log.score(X_train, y_train))
print('테스트셋 : ', log.score(X_test, y_test))
print('정확도 : {:.4f}'.format(accuracy_score(y_test, y_pred)))

#print('정밀도 : {:.4f}'.format(precision_score(y_test, y_pred, average='macro')))
#print('재현율 : {:.4f}'.format(recall_score(y_test, y_pred, average='macro')))

from sklearn.ensemble import GradientBoostingClassifier
ran = GradientBoostingClassifier(max_depth=5)
ran.fit(X_train, y_train)
y_pred = ran.predict(X_test)
print('--------------------------------------GradientBoostingClassifier----------------------------------')
print('훈련셋 : ', ran.score(X_train, y_train))
print('테스트셋 : ', ran.score(X_test, y_test))
print('정확도 : {:.4f}'.format(accuracy_score(y_test, y_pred)))
#print('정밀도 : {:.4f}'.format(precision_score(y_test, y_pred, average='macro')))
#print('재현율 : {:.4f}'.format(recall_score(y_test, y_pred, average='macro')))

from xgboost import XGBClassifier
scg = XGBClassifier()
scg.fit(X_train, y_train)
y_pred = scg.predict(X_test)
print('--------------------------------------XGBClassifier----------------------------------')
print('훈련셋 : ', scg.score(X_train, y_train))
print('테스트셋 : ', scg.score(X_test, y_test))
print('정확도 : {:.4f}'.format(accuracy_score(y_test, y_pred)))
#print('정밀도 : {:.4f}'.format(precision_score(y_test, y_pred, average='macro')))
#print('재현율 : {:.4f}'.format(recall_score(y_test, y_pred, average='macro')))

from sklearn.svm import SVC
sc = SVC()
sc.fit(X_train, y_train)
y_pred = sc.predict(X_test)
print('--------------------------------------SVC----------------------------------')
print('훈련셋 : ', sc.score(X_train, y_train))
print('테스트셋 : ', sc.score(X_test, y_test))
print('정확도 : {:.4f}'.format(accuracy_score(y_test, y_pred)))
#print('정밀도 : {:.4f}'.format(precision_score(y_test, y_pred, average='macro')))
#print('재현율 : {:.4f}'.format(recall_score(y_test, y_pred, average='macro')))