#!C:\python34
n = 23
f = 1.2345678
s = "Computer"

print("my name is {:b}".format(n))
print("my name is {:d}".format(n))

print("{:f}".format(f))
print("{:.3f}".format(f))
print("{:11.3f}".format(f))

print("{0} {1} {2}".format(n,f,s))

print("{name} own\'s {amount} {object}".format(    
    name = "Will",
    amount = 5,
    object = "mangos"
))

