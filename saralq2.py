f = open('saral_q1.txt','r')
f1 = f.read()
i = 0
count = 1
while i < len(f1):
    if f1[i] == '\n':
        count+=1
    i+=1
print(count)
