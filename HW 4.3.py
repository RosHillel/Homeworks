import random

nums_size = random.randint(3, 10)
numbers = []

for i in range(nums_size):
    numbers.append(random.randint(1, 10))

print(numbers)

print(f"[{numbers[0]}, {numbers[2]}, {numbers[-2]}]")


