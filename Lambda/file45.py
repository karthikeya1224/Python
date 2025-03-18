from functools import reduce
data = [5, 10, 15, 20, 25]
squares = list(map(lambda x: x ** 2, data))
filtered = list(filter(lambda x: x > 100, squares))
total = reduce(lambda x, y: x + y, filtered)
print(f"Squares: {squares}")
print(f"Filtered: {filtered}")
print(f"Total sum: {total}")
