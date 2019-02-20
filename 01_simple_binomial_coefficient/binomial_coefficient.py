import math
print("Hello, world!")

# "n choose k" or (n/k) is a binomial coefficient
# it is the number of ways to choose a k-element subset from a n-element set

# lets wait on more number theory.

n = 10
k = 5

numerator = math.factorial(n)
denominator = math.factorial(k)*math.factorial(n-k)

print (numerator / denominator)