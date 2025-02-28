number = int(input("Введіть 5ти значне число: ")) #12345
n1 = number % 10
n2 = number % 100 // 10
n3 = number % 1000 // 100
n4 = number % 10000 // 1000
n5 = number // 10000

print(n1, n2, n3, n4, n5, sep="\n")