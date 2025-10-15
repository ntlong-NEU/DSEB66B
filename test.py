from functools import reduce
# Sum of all numbers in a list
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total) # Output: 10
