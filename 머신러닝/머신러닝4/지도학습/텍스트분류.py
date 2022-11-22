bards_words = ["I like star",  \
                "red star, blue star",  \
                "I like dog"]

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
vect.fit(bards_words)

print("어휘사전의 크기 : ", len(vect.vocabulary_))
print("어휘사전의 내용 : ", vect.vocabulary_)

# 희소행열을 밀집행렬로 
bag_of_words = vect.transform(bards_words)
print(bag_of_words)
print(bag_of_words.toarray())