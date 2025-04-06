prime_generator = 11
numbers = []

for i in range(prime_generator + 1):
    numbers.append(i)



# Фильтруем только простые числа
primes = []
for num in numbers:
    if num > 1:  # Простые числа начинаются с 2
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Проверка делителей
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

print("Простые числа:", primes)