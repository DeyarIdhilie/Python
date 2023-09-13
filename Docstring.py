#help on functions that are not builtin
'''help(least_difference)
Help on function least_difference in module __main__:
least_difference(num1, num2, num3)'''
#note that there is no automated description generated
#how to create a description that will be provided when help is called
#when i write a function, i can provide a description --> docstring

def least_difference(num1, num2, num3):
    """Return the smallest difference between any two numbers
       among num1, num2, and num3"""
    diff1= abs(num1-num2)
    diff2= abs(num2-num3)
    diff3= abs(num3-num1)
    return(min(diff1, diff2, diff3))

help(least_difference)
'''Help on function least_difference in module __main__:
least_difference(num1, num2, num3)
    Return the smallest difference between any two numbers
    among num1, num2, and num3
'''
