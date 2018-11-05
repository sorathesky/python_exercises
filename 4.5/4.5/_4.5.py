# Three small programs
# Basic Conditional logic from 4.4
# and, or, and not

# Program that given two variables a and b will print "divisible"
# If one number can divide the other
a, b = int(input("a = ")), int(input("b = "))
if a % b == 0 or b % a == 0:
    print("divisible")


# Given input c, d print c/d if d is not equal to zero
# c, d = int(input("c = ")), int(input("d = "))
# if d != 0: print(c/d)
# if b is not 0: print(c/d)
# if not(b == -0): print(c/d)


# write a program that prints "equal" 
# if all three names are equal to each other when lowercase

name1 = input("name1")
name2 = input("name2")
name3 = input("name3")

if name1.lower() == name2.lower() == name3.lower():
    print("equal")
