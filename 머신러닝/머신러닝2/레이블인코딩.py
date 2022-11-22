from sklearn.preprocessing import LabelEncoder

items = ["TV", "냉장고", "컴퓨터", "선풍기", "냉장고", "믹서", "믹서"]
encoder = LabelEncoder() # 객체만들기
encoder.fit( items )

labels = encoder.transform( items )
print( labels )

print(encoder.classes_)
print(encoder.inverse_transform([3,2,4,1,0]))