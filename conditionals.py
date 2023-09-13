#booleans are often combined with conditional statements(if-then statements)
#this is usually done using keywords like if,elif,else
#they let u control what pieces of code are run based on the value of some boolean condition

def inspect(num):

    if isinstance(num,int):
        if (num == 0):
            print('zero')
        elif (num > 0):
            print("{} is positive".format(num))
        elif (num < 0):
            print("%d is negative" % num)
    else:
        print("{} is hmmm...".format(num))
        print("%s is hmm..." % num)
        print(f"{num} is not a degit")

inspect(0)#zero
inspect(11)#11 is positive
inspect(-19)#-19 is negative
inspect("string")
'''string is hmmm...
string is hmm...
string is not a degit'''

#identation is so important
def f(x):
    if x>0:
        print('this will be printed when x is postive')
    print('this will be printed whenever the function is called',x)

f(0)
f(1)
f(-1)
'''
this will be printed whenever the function is called 0
this will be printed when x is postive
this will be printed whenever the function is called 1
this will be printed whenever the function is called -1
'''


#let's talk about boolean conversion
'''
in numbers, any nubmer is True unless it's Zero
in Strings/sequences, they are True unless empty
'''
if 0:
    print("shine")
if 2.0:
    print("spark")
if "":
    print("sprinkle")
if " ":
    print("shshsh")
'''    
>>>
spark
shshsh
'''
print(bool(1))#True
print(bool(0))#False
print(bool(""))#False
print(bool(" "))#True
print(bool("spam"))#True