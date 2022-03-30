#n=int(input("enter a number..."))
'''
s={1,2,3}
print(type(s))
s={'a','b',3}
print(type(s))
s={}
print(type(s))
s=set()
print(type(s))

#s={[1,2],'a','b'}#list in only the immutable data type

s={(1,2),'a','b'}
print(type(s))
s={{1,2},1.3}
print(type(s))

'''
'''
s={5,5,12,5,6,1,9,8,9}
print(s)

for n in s:
    print(n)
'''
'''
#remove duplicate elements in list
l=[10,20,35,60,40,10,25,20]
print(l)
s=set(l)
print(s)
l=list(s)
print(l)
'''
'''
#remove duplicate elements in tuple
t=(10,20,35,69,20,10,'a','b','a')
print(t)
s=set(t)
print(s)
t=tuple(s)
print(t)

'''
'''
#print(s[2])#type error because set is unordered

s.add(5)#add only one elements in set
print(s)
s.add([4,'a'])#error
print(s)
s.add((4,'a'))#add tupple is immutable
print(s)
'''
'''
#add()add only one elements
#update() we can pass multiple elements
s={10,20,30,10,20,'a','b','a'}
s.update('b')#add it
s.update(['x','zd'])#add multiple elements
print(s)
s.update(['c','d'],['x','y','z'])
print(s)
s.update(['c','d'],['x','y','z'],('t','u'))
print(s)
'''
'''
s1={10,203,30}
s2={20,68,90,}
s3=s1+s2
#print(s3)#concatination and replication is not allowed in te set

s4=s1*3
#print(s4) replication is not allowed in te set

'''
'''
#add the list data in the set
#1
l=[10,5,2,'a',10,'b',2]
s=set()
for n in l:
    s.add(n)
print(s)

#2
l=[10,5,2,'a',10,'b',2]
s1=set()
s1.update([10,5,2,'a',10,'b',2])
print(s1)

'''

'''
#discard() remove the data in the set if the elements not available in the set discard() does not return the error

s={10,8,9,6,4,10}
print(s)
s.discard(4)
print(s)

s.discard('z')
print(s)

s.remove(10)#if the elements not available in the set remove() return the error
print(s)
s.remove(100)
#print(s)

'''

'''
#remove the 'hallo' data from the set
#delete 'welcome' data from the set
s={7,'a','hello','haii'}
s.discard('hello')
print(s)
s.discard('welcome')
print(s)

#pop() method it pop randomely any element in the set

s={10,100,1000,'a','b','v','25',25}
a=s.pop()
s.clear()   #delete all elements in the set
print(a)
print(s)
'''
'''
#print s1 in all string and s2 all integer
s={10,100,1000,'a','b','v','as',25}
s1=set()
s2=set()
for n in s:
    if type(n)==int:
        s1.add(n)
    else:
        s2.add(n)

print(s1)
print(s2)

'''
'''
s1={10,20,30,40}
s2={50,60,70,80}
s3=s1
s4={10,20,30,40}
print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))

print(s1==s2)
print(s4!=s1)
print(s3==s1)
print(s1 is s2)
print(s4 is not s2)
print(s3 is not s1)
print(10 in s3)
print(109 in s1)
print(40 in s2)
print(40 not in s2)

'''
'''
a={'d',6,'y'}
b={10,20,6,'d','f','g','y'}
print(a.issubset(b))
print(b.issubset(a))
print(b.issuperset(a))
print(a.issuperset(b))

'''
'''
basket1={'orange','apple','pear','banana'}
basket2={'pear','orange','banana'}
print(basket1-basket2)#set difference  #letters in basket 2 but not in basket 2
print(basket2-basket1)

print(basket1 | basket2)#letters in basket 1 or basket 2 or both

print(basket1 & basket2)##letters in both basket 1 and basket 2 # intersection

print(basket1 ^ basket2)#letters in basket 1 or basket 2 but not both #^symmentric difference

'''

a={1,2,3,4}
b={5,6,7}
print('are a and b disjoint? ',a.isdisjoint(b))#disjoint it returns true if two sets are disjoint set  if not return false

print(a.difference(b))#this method returns return difference of the both set
print(b.difference(a))

result=a.difference_update(b)
print(result)
a={10,20,30}
b={10,20,30}
r2=a.difference_update(b)
print(r2)

A={'a','b','c','d'}
B={'c','f','g'}
result1=A.difference_update(B)
print(result1)