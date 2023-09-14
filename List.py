#starting with datastructure in python
#List--> ordered sequence of values

listOfIntegers = [2,5,7,3]
listOfStrings = ['Tulkarm','Nablus','Ramallah']

#a list can contain different types, even functions
ListOfObjects = ['hello',4, [1,5,3], True, round]

listOfLists = [
    [1,2,5],
    ['hello','world','!']
]

#how to access element in a list of list
#example !
exlamtion = listOfLists[-1][-1]
print('exlamtion', exlamtion)#exlamtion !

planets = ['pluto', 'venus', 'Mercury']
#since lists are ordered ---> each element could be accessed by index
print(planets[0])#pluto
#index 0 is the start of the list
#if we are moving the right the index will be incremented
#index -1 to access the end of the list
#if we are moving to the left the index will be decreased
print(planets[-1])#Mercury

#Slicing
print(planets[0:2])#['pluto', 'venus']
print(planets[0:3])#['pluto', 'venus', 'Mercury']
#the slice[a:b] will include all the elements from index a to index b-1
#a and b are both optional, if we didn't specify a it will assumed to be 0 and for b it will be assumed to be the length of the list

numbers = [1,5,2,6,0]
print(numbers[:3])#[1, 5, 2]
print(numbers[1:])#[5, 2, 6, 0]
print(numbers[-4:])#[5, 2, 6, 0]#print to the last element
print(numbers[1:-1])#[5, 2, 6]#print all the element expect first and last ones

#lists are mutabel, meaning it could be modified in place
#meaning it could be changed without the need to reference new place in the memory
#you could change an element or slice in a list
numbers[1]=9
'''numbers[5]=4
IndexError: list assignment index out of range'''
numbers[-1]=8
'''numbers[-8]=3
IndexError: list assignment index out of range'''
print(numbers)#[1, 9, 2, 6, 8]
numbers[:5]=[2,4,4,1,7,9]
print(numbers)#[2, 4, 4, 1, 7, 9]
numbers[1:3] = ['2']#note that the slice is 2 element long but the assigment is 1 element so the other element is removed
print(numbers)#[2, '2', 1, 7, 9]

"""print(sorted(numbers))
TypeError: '<' not supported between instances of 'str' and 'int'"""
print(sorted(planets))#['Mercury', 'pluto', 'venus']#alphabatic order
print(planets)#['pluto', 'venus', 'Mercury']
planets.sort()
print(planets)#['Mercury', 'pluto', 'venus']
planets.sort(reverse=True)
print(planets)#['venus', 'pluto', 'Mercury']

#len
print(len(numbers))#5

#sum
numbers[1]=8
print(sum(numbers))#27

#max
print(max(numbers))#9

#how to add new element to the end of a list
#note that append only exist within lists
numbers.append([11,29])
print(numbers)#[2, 8, 1, 7, 9, [11, 29]]

#list.pop --> remove the last element in a list and retreive it
print(planets)#['venus', 'pluto', 'Mercury']
print(planets.pop())#Mercury
print(planets)#['venus', 'pluto']

#search is a list
print(planets.index('venus'))#0
'''planets.index('Mercury')
ValueError: 'Mercury' is not in list'''

#how to check if the variabel exists in the list
print('Mercury' in planets)#False
print('venus' in planets)#True

#how to find all methods that apply on a type
help(planets)

#how to delete all the elements of a list
planets.clear()
print(planets)#[]