'''
t=()
t1=tuple()
print(id(t))
print(id(t1))

t=(1,2,3)
t1=(4,5,6)
print(id(t))
print(id(t1))

t=(5,6,7)
t1=(15,10,5)
print(id(t[0]))
print(id(t1[2]))

a,b,c=t
print(a)
print(b)
print(c)
'''
# a,b=t Error because in t have a 3 variable

'''
t2=(10)
print(type(t2)) #data type int

t2=(10,)
print(type(t2)) #data type tuple

#nested tuple

t=((10,20),(30,40))
print(t[1])
print(t[1][1])

t1=(10,20,'pne',True)

for i in t1:
    print(i)

t1=('pne')#check t1=('pune',)
for i in t1:
    print(i)

#conversion tuple to List
t=(10,20,30)
l=list(t)
print(l)
print(type(l))

#conversion List to Tuple
t=tuple(l)
print(t)
print(type(t))
'''

'''
t=(100,'pune',(50,60),'hello')
print(t[0])
print(t[-3]) #pune
print(t[2][-1]) #60

print(t[:])

# print(t[10]) #Index Error because 10 index is not available

print(t[-3:])

#iterate the date
t=((10,20),(30,40))
for x,y in t:
    print(x,y)

'''
'''
#print the sum of odd number
t3=(35,72,65,33,35,72)
sum=0
for n in t3:
    if n%2==1:
        sum+=n
print("Sum of odd number's: ", sum)

x=[n for n in range(10)] #add multiple element sequence wise in list
print(x)


x=tuple(n for n in range(10)) #add multiple element sequence wise in the tuple
print(x)

'''
'''
t=('a','pune',100,20)
# t[1]='welcome' type erro because tuple is imutable
print(t)

t1=(10,20,30,40)
t2=(50,60,70,80)
t3=t1
t4=(10,20,30,40)
print(t1==t3) #True
print(t2==t4) #False
print(t1==t4) #True
print(t4==t3) #True
print(t1 is t2) #identity operator is & is not is used to check memory address comparison
                #membership operator is used to cheak data comparison
print(t1>t2)
'''
'''
t1=(10,20,'a')
t2=('a','b','c')
t3=t1+t2
print(t3)

print(t1[2])
print(t3[2])

print(id(t1[2]))
print(id(t3[2]))

t1=t1+t2
print(t1)
print(id(t1)) # it destroy first t1 and create new tuple t1 with t2

print(t1*3)#replication print  same t1 3 times

'''
'''

t=(35,73,80)
#to add the following data in tuple ('a','hello','haii')
#1
l=list(t)
l.append('a')
l.append('hello')
l.append('haii')
t=tuple(l)
print(t)
print(type(t))

#2
t2=(40,52,30)
t3=('a','hello','haii')
t1=t2+t3
print(t1)

'''
'''
t=(10,10,70,30,10,50)
print(t.count(10))
print(len(t))
print(t.index(10))
print(t.index(10,2))
#              value, start, end Value find return it index otherwise throw Value error
print(t.index(50,5,9))

#sort() it use in list
#sorted() it use in tuple

print(t)
print(sorted(t))
print(sorted(t,reverse=True))

#t=('a',10,'x',100,True)
#print(max(t))
#print(min(t))
#print(sorted(t))#Type error because data is not homogeneous

print(max(t))
print(min(t))
'''
'''
t=((20,40),('hello',10),(100,'haii'))
#print(t1)
t1=()
l=list(t1)
j=0
l2=[]
for i in t:
    j=0
    for n in i:

        if j==1:
            l.append(n)
        else:
            l2.append(n)
        j=1
#print(l)
t2=tuple(l)
t1=tuple(l2)
print(t2)
print(t1)

t=((20,40),('hello',10),(100,'haii'))
t1=[]
t2=[]
for x,y in t:
    t1.append(x)
    t2.append(y)
print(t1)
print(t2)
'''

t1=(10,20,35,68,50,90)
print(t1)
t2=()
for n in reversed(t1):
    t2=t2+(n, )

print(t2)

t3=(10,20,33)
print('this is a tuple {0}'.format(t3))