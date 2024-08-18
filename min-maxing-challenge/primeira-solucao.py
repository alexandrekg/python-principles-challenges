def largest_difference(numbers):
    return max(numbers) - min(numbers)

print(largest_difference([1, 2, 3]), largest_difference([1, 2, 3]) == 2)
print(largest_difference([20, 30, 50]), largest_difference([20, 30, 50]) == 30)
print(largest_difference([50, 2, 80]), largest_difference([50, 2, 80]) == 78)
print(largest_difference([90, 25, 65]), largest_difference([90, 25, 65]) == 65)
