# The various types of Comparison Operators include:
# ==, =!, <, >, <=, >=

tmp = """
(-∞, -30) REALLY COLD!
(-30, 0)  cold
0         zero
(0, 20)   perfect  
[20, 40)  hot  
[40, ∞)   REALLY HOT!"""
print(tmp)

t = int(input())

if (t <= -30):
    print("REALLY COLD!")
if (t < 0):
    if (t > -30):
        print("cold!")
if (t == 0):
    print("zero!")
if (t > 0):
    if (t < 20):
        print("perfect!")
if (t >= 20):
    if (t < 40):
        print("hot!")
if (t >= 40):
        print("REALLY HOT!")