def add_one(some_list):
    number = int("".join(map(str, some_list)))
    changed_number = number + 1
    result_list = [int(i) for i in str(changed_number)]
    return result_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
print(add_one([1, 2, 3, 4]))
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
print(add_one([9, 9, 9]))
assert add_one([0]) == [1], 'Test3'
print(add_one([0]))
assert add_one([9]) == [1, 0], 'Test4'
print(add_one([9]))
print("ОК")









