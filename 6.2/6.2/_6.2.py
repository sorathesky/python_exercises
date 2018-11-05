# Default arguments
# Variadic functions, functions with unlimited parameters
# difference between arguments and parameters

import datetime as dt

def add0(a, b, c): # Parameters of a function
  return a + b + c

print(add0(1, 2, 3))  # arguments in a function

def add1(*numbers): # use of tuple in a variadic function
  total = 0
  for n in numbers:
    total += n
  return total

print(add1(1, 2, 3, 4, 5, 6)) 

def record_time( message, time = dt.datetime.now() ): # time is a default parameter
  
  # could be saved to a file
  print("{:}, time: {:}".format(message, time))

record_time("It is the morning") # functions with default parameter don't need arguments for that parameter
record_time("It is the morning", "Feb 22nd, 1998") # default parameters can be overwritten





