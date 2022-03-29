num = int(input("enter a number: "))
n = num
i = 2
div = 0
while num > 0:
    if num % i == 0:
        div = 1
        break
    i = i + 1
    num = num - 1
if div == 0:
    print(n, " is Prime Number")
else:
    print(n, " is Not Prime Number")
