import math

def mean(arr):
	total = sum(arr)
	return total / len(arr)

print(f"Mean is: {mean({1, 2, 3, 4, 5})}")