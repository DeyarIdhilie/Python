from math import *
from numpy import *

#the statment bellow will throw an error why, because the compiler face a difficult-to-debug situation
#which is both numpy and math modules have a function called log
#the second import shadow the first one
'''print(pi, log(32,2))'''#TypeError: return arrays must be of ArrayType

#let's try to solve
'''print(math.pi)'''#NameError: name 'math' is not defined. Did you mean: 'mat'?

