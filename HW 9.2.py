def difference(numbers):
    if len(numbers) > 0:
        max_number = max(numbers)
        min_number = min(numbers)
        variance = max(numbers) - min(numbers)
        result = round(variance, 2)

        return result
    else:
        return 0

assert difference([1, 2, 3]) == 2, 'Test1'
print(difference([1, 2, 3]))
assert difference([5, -5]) == 10, 'Test2'
print(difference([5, -5]))
assert difference([10.2, -2.2, 0, 1.1, 0.5]) == 12.4, 'Test3'
print(difference([10.2, -2.2, 0, 1.1, 0.5]))
assert difference([]) == 0, 'Test4'
print(difference([]))

print('OK')