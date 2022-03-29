num = int(input("enter a number: "))
first, last = 0, 1
count = 0
if num < 0:
    print("please enter positive integer")
else:
    while count < num:
        print(first)
        sum = first + last
        first = last
        last = sum
        count += 1
