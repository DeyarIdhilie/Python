#some built-in functions
#min
print(min(1,-1,0,10,-33))#-33
print(min(1.1,-2,-44.1,0.0,4.3))#-44.1

#max
print(max(1,-1,0,10,-33))#10
print(max(1.1,-2,-44.1,0.0,4.3))#4.3

#abs
print(abs(3))#3
print(abs(0))#0
print(abs(-3))#3
print(abs(-1.0))#1.0
print(abs(1.0))#1.0
print(abs(2.2))#2.2
"""print(abs('1'))#TypeError: bad operand type for abs(): 'str'"""

#parsing
print(int(1.2))#1
print(float(1))#1.0
i= 5
print(float(i))#5.0
print(int(3))#3
print(int('342'))
print(float('25.3'))
"""print(float('25.3'))#ValueError: invalid literal for int() with base 10: '25.3'"""
print(float('2'))#2.0