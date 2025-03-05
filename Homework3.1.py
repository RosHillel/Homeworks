number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))
mathe_operation = (input("Введіть дію над числами: "))   # +, -, *, /


# v1
# if mathe_operation == "+":
#     print(number_1 + number_2)
# elif mathe_operation == "-":
#     print(number_1 - number_2)
# elif mathe_operation == "*":
#     print(number_1 * number_2)
# elif mathe_operation == "/" and number_2 > 0:
#     print(number_1 / number_2)
# else:
#     print("\nДію не можна виконати!")


#v2
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




