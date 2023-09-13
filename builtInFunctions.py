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

#round(number, decimalDigits)
#the first argumant is requried, but the second is optional
#the second argument is optional bc it's by default a zero
'''round()#TypeError: round() missing required argument 'number' (pos 1)'''
print(round(1.55))#2
x= round(1.2245)#1
print(x)#1
print(type(x))#<class 'int'>
y= round(x,2)
print(y)#1
z= round(1.52557,3)#1.526
print(z)
print(type(z))#<class 'float'>

#note: banker's rounding, which means when the decimal is .5, you either round up or down so that the result is always even
print(round(2.5))#2
print(round(51.5))#52
print(round(-51.5))#-52
print(round(-2.5))#-2

#if the second argument is positive the round function works on the decimal digigts
#but if it's negative, it works on the integer part
print(round(171.573653,-2))#-2 means to the nearest hundred #200
print(round(5463, -2))#5500
print(round(5465,-1))#to the nearest ten#also note when half round to the nearest even
#print(round(2.35, .5))#TypeError: 'float' object cannot be interpreted as an integer
print(round(2.35, int(.5)))#2.0

#help function
help(abs)
'''abs(x, /)
    Return the absolute value of the argument.'''
#help() display 2 things ,first the function header and the argunments it takes&&a description of what it does
#we only need to send the function name
#in progarmming it's known that func() is a way of calling the function, so if we say help(func()) the func will be called before the help
'''help(round())
TypeError: round() missing required argument 'number' (pos 1)'''
help(round(2.1))#what happens right here is that the help will be on integers, since the value of the expression will be calculated then the help will be called
