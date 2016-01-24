import nltk
import string
import numpy as np
from collections import Counter
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn import svm


##############################################################
#step 2: 
token_dict = {}


def tokenize(text):
    tag=['NN','IN','JJ','NMS','VBP','RB','VB','VBD']
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    token=list()
    for item in tagged:
        if item[1] in tag:
            token.append(item[0])  
    return token

with open('train.txt') as stopF:
    text = stopF.read()
    token_dict['stp'] = text.lower().translate(None, string.punctuation)

stopF.close()

##############################################################
#step 3: 1)tf-idf for words in tweet mirizim to bag of word -> dict{word:tfidf,...}
#        2) k ta bishtar ro mirizim to k_best : listTuple[(word,tfidf),...]
#        3) best faghat shamele word ha to k_best

tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

str=text
response = tfidf.transform([str])

feature_names = tfidf.get_feature_names()

bag_of_word=dict()
for col in response.nonzero()[1]:
    bag_of_word[feature_names[col].encode("utf-8")]= response[0, col]


k = 50
count = Counter(bag_of_word)
k_best = count.most_common(k)
best=list()


f = open("feature.txt", "wb")
for i in range(k-1):
    f.write(k_best[i][0]+"\n")
f.close()
    
