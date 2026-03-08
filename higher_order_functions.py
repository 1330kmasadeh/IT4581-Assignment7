# higher_order_functions.py
# Demonstrating higher-order functions: map, filter, reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# mapping example
mapped = list(map(lambda x: x * 2, numbers))
print("Map result:", mapped)

# filtering example
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter result:", filtered)

# reducing example
reduced = reduce(lambda x, y: x + y, numbers)
print("Reduce result:", reduced)
