#there are standard library, that can be found anywhere
#you access this code using import
import math
#we could name the imported module as short alias to ease dealing with
import numpy as np
#or
import pandas
pd = pandas

print(type(math))#<class 'module'>
#a module is a collection of variabels(namespace) defined by someone else

#to see all the names in math
print(dir(math))#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

#some could be variabels such
print(math.pi)#3.141592653589793
#note that we needed to use math to access pi
#from math import * would make all the modules's variabel directly accessibel without any dotted prefix


#some could be functions
print(math.log(32,2))#5.0
help(math.log)
'''Help on built-in function log in module math:
log(...)
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base not specified, returns the natural logarithm (base e) of x.
'''

#help on modules
help(math)


