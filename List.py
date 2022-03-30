'''
l = ['a', 10, 25]
print(l)
l.insert(0, 'hello')
print(l)
l.insert(6, 'j')
print(l)
l2=[10,20,30,45]
print(l+l2)

print(l2*3)

l3=l2.copy() #in copy data is same but the location is different
print(l3)

print(id(l2))
print(id(l3))

l.extend(l2)
print(l)
'''
'''
l1 = ['a', 10, 25]
l2 = [10, 20, 30, 58, 'hello']

animal = ['cat', 'dog']
animal[1] = 'cow'
print(animal)

animal[1:3] = ['tiger', 'lion', 'bat']
print(animal)
'''
'''
animal[2:5] ='ant'
print(animal)
'''
'''
animal[3:6]=['ant']
print(animal)
animal[2:5]='10'
print(animal)
'''
'''
animal = ['cat', 'dog']
print(animal.index('cat'))
#print(animal.index('tiger'))#value error
animal.reverse()
print(animal)

fruit=['apple','mango','orange','apple','orange']
print(fruit.count('apple'))
print(fruit.count('orange'))

fruit.sort()#ascending order sorting
print(fruit)

fruit.reverse()#descending order
print(fruit)
'''
'''
fruit=['apple','mango','orange','apple','orange']
a=fruit.remove('apple')#it remove data permanently
print(fruit)
print(a)

a=fruit.pop()
print(a)
a=fruit.pop()
print(a)
a=fruit.pop(0)
print(a)
#a=fruit.pop(3)
#print(a)
#a=fruit.pop(10)#index erro
#print(a)

l=[5,6,10,0,15,12,18]
#to print the addition of only even numbers from list
sum=0
for i in l:
    if i%2==0:
        sum+=i
print(sum)

#print only vowels from given list
l2=['u','a','f','s','i','h']
l3=[]
for n in l2:
    if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
        print(n,end=' ')
        l3.append(n)
print()
print(l3)
'''
'''
l=[1,2,3,4,5,6,7,8,9]
#l.del[2]
del l[2]
print(l)
del l[3:6]
print(l)
del l[:] # l.clear() both function delete all the elements in the list
print(l)

l=['vijay']*2
print(l)

l=[['vijay']*2]
print(l)

l=[['vijay']*2]*3
print(l)
'''

# print the output
# GOOD good 4
# EVENING evening 7

s = 'Good evening How are you'
word = s.split()
print(word)
for i in word:
    a = i.upper()
    b = i.lower()
    c = len(i)
    print(a, b, c)

print("***************************")
x = [[i.upper(), i.lower(), len(i)] for i in word]
print(x)

# to get the largest number from the list
# to get the smallest number from the list

n = [10, 20, 30, 40, 50, 23, 56, 100]

j=n[0]

for i in n:
    if i>j:
        j=i
print("Largest Number: ",j)

n = [10, 20, 30, 40, 50, 23, 56, 100]

j=n[0]
for i in n:
    if i<j:
        j=i
print("Smallest Number: ",j)

an=['a','b','v']
an[2:5]='at'
print(an)

l123=[10,20,30,40]
print(max(l123))śś