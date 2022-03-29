num=int(input("enter a number: "))
div=False
for i in range(2,num):
    if num%i==0:
        div=True
        break
if div==False:
    print(num," Is Prime Number")
else:
    print(num," Is Not Prime Number")