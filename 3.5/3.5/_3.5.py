
#import the pprint function from the pprint module as a function called pretty_print
from pprint import pprint as pretty_print

#import the copy and deepcopy functions from the copy module
from copy import copy, deepcopy




# 2D Matrix creation
nums_2d = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22]
]
print(nums_2d[1][3])
print()

print(nums_2d)
print()

pretty_print(nums_2d)

# 2D matrix manipulations
nums_2d[2][1] = -5
print()
pretty_print(nums_2d)

letters = ["A", "B", "C", "D", "E"]
letters_2d = [copy(letters), copy(letters), copy(letters)]
print()
pretty_print(letters_2d)

# Issues with matrix referencing
# when building arrays of arrays you are referencing not copying so the original is changed across all refrences
# creates unecessary bugs

print()
letters_2d[0][0] = "F"
pretty_print(letters_2d)