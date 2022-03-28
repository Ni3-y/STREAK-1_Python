# To find the correct string from specified string
n="haii A AAA Aitin hou pune are you"
cnt=0
for i in (n):
    if i=='A':
        cnt+=1
print(cnt)
a=""
main = "this is an example example"
sub = "example"
count = 0
done = False
for i in range (0,len(main)):
   match = True
   if sub[0]==main[i]:
     j=0
     for j in range(0,len(sub)):
         if sub[j]!=main[i+j]:
             match = False
             print("No substring")
             break
         else:
             count=count+1
             a+=main[i+j]
             if match == True and count == len(sub):
                 print("Substring")
                 print("Position start:",i)
                 done = True
                 break
   if done == True:
     break

print("aaaa",a)