'''
result = float(input("enter percentage"))
if(result >= 70):
    print("A+")
elif(result>=60):
    print("B+")
else:
    print("Fail")
print("done!")

if(result%2==0):
    print(result," is even")
else:
    print(result," is odd")

if 0:
    print("true")
else:
    print("false")
'''

a=5
if(a>0):
    print("Positive")
else:
    print("Negative")
print("------------")

print("positive" if a>0 else "Negative") #if else single line

b=0
print("positive" if b>0 else "Zero" if(b==0) else "Negative")

