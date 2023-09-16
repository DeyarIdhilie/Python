#enumerate is a built_in function
#used to keep count of the iterations while dealing with iterators
#syntax: enumerate(iteratabel, start=)
#iteratable --> any object that support iteration such as lists, strings
#start--> the index value from which the counter will be started by defalut it is 0
#return is an iterator with index and element pairs

list1 = ['hello', 'world', '!']
obj1 = enumerate(list1)
print(type(obj1))#<enumerate object at 0x000001CFC4EBFDD0>
print(obj1)#<enumerate object at 0x000001CFC4EBFDD0>
print(list(obj1))#[(0, 'hello'), (1, 'world'), (2, '!')]
print(list(enumerate(list1, 2)))#[(2, 'hello'), (3, 'world'), (4, '!')]


#enumerate and loops

#return each pair
for pair in enumerate(list1):
    print(pair)
'''(0, 'hello')
(1, 'world')
(2, '!')'''

#return index and element seperately
for index, element in enumerate(list1):
    print(index, element)
'''0 hello
1 world
2 !'''


