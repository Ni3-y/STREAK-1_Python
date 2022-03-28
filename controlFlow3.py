# do while loop & switch statement is not present in python
# while loop
'''
i = 1
while (i < 10):
    print(i)
    i = i + 1; '''

'''
digit=0
num=int(input("enter a number: "))
while num !=0:
    num=num//10;
    print("num: ",num)
    digit=digit+1
print("Total digit is: ",digit)
'''

'''
# GCD
a = int(input("enter first number: "))
b = int(input("enter second number: "))
while a != b:
    if a > b:
        a = a - b  # a-=b
    else:
        b = b - a  # b-=a
print("GCD", a)
'''

'''
l1=[1,2,3,4,5,2,3,8]
for n in l1:
    print(n,end=" ") #end is used to print data in single line

for n in range(10):
    print(n,end=" ")
print()

for n in range(2,10):
    print(n,end=" ")
print()

for n in range(2,20+1,2):
    print(n,end=" ")

'''

'''
for n in range(3,50): # or for n in range(3,50,2) print(n) #it print all odd number upto 50
    if(n%2==1):
        print(n,end=" ")
print()
for n in range(3,50):
    if(n%2==0):
        print(n,end=" ")
'''

'''
#Print Prime Number
f=False
n=int(input("enter a number: "))
for i in range(2,n):
    if(n%i==0):
        f=True
if(f==False):
    print("prime number")
else:
    print("not prime number")
#print("prime" )

'''

'''
#Break stetment
for i in range(10):
    if(i==4):
        break
    print(i)

for n in "welcome":
    if n=='e':
        break
    print(n)

for i in 'Welcome':
    if((i=='o') or (i=='e')):
        break
    print(i)

s={10,20,30,45,25}
for i in(s):
    print(i)
'''
'''
#Continue

for n in range(10):
    if(n==5):
        continue
    print(n,end=" ")
'''

'''
#1
for i in range(10):
    print(i)
else:
    print("else block")

#2
for i in range(10):
    if(i==4):
        break
    print(i)
else:
    print("else block")
'''
#3
'''
for i in range(10):
    print(10/0)
    print(i)
else:
    print("else block")
'''
'''
import os
for i in range(10):
    print(i)
    os._exit(0)
else:
    print("else block")
print("done")
'''
'''
import os
n=10
while n>1:
    print(n)
    n-=1
else:
    print("else block")
'''
'''
l1=[10,20,30,54,69]
for n in range(10):
    print(n)
else:
    print("else block")'''

n=11
div=0
for i in range(2,n):
    if(n%i==0):
        div=1
        break
if(div==0):
    print("prime")
else:
    print("not prime")
