#how to defind a tuple
t = (1,5,4)
print(type(t))#<class 'tuple'>
t2 = 1,5,3
print(type(t2))#<class 'tuple'>

#tuple are immutabel, meaning it can't be modified
'''t[1] = 6
TypeError: 'tuple' object does not support item assignment'''

#but it's ordered
print(t[1])#5

#when to use tuple, if the function return more than value
def multi_value_return():
    return "hello","people"
print(multi_value_return())#('hello', 'people')
value1,value2 = multi_value_return()
print(value1,value2)#hello people

#example on a builtin fnction that return multivalue
x=0.125
print(x.as_integer_ratio())#(1, 8)
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator, numerator/denominator, sep=',')#1,8,0.125

#swapping 2 variable using tuple
a=19
b=92
a,b = b,a
print('a=',a,'b=',b)#a= 92 b= 19


