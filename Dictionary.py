'''
    DICTIONARY
d={1:12345,'a':'hello'}
print(type(d))
print(d)
print(d['a'])
print(d[1])

d={1:[1,2,3,4,5],'a':'welcome'}
print(d[1])

d={1:(1,2,3,4,5),'a':'welcome'}
print(d[1])

d={1:{1,2,3,4,5},'a':'welcome'}
print(d[1])


#d={[1,2,3,4]:'hell','a':'welcome'}#list in key are not allowed

#d={{1,2,3,4}:'hell','a':'welcome'}

d={(1,2,3,4):'hell','a':'welcome'} #in dictionary only mutable data type are allowed ex.String, Number, Tuple
print(d)
d=dict()
print(type(d))
d={}
print(type(d))

d={1:'haii','a':5678,(1,2,3):'welcome'}
#for n in d:
#    print(n)

for n in d:
    print(n,d[n])
'''
'''
phonebook={}
print(phonebook)
phonebook['nitin']=7754402932
phonebook['abhijit']=5979802932
phonebook['balaji']=7967596174

print(phonebook)

phonebook1={'balaji':6896608080,'ram':259}
print(phonebook1)

print(id(phonebook))
print(id(phonebook1))

print(id(phonebook['balaji']))
print(id(phonebook1['balaji']))#in dictionary both key are same but memory location diff

friends={'ram':123456,'sham':7896554}
print(friends['ram'])
print(friends['sham'])
#print(friends['adb'])#error

print(friends.get('sham'))
print(friends.get('ram'))
print(friends.get('Abc'))#None Abc is not available in friends
'''
'''

d2={1:'nitin',12:'abhijit',3:'balaji',5:'ram'}
print(d2.keys())
print(d2.values())

a=d2.keys()
print(type(a))#type= dictionary key

#list
b=list(d2.keys())
print(b)
print(type(b)) #type list

print(list(d2.values()))

#tuple
t=tuple(d2.keys())
print(type(t))
print(tuple(d2.keys()))
print(tuple(d2.values()))

#set

s=set(d2.keys())
print(type(s))
print(set(d2.keys()))

#sorted the data in dictionary

print(sorted(d2.keys()))
print(sorted(d2.values()))
'''
'''
d1={1:123,2:256,3:4569,4:89}
print(d1.items())

for k,v in d1.items():
    print(k,v)

del d1[2]
print(d1)

n=d1.pop(1)
print(n)

d2={}
#d2.popitem() error
d2.clear()

d={1:'ram',2:'nitin'}
print(id(d))
d1={3:'balaji',4:'abhijit',1:'sham'}
d.update(d1)
print(id(d))
print(d)

x={*d,*d1}
print(x) #print only keys

x={**d,**d1}
print(x)    #print both key and values

d2={1:113,2:2365,3:322,4:23}
print(id(d2))
d3=d2.copy()
print(d3)
print(id(d3))

print(len(d2))
print(len(d2.keys()))
print(len(d2.values()))

d5={1:'',2:'12',3:" "}
print(d5)

'''

'''
#converting list into dictionary using zip() method
l1=[10,20,30,40]
l2=['nitin','ram','balaji','abhijt']
x=zip(l1,l2)
print(x)
d=dict(x)
print(d) #{10: 'nitin', 20: 'ram', 30: 'balaji', 40: 'abhijt'}

'''
'''
l1=[10,20,30,40,10]
l2=['nitin','ram','balaji','abhijt','xyz']
x=zip(l1,l2)
print(x)
d=dict(x)
print(d)
'''
'''

#converting tuple into dictionary
l1=(10,20,30,40)
l2=('nitin','ram','balaji','abhijt')
x=zip(l1,l2)
print(x)
d=dict(x)
print(d) #{10: 'nitin', 20: 'ram', 30: 'balaji', 40: 'abhijt'}

#converting set into dictionary
l1={10,20,30,40}
l2={'nitin','ram','balaji','abhijt'}
x=zip(l1,l2)
print(x)
d=dict(x)
print(d) #{10: 'nitin', 20: 'ram', 30: 'balaji', 40: 'abhijt'}
'''
#print dictionary using d1 and d2 but key is d1 and value is d2 value
d1={1:'a',2:'u'}
d2={'a':123,'b':456}
d1=list(d1.keys())
d2=list(d2.values())
x=zip(d1,d2)
print(dict(x))  #{1: 123, 2: 456}

#print dictionary keys are different but values are same
l1=['a','b','c','d','e']
d=dict.fromkeys(l1,10)
print(d)# {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}

#print dictionary using list
l2=[(1,'a'),(2,'b'),(3,'c'),(4,'d')]
print(dict(l2))  #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}