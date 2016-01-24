import nltk
import string
import numpy as np
from collections import Counter
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn import svm

#step 4 : create vector for train set:
count=1
vector=dict()
best=list()
k=600
n=0
with open('feature.txt') as f :
    for i in f.readlines():
	if n<k:
        	best.append(i)
		n=n+1
f.close()   

with open('train.txt') as tweetFile:
    tweet = tweetFile.readlines()
    for statment in tweet:
        vecOfTweet=list()
        for item in best:
            if item in statment:
                vecOfTweet.append(1)
            else:
                vecOfTweet.append(0)
        #print vecOfTweet
        vector[count]=vecOfTweet
        count +=1
tweetFile.close()
print "create vector for train set"
#print vector
count=1
vector_test=dict()

with open('test.txt') as tweetFile:
    tweet = tweetFile.readlines()
    for statment in tweet:
        vecOfTweet=list()
        for item in best:
            if item in statment:
                vecOfTweet.append(1)
            else:
                vecOfTweet.append(0)
        #print vecOfTweet
        vector_test[count]=vecOfTweet
        count +=1
tweetFile.close()
print "create vector for test set"




################################################
#There are 3 types of labels with each label will be trained apart
#label s
#label w
#label k
#for example for label s:
list_file_train=['train_lable_s.txt','train_lable_w.txt','train_lable_k.txt']
list_file_test=['test_lable_s.txt','test_lable_w.txt','test_lable_k.txt']
size=[5,4,15]
for z in range(3):

	lable=list()
	with open(list_file_train[z]) as f :
	    for i in f.readlines():
		lable.append(i)
	f.close()

	s=list()
	with open(list_file_test[z]) as f :
	    for i in f.readlines():
		s.append(i)
	f.close()

	X=vector.values()
	clf = svm.SVC()
	clf.fit(X, lable) 
	print "finish train"
	t=vector_test.values()
	pre=clf.predict(t)

	print "finish learning and predicting",list_file_train[z],"\n"

	sum_miss = 0
	for i in range(38973):
	    c=0
	    for j in range(size[z]):
		    if s[i][j]!=pre[i][j]:
			c+=1
	    sum_miss=float(sum_miss)+(float(c)/5)

	print "The percentage of correct predictions : ",100-((sum_miss/38973)*100)




