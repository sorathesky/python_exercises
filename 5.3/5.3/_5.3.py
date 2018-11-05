my_list = [1, 2, 3, 4, 5]
my_tuple = (2, 7, 8, 9, 10) # Immutable, cannot be appended
my_string = "Hello World!"

# What is an iterable
print('__iter__' in dir(my_list))
print('__iter__' in dir(my_tuple))
print('__iter__' in dir(my_string))

# Examples
#for elem in my_list:
#  print(elem)

list_iterator = iter(my_list) # ability to grab next objects in list

while True:   # Iters till end of list
    try:
      next_elem = next(list_iterator) 
      print(next_elem)
    except StopIteration:
      break
    