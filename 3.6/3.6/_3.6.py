


a = list(range(0, 10))
print(a)
print()

#List Slicing to query parts of an array
print(a[0:5])
print(a[2:len(a)])
print(a[2:])
print(a[:])
print()

print(a[::])
print(a[::1])
print(a[::2])
print(a[0:6:2])
print()

#Reverse Slicing
#Reverse Indexing
# negative indexing can create bugs
print(a[-1])
print(a[2:-1])

print(a[::-1])
print(a[::-2])