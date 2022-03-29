n=input("enter string")
s="pune"
a=""
p=0
for i in range(0,len(n)):
    if s[0]==n[i]:
        j=0
        for j in range(0,len(s)):
            if s[j]==n[i+j]:
                a+=n[i+j]
    if(a=="pune"):
        break
print(a)