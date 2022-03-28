# calculate right to left
a = 0B101
print(a)  # print binary number number
b = 0o123
print(b)  # print octal number
c = 0xfa
print(c)  # print hexadecimal number

# conversion decimal to binary, hex, octal
decimal = 10
print(bin(decimal))
print(oct(decimal))
print(hex(decimal))

a, b, c, d = 0B10, 0o10, 10, 0x10
print(a, b, c, d)

'''
#print ascii value
c=input("enter a character")
print("ASCII value of"+c+"is: ",ord(c))
'''

print(chr(0xaa))  # integer to ascii
print(chr(0xff))
print(chr(200))
print(chr(122))

# bitwise operator

print(10 & 7)
print(10 | 7)
print(~10)  # bitwise not
print(bin(b))
print(13 ^ 7)  # bitwise xor both bit 1 1 or 0 0  return 0
print(10 << 3)  # bitwise left Shift
print(10 >> 2)  # bitwise right shift

print(bin(13))
print(13>>3)
print(bin(1))

if(True):
    print("true")
print("hello")