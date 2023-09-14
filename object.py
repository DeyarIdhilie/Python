#everything in python is an object
#an object carry some things around with it and u access that thing using dot
x = 12 #number#a real number so it has an imaginary part
print(x.imag)#0
y = 12 + 3j# it's a complex number
print(y.imag)#3.0

'''the things an object can carry aroud include funcions
a function attached to an object is called a method
but non-function things that are attached to an object is attribute
to access a method u only need the dot syntax .method,but to actally call it method()'''
z = 5
print(z.bit_length())#3
z = 9
print(z.bit_length())#4
#error
"""z = 'hello'
print(z.bit_length())
AttributeError: 'str' object has no attribute 'bit_length'"""

