# prime number checker 
# A prime number is a number that is not divisible by any number other than one and itself
# Primes: 2,3,5,7,11,13,17,19,23,27,29,31,37,41,43
# The number one by definition is not prime
# The number 10 is not prime because it has factors [2, 5] which divide into it

#n = int(input("n = "))
for n in range(-10, 10):
  if n >= 2:
    divisors = []
    for divisor in range(2, n):
      if n % divisor == 0:
        divisors.append(divisor)
  
    if len(divisors) == 0:  # Prime!
      print("{:d} is prime!".format(n))
    else:
      print("{:d} is not prime because {:} divide {:d}".format(n, str(divisors), n))
  else:
    print("{:d} is not prime!".format(n))
