s = "Hello world"
a = [4, 6, 9]

# "In" keyword
# Allows us to see what is in an object
print( 5 in a)
print( 4 in a)
print( "ello" in s)

# For loops with lists
for even_number in [2, 4, 6, 8, 10]:
    print(even_number)
    #can add more conditional code here too


odds = [1, 2, 5, 7, 9, 11]
for odd_number in odds:
    print(odd_number)

# for loops using indexing

print(range(len(odds)))

for index in range(len(odds)):
    print("Index: {:d}, odd number: {:d}".format(index, odds[index]))