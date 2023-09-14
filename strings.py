#strings could be declared by either single quotes or doubel, there both are the same#string is a sequence of characters
s1= 'string'
s2= "string"
print(s1==s2)#True
s1=2
s2='2'
print(s1==s2)#False
s1= 'String'
s2= "string"
print(s1==s2)#False

#when to double and when to single
s1 = 'hello "genius"'
print(s1)##hello "genius"
s2 = "hello 'gorg'"
print(s2)#hello 'gorg'

#what to do if i want to use single quotes even if the string has single quote
#and double when it has doulbe quote
print('hello \' Honey')#hello ' Honey
print("hello\" 3ini")#hello" 3ini

#how to add line in string
print("hello world!\nIt's me")
print('''hello world!
It's me''')
"""
>>>
hello world!
It's me
hello world!
It's me"""
print("hello world!\nIt's me" == '''hello world!
It's me''')#True

print("hello\\")#hello\
#strings are immutabel, cannot be mutated or changed
#individual characters within a string cannot be reassigned
