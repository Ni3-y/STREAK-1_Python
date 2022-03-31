'''
# normal function
def add(a, b):
    print(a + b)


add(10, 20)

# lambda function
f = lambda a, b: a + b
print(f(10, 20))

b = lambda x, y: x if x > y else y
print(b(20, 10))

# check nummber is positive or negative using lambda function
c = lambda a: 'Positive' if a > 0 else 'Negative'
print(c(-10))

# check nummber is positive or negative or zero using lambda function
c = lambda a: 'Positive' if a > 0 else 'negative' if a < 0 else 'zero'
print(c(0))

# filter() method
# print even number upto 10 using filter
print(list(filter(lambda x: x % 2 == 0, range(10))))

l = [10, 20, 55, 65, 87, 99, 12, 11]
print(list(filter(lambda n: n % 2 != 0, l)))

l = [10, 20, 55, 65, 87, 99, 12, 11]
print(tuple(filter(lambda n: n % 2 != 0, l)))

l = [10, 20, 55, 65, 87, 99, 12, 11]
print(set(filter(lambda n: n % 2 != 0, l)))

n = 'Nitin'
print(list(filter(lambda a: a == 'i' or a == 't', n)))

# map method

print(list(map(lambda n: 2 * n, range(10))))
'''
import math

'''
#get all modules
print(help('modules'))

import math
print(dir(math))

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb',
 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 
 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan',
  'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

'''
'''
import math
print(math.sqrt(4))
print(math.factorial(5))
print(math.pow(4,2))
print(math.pi)
'''
'''
import math as mt
print(mt.sqrt(4))
print(mt.pow(2,2))
'''
'''
from math import pi #import only pi
from math import sqrt,pow
print(pi)
print(sqrt(5))
print(math.factorial(5))
'''

#create user define moule

''' 1
import firstUserDefineModule as fm
fm.add(10,20)
fm.multiply(10,2)

print(fm.name)

'''
#2
from firstUserDefineModule import add,name
add(20,20)
print(name)


str="nitin"

print(list(map(lambda n:n,str)))
print(tuple(map(lambda n:n,str)))
print(set(map(lambda n:n,str)))