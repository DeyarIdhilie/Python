#defining our own functions
#function has 2 parts: header and body
#header is introduced by the keyword def
#the indented block after : is the code that will be runned after calling the function

'''def function(args):
    code'''

#if the function is supposed to return a value we need to add return at the end of the code

def least_difference(num1, num2, num3):
    diff1= abs(num1-num2)
    diff2= abs(num2-num3)
    diff3= abs(num3-num1)
    return(min(diff1, diff2, diff3))

#how to call the function?
"""print(least_difference())
TypeError: least_difference() missing 3 required positional arguments: 'num1', 'num2', and 'num3'"""
print(least_difference(5,4,8))#1

#how to add an optional argument
def pass_arguments(a, b=None):
    print(a)
    print(b)
    print(type(b))

pass_arguments(4)
'''output
4
None
<class 'NoneType'>'''
pass_arguments(3,2)
'''output
3
2
<class 'int'>'''

#if a function doesn't return anything what will happen if we tried to print the result of calling it
#ex
result = print('hi')
print(result)#None
#note None is what called null in other languages

#Default argument
#how to define an argument with an initial value
#this basiclly means that if the value was passed during function calling the inital value will be used
def greet(who="Colin"):
    print("Hello,",who)

greet()#Hello, Colin
greet('Deyar')#Hello, Deyar
greet(who="Student")#Hello, Student
greet(4)#Hello, 4

#example of a builtin function with a default argument
#print(*args, sep=' ', end='\n', file=None, flush=False)
#sep is the special string that is added between printed arguments
#its default value is single space
print("Hi","guys", "!")#Hi guys !
print(4,5,6,sep='+')#4+5+6