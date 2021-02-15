
f = open('saral_q4.txt','r')
f1 = f.read()
list1 = f1.split('\n')
print(list1)
i = 0
while i < len(list1):
    if "delhi" in list1[i]:
        d= open("delhi.txt",'a')
        d.write(list1[i])
        d.write('\n')
    elif "shimla" in list1[i]:
        s = open("shimla.txt",'a')
        s.write(list1[i])
        s.write('\n')
    else:
        o = open("others.txt",'a')
        o.write(list1[i])
        o.write('\n')
    i+=1
d.close()
s.close()
o.close()
f.close()

