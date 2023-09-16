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


s1='hello'
print(s1[0])#h #indexing
print(s1[0:2])#he #slicing
print(s1[-3:])#llo

#strings are immutabel, cannot be mutated or changed
#individual characters within a string cannot be reassigned
"""s1[0]='j'
TypeError: 'str' object does not support item assignment"""
"""s1.append('!')
AttributeError: 'str' object has no attribute 'append'"""

#find string length
print(len(s1))#5

#how to split the string to characters
print([char for char in s1])#['h', 'e', 'l', 'l', 'o']
#edit each character in the string
print([char+'!' for char in s1])#['h!', 'e!', 'l!', 'l!', 'o!']

#to all caps and all lowers
s= 'hi people I am  me'
print(s.upper())#HI PEOPLE I AM ME
print(s.lower())#hi people i am me

#seaching
print(s.index('m'))#search for the index of the first apperence of the char#13
print(s.index('me'))#search for the index of the start of the substring#16
print(s.startswith('hi'))#True#does the string start with this substring
print(s.startswith('h'))#True
print(s.endswith('e'))#True

#spliting a character
words = "hello world, it's me"
print(words.split())#['hello', 'world,', "it's", 'me']
date_of_today= '15.9.2023'
day,month,year = date_of_today.split('.')
the_date = '-'.join([day,month,year])
print(the_date)#15-9-2023

#join
words = "pluto is a planet!"
combined =' 👏 '.join([word.upper() for word in words.split()])#PLUTO 👏 IS 👏 A 👏 PLANET!
print(combined)

#parse to string
day = str(9)
print('we will be aired at 2 am on the '+day+"th",sep='')#we will be aired at 2 am on the 9th

print('{}, we wil be aired at 2 on the {}th'.format('hi',9))#hi, we wil be aired at 2 on the 9th
print('%s, we will be aired at 2 am on the %dth'%('hi',9))#hi, we will be aired at 2 am on the 9th

#more on formate
print('{0} everyone, it is ur favorite {1} ,{0}! {1}! '.format('hi','programmer'))#hi everyone, it is ur favorite programmer ,hi! programmer!

#more on formating numbers in strings
print('my weight is {:.1} and my age is {:.2} '.format(52.5,22.5))
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
print(pluto_mass / earth_mass, '{:.3%},{:,}'.format(pluto_mass / earth_mass,population))#0.002181775560095107 0.218%,52,910,390

#rstrip(set of characters)
#rstrip remove any one of those characters if found at the end of a string
dirty = 'Deyar,lmm,.'
clean = dirty.rstrip()
print(clean)#Deyar,lmm,.
clean = dirty.rstrip('lm.,')
print(clean)#Deyar

#problem soliving
'''A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

Your function should meet the following criteria:

Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.
add Codeadd Markdown'''
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.
    """
    indicies = []
    for index, document in enumerate(doc_list):
        words = document.split()
        clean_words = [(word.rstrip('.,')).lower() for word in words]

        if(keyword.lower() in clean_words):
            indicies.append(index)

    return(indicies)

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville", 'saw a casIno, let us enter']
print(word_search(doc_list, 'casino'))


