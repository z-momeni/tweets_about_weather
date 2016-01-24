#step 1: get tweet from train.csv:
import csv


write_tweet = open("train.txt", "wb")

with open('my_train.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     #print reader['tweet']
     for row in reader:
		 write_tweet.write(row['tweet'])
		 write_tweet.write("\n")
		 
write_tweet.close()


tweet_test = open("test.txt", "wb")

with open('my_test.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     #print reader['tweet']
     for row in reader:
		 tweet_test.write(row['tweet'])
		 tweet_test.write("\n")
tweet_test.close()

#lablae for test:

f_s = open("test_lable_s.txt", "wb")
f_w = open("test_lable_w.txt", "wb")
f_k = open("test_lable_k.txt", "wb")

with open('my_test.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     #r=['s1','s2','s3','s4','s5','w1','w2','w3','w4','k1','k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12','k13','k14','k15']
     s_i=['s1','s2','s3','s4','s5']
     w_i=['w1','w2','w3','w4']
     k_i=['k1','k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12','k13','k14','k15']
     lable=list()
     for row in reader:
		 l=""
		 for i in s_i:
		    if float(row[i])>0.5:
		        l=l+'1'
		    else:
		        l=l+'0'
		 f_s.write(l+"\n")
		 l=""
		 for i in w_i:
		    if float(row[i])>0.5:
		        l=l+'1'
		    else:
		        l=l+'0'
		 f_w.write(l+"\n")
		 l=""
		 for i in k_i:
		    if float(row[i])>0.5:
		        l=l+'1'
		    else:
		        l=l+'0'
		 f_k.write(l+"\n")

         
csvfile.close()
f_s.close()
f_w.close()
f_k.close()

#lable for train:
f_s = open("train_lable_s.txt", "wb")
f_w = open("train_lable_w.txt", "wb")
f_k = open("train_lable_k.txt", "wb")

with open('my_train.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     #r=['s1','s2','s3','s4','s5','w1','w2','w3','w4','k1','k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12','k13','k14','k15']
     s_i=['s1','s2','s3','s4','s5']
     w_i=['w1','w2','w3','w4']
     k_i=['k1','k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12','k13','k14','k15']
     lable=list()
     for row in reader:
		 l=""
		 for i in s_i:
		    if float(row[i])>0.5:
		        l=l+'1'
		    else:
		        l=l+'0'
		 f_s.write(l+"\n")
		 l=""
		 for i in w_i:
		    if float(row[i])>0.5:
		        l=l+'1'
		    else:
		        l=l+'0'
		 f_w.write(l+"\n")
		 l=""
		 for i in k_i:
		    if float(row[i])>0.5:
		        l=l+'1'
		    else:
		        l=l+'0'
		 f_k.write(l+"\n")

         
csvfile.close()
f_s.close()
f_w.close()
f_k.close()
