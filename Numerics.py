#in this file we will learn about variable declaration in python and numeric variables in python
#in python, variables are declared by assigning a value
#python is dynamiclly typed language , meaning that the type of the variable is determind during runtime
#but still it's strongly typed meaning that the variable have a type and it matters when performing operation on the variabel
num1 = 3
num1 = num1 * 3
print(num1) #output is 9

#numbers in python
intNum = 1
print(type(intNum)) #<class 'int'>

floatNum = 1.7
print(type(floatNum)) #<class 'float'>

#operations
additionResult = intNum + floatNum #to find the sum of 2 numbers
print(additionResult) #2.7
print(type(additionResult))#<class 'float'>

intNum = intNum + floatNum
print(intNum) #2.7
print(type(intNum))#<class 'float'>