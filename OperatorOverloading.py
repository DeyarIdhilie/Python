num1 = 3
string1 = 'hello '
#the code below is showing 'operator oveloading' --> this is when the same operator has differnet meaning depending on what kind of things they are applied to
num1 = num1 * 3
print(num1) #output is 9

string1 = string1 * 3
print(string1) #output is hello hello hello

word1 = 'hello'
word2 = 'world'

sentence = word1 + ' '+ word2
print(sentence)#hello world
sentence = sentence + '!'
print(sentence)