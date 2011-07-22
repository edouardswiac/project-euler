# The sum of the squares of the first ten natural numbers is,
# 1sq + 2sq + ... + 10sq = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)sq = 55sq = 3025
#
# Hence the difference between the sum of the squares of the first ten 
# natural numbers and the square of the sum is 3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

numbers = range(1, 101)
diff = pow(sum(numbers),2) - sum([pow(n,2) for n in numbers])

print "Difference is %d" % (diff)