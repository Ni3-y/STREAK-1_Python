num = int(input("enter a number: "))
first, last = 0, 1
cnt = 0
for i in range(num):
    print(first)
    sum=first+last
    first=last
    last = sum
