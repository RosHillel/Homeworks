def find_unique_value(some_list):
    unique_numbers = []
    for num in some_list:
        if some_list.count(num) == 1:
            unique_numbers = num
            break
    return unique_numbers


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
print(find_unique_value([1, 2, 1, 1]))
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
print(find_unique_value([2, 3, 3, 3, 5, 5]))
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
print("ОК")