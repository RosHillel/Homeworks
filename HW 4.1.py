numbers = [0, 1, 12, 0, 42, 3, 0]

for i in range(numbers.count(0)):
    numbers.remove(0)
    numbers.append(0)

print(numbers)






