f = open('intro.txt','r')
f1 = open('data','w')
for data in f:
    f1.write(data)