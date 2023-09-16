#dictionaries are a built-in datastructure in python
#which map keys to values
#dictionary = {key:value}

dec1 = {'one':1, 'two':2, 'three':3}
print(dec1['one'])#1 #note: values are accessed by their keys
"""print(dec1[1])#error"""

#how to add a new pair
dec1['four']= 4
print(dec1)#{'one': 1, 'two': 2, 'three': 3, 'four': 4}

#how to change a value
dec1['one']='1'
print(dec1)#{'one': '1', 'two': 2, 'three': 3, 'four': 4}

#can i add and change at the same time
dec1.update({"one":1, "five":5})
print(dec1)#{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

#creat a new ditcionary with old dictionary
dec2 = {**dec1, "six":6}
print(dec2)#{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

#dictionary comprehesnion
list1s = ['hello', 'Deyar']
new_dict = {list1:list1[0] for list1 in list1s }
print(new_dict)#{'hello': 'h', 'Deyar': 'D'}

#search for a key
planets = {'Mercury': 'M',
 'Venus': 'V',
 'Earth': 'E',
 'Mars': 'M',
 'Jupiter': 'J',
 'Saturn': 'S',
 'Uranus': 'U',
 'Neptune': 'N'}

print('venus' in planets)#False
print('Venus'in planets)#True
print('moon' in planets)#False

#loop through the dictionary
#as seen below, dictionaries now are ordered and remeber the order each insertion happened
for key,value in planets.items():
    print(key,value)
'''Mercury M
Venus V
Earth E
Mars M
Jupiter J
Saturn S
Uranus U
Neptune N'''

planets["Earth"] = 'e'

for key,value in planets.items():
    print(key,value)
'''
Mercury M
Venus V
Earth e
Mars M
Jupiter J
Saturn S
Uranus U
Neptune N'''

for planet in planets:
    print('{} = {}'.format(planet,planets[planet]))
'''Mercury = M
Venus = V
Earth = e
Mars = M
Jupiter = J
Saturn = S
Uranus = U
Neptune = N'''

print(dec1)

for planet, initial in planets.items():
    print('Planet {} starts with \"{}\"'.format(planet,initial))
'''Planet Mercury starts with "M"
Planet Venus starts with "V"
Planet Earth starts with "e"
Planet Mars starts with "M"
Planet Jupiter starts with "J"
Planet Saturn starts with "S"
Planet Uranus starts with "U"
Planet Neptune starts with "N"
'''

#delete a pair
my_dict = {"name": "John", "age": 30, "city": "New York"}
"""del my_dict['country']#KeyError: 'country'"""
#to avoid keyError
if 'age' in my_dict:
    del my_dict["age"]
print(my_dict)#{'name': 'John', 'city': 'New York'}

#pop, delete and return the key's value
print(my_dict.pop('name'))#John
#what will happen if the key doesn't exist
"""print(my_dict.pop('country'))#KeyError: 'country'"""
#so how to solve it ? add a default value
print(my_dict.pop('country', None))#None
print(my_dict.pop('country', 'palestine'))#palestine
print(my_dict.pop('city',None))#New York










