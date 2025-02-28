number = int(input("Введите 4-х значное число: "))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 1000 % 100 // 10   #n3 = number % 1000 // 10 % 10 (як альтернатива)
n4 = number % 1000 % 100 % 10

print(n1, n2, n3, n4, sep="\n")
