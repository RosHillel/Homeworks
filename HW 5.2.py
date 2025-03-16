while True:

    number_1 = int(input("Введіть перше число: "))
    number_2 = int(input("Введіть друге число: "))
    mathe_operation = (input("Введіть дію над числами: "))   # +, -, *, /


    match mathe_operation:
        case "+":
            print(number_1 + number_2)
        case "-":
            print(number_1 - number_2)
        case "*":
            print(number_1 * number_2)
        case "/":
            if number_2 > 0:
                print(number_1 / number_2)
            else:
                print("\nНа нуль ділити не можна!")
        case _:
            print("\nНекоректна дія")

    user_input = input("Enter 'y' to continue: ")
    if user_input == "y":
        print("continued...")
        continue
    else:
        break




