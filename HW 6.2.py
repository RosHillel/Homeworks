while True:
    significance = int(input("Enter a value from >= 0 to 8640000: "))

    days = significance // 86400
    days_sec = days * 86400
    one_hour = 3600 # in seconds
    one_minute = 60  # in seconds
    remnant = significance - days_sec
    rest_hour = remnant // one_hour
    rest_sec = remnant % one_hour

    if days == 1:
        print(f"{days} день, ", end="")
    elif 20 < days < 100:
        if days % 10 == 1:
            print(f"{days} день, ", end="")
        elif 20 < days < 25:
            if days % 10 == 2 or 4:
                print(f"{days} дні, ", end="")
        else:
            print(f"{days} днів, ", end="")
    elif 2 <= days <= 4:
        print(f"{days} дні, ", end="")
    else:
        print(f"{days} днів, ", end="")

    if remnant >= one_hour:
        print(f"{str(rest_hour).zfill(2)}:", end="")
        if rest_sec // 60 < 60:
            print(f"{str(rest_sec // 60).zfill(2)}:", end="")
            print(str(rest_sec % 60).zfill(2))
        else:
            print("Fail")
    elif remnant < one_hour:
        print("00:", end="")
        if remnant >= 60:
            print(str(remnant // 60).zfill(2))
            print(str(remnant % 60).zfill(2))
        elif remnant < 60:
            print("00:00")
        else:
            print("Fail")

    user_input = input("Enter '-' to exit the program or any key to continue: ")
    if user_input == "-":
        print("Exit from program...")
        break
    else:
        continue