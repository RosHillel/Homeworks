number = int(input("Enter a number: "))

if number <= 9:
    print(number)
while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    number = product
    print(number)