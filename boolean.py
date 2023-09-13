#how to declare a boolean variabel
x = True
y = False
print(x)#True
print(type(x))#<class 'bool'>
print(y)#False
print(type(y))#<class 'bool'>

'''comparison operations
a==b is equal?
a!=b is not equal?
a>b is a greater than b?
a>=b is a greater or equal to b?
a<b is a less than b?
a<=b is a less or equal to b?'''
#note: == is used for comparison, = is used to assign value

#are u a child?
def is_a_child(age):
    return age<18
print('is a 19 year old a child?', is_a_child(19))#is a 19 year old a child? False

#comparison between different types
print(3.0 == 3)#True
print('3' == 3)#False

#is the number odd?
def is_the_number_odd(num):
    return num%2 == 1
def is_the_number_even(num):
    return num%2 == 0
print(is_the_number_odd(5),
      is_the_number_even(5),
      is_the_number_even(4),
      is_the_number_odd(4),
      sep='\n')
'''True
False
True
False'''

#how to combine boolean values? using and, or, not

'''
a | b | a and b
T | T | T
T | F | F
F | T | F
F | F | F
'''
'''
a | b | a or b
T | T | T
T | F | T
F | T | T
F | F | F
'''
'''
a | not a 
T | F 
F | T 
'''

print(True or True and False)#True
#https://docs.python.org/3/reference/expressions.html#operator-precedence
# so not is evaluated before and and and is evaluated before or

''' 
The problem
prepared_for_weather = have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

I'm trying to say that I'm safe from today's weather:
if I have an umbrella...
or if the rain isn't too heavy and I have a hood...
otherwise, I'm still fine unless it's raining and it's a workday
solution
prepared_for_weather = have_umbrella 
                       or (rain_level < 5 and have_hood) 
                       or (not (rain_level > 0 and is_workday))
'''