'''there are for argument type
    1. Default Argument
#when we call the function if we are not passing any arguments the default value is assigned

def emp(id=101, name="abc", sal=15325):
    print("Id: ",id,end=" ")
    print("Name: ",name,end=" ")
    print("Salary: ",sal,end=" ")
    print()
emp()
emp(104)
emp(102,"Nitin")
emp(103,"Nitin",15362)

'''
#2 Required Argument
'''
#3 Keyword/Named argument
def empd(name,role):
    print("Name: ",name," role: ",role)
empd(name="abc", role="efg")
empd(role="xyz",name="qwe")
'''
'''
#4 variable number of arguments
def varlength(*vararg):
    pass
varlength(102,20,30,45)
'''
'''
#none keyword
#1
def add(a):
    if a%2==0:
        return True
x=add(5)
print(x)

#2
def add(a):
    if a%2==0:
        return True
    return False
x=add(5)
print(x)

#3
def ad():
    c=20+5
a=ad()
print(a)
'''

'''
a="Nitin Yewale"
print(a[4:9])
print(a[-10:-1])
print(a[-10:])
print(a[5:])
print(a[4])
'''
'''
b="haii hello bye!..."
print(b[5])
print(b[:])
print(b[2:2])
print(b[-11:-5])
print(len(b))
'''
'''
#String Operations
c=" hello "
print(len(c))#7
print(len(c.strip()))#len=5 strip() method is used to remove the white sapces leading and trailing

c="@@@@^^^ni3%%%%%"
print(c)
print(c.lstrip('@')) # lstrip() is used to remove left side white spaces
print(c.rstrip('%'))
print(c.rstrip('%').lstrip("@"))
print(c.lstrip('@').lstrip('^').rstrip('%'))
'''
'''
a="Hello"
b="hello"
print(a[1] is not b[1])
print(id(a[1]))
print(id(b[1]))
print(id(a))
print(id(b))
print(a[1]>b[4])
'''

# To find the correct string from specified string
# count 'A' charecter from given string(without count function)