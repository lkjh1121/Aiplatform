from nltk import sent_tokenize #nltk - 자연어 처리를 담당한다 
import nltk 
nltk.download("punkt")

text_sample = """
To Kill a Mockingbird is a novel by the American author Harper Lee. 
It was published in 1960 and was instantly successful. 
In the United States, it is widely read in high schools 
and middle schools. To Kill a Mockingbird has become a classic 
of modern American literature, winning the Pulitzer Prize. 
The plot and characters are loosely based on Lee's observations 
of her family, her neighbors and an event that occurred near her 
hometown of Monroeville, Alabama, in 1936, when she was ten.
"""
#sent_tokenize - 문장단위로 쪼갬 
sentences = sent_tokenize(text_sample)
print( type(sentences), len(sentences))
print( sentences)

bards_words = sentences

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer() 
vect.fit(bards_words )

print("어휘사전의 크기 : ", len(vect.vocabulary_))
print("어휘사전의 내용 : ", vect.vocabulary_)

#희소행열을 밀집행렬로
bag_of_words = vect.transform(bards_words)
print(bag_of_words  )
print(bag_of_words.toarray())