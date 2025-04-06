generate_cube_numbers = 1000
numbers = []
for i in range(generate_cube_numbers + 1):
    numbers.append(i)
numbers = numbers[2:]
# print(numbers)

cube = []
for num in numbers:
    if num ** 3 <= generate_cube_numbers:
        cube.append(num ** 3)
    else:
        break
print(cube)

# это я написал сам



def generate_cube_numbers(end):
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1

# это я написал с подсказкой, так как не совсем понял как работать с структурой с yield, gen... в функции 

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print('Ok')