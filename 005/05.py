# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

# not the cleanest solution, I am sure using maths could avoid looping on
# every natural member

DIVISORS = range(1,21)

n = 1
while True:
    if all([n % x == 0 for x in DIVISORS]) == True:
        break;
    n += 1
    
print "%d" % (n)