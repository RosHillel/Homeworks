numbers = [1, 2, 3, 4, 5, 6]
median = len(numbers) // 2

if len(numbers) % 2 != 0:
    median += 1

list1 = numbers[:median]
list2 = numbers[median:]
print(list1, list2, sep=", ")