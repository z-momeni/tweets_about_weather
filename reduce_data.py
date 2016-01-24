f=open('my_train.csv','w')
g=open('my_test.csv','w')

h=open('train.csv','r')
i=0
for line in h.readlines():
    if i==0:
        f.write(line)
        k=line.split(',')
        g.write(line)
    elif i>0:
        if i%2==0:
            f.write(line)
        else:
            k=line.split(',')
            g.write(line)
    i+=1

f.close()
g.close()
h.close()
