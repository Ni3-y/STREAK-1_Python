n="haii hello how are you...!"
temp=''
l1=[]
p=n.strip()
#print(p)
for i in p:
    if(i==' '):
        l1.append(temp)
        temp=''
    else:
        temp+=i

l1.append(temp)
print(l1)