#how to iterate in a list
names = ["Deyar","Limar","Islam","Ali","Yousef"]
for name in names:
    print(name,end=' ')#Deyar Limar Islam Ali Yousef

#iterate in a tuple
multplicands = (3,5,1,6,9)
product = 1
for num in multplicands:
    product= num*product
print(product)#810

#iterate in a string
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
for char in s:
    if char.isupper():
        print(char,end='')#HELLO
print('\n')
#range()
#range(n) means integers from 0 to n-1
#range(4) means 0,1,2,3
for i in range(5):
    print(i,end='')
#01234

print('\n')

#while loop
#it will iterate untill the condition is met
i = 0
while i<10:
    print(i, end=' ')
    i+=1
#0 1 2 3 4 5 6 7 8 9

print('\n')

#list comprehension
squares = [n**2 for n in range(10)]#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)

#do the samething without list comprehension
i=0
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#find even number in a list
numbers= [1,2,3,4,5,6,7,8,9,10,11,12]
even_numbers = [number for number in numbers if (number%2 ==0)]
print(even_numbers)#[2, 4, 6, 8, 10, 12]

#multiply even numbers by 10
even_numbers_by_ten = [number*10 for number in numbers if (number%2 == 0)]
print(even_numbers_by_ten)#[20, 40, 60, 80, 100, 120]

#find number of negatives in a list
#first using a for loop
count_negatives = 0
numbers = [1,3,0,0,-1,-5,4,-20]
for number in numbers:
    if number<0:
        count_negatives +=1
print(count_negatives)#3

#using sum and list comprehension
count_negatives= sum([num<0 for num in numbers])#[F,F,F,F,T,T,F,T]#note:the int value of true is 1 and false is 0
print(count_negatives)#3

#using len and list comprehension
count_negatives= len([num for num in numbers if num<0])
print(count_negatives)#3

#find if a given list of numbers is lucky, a lucky list has at least one number divisible by 7


lucky_list = [5,2,51,49,6]
not_lucky_list = [1,3,5]
def is_lucky(numbers):
    # using list comprehension
    print(
        (sum([num % 7 == 0 for num in numbers]))>0
    )
    print(
        (len([num for num in numbers if num%7==0]))>0
    )
    # using for loop
    for num in numbers:
        if num%7 ==0:
            return True
    return False
print(is_lucky(lucky_list), is_lucky(not_lucky_list))
'''True
True
False
False
True False'''

#using list comprehension and any
help(any)
'''any(iterable, /)
    Return True if bool(x) is True for any x in the iterable.
    
    If the iterable is empty, return False.'''
def is_lucky_using_any(numbers):
    return(any([num%7 == 0 for num in numbers]))
print(is_lucky_using_any(lucky_list), is_lucky_using_any(not_lucky_list))#True False

#python panda and numpy compare each element in the list to number(element-wise comparison)
#let's implement that behavior
#it should return a list of true or false, true if the element is greater than the number, false otherwise

def element_wise_comparison_greater_than_loop(theList, number):
    comparison_result = []
    for element in theList:
            comparison_result.append(element>number)
    return comparison_result
print(element_wise_comparison_greater_than_loop([1, 2, 3, 4], 2))#[False, False, True, True]

def element_wise_comparison_greater_than_list_comprehension(theList, number):
    return([element > number for element in theList])

print(element_wise_comparison_greater_than_list_comprehension([1, 2, 3, 4], 2))

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
#note range(0) and range(-1) are both = zero so if the length is 1 or 0 the loop will not be entered and the value will be False
        