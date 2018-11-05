# What is a function that returns a value
# What is a "void" function and when to use it
# When do we use a void function versus when do we use a function with a return value
# A function which produces output and uses the return keyword returns an assignable value to a variable 
# Examples of a function which returns assignable values is: max_value = max ([3, 6, 2, 9])
# chunks = ".split() returns a lsit of strings separated by spaces".split()
# list_length = len(["a", "b", "c"])

def is_even(number):
  if number % 2 == 0:
    return True

  return False

# A void function does not return a value, it performs an action. Void functions do not use the "return" keyword in their implementation
# Examples of void functions include: print("I return nothing, I just print things on console")
# .sort(), .insert()

def is_even(number):
  if number % 2 == 0:
    print("{} is even".format(number))
  else:
    print("{} is odd".format(number))