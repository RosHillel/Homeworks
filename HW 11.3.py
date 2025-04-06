def is_even(number):
    last_digit = int(str(number)[-1])
    if last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8:
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
print(is_even(2494563894038**2))
assert is_even(1056897**2) == False, 'Test2'
print(is_even(1056897**2))
assert is_even(24945638940387**3) == False, 'Test3'
print(is_even(24945638940387**3))


### другий варіант


def is_even(number):
    last_digit = int(str(number)[-1])
    match last_digit:
        case 0:
            return True
        case 2:
            return True
        case 4:
            return True
        case 6:
            return True
        case 8:
            return True
        case _:
            return False


assert is_even(2494563894038**2) == True, 'Test1'
print(is_even(2494563894038**2))
assert is_even(1056897**2) == False, 'Test2'
print(is_even(1056897**2))
assert is_even(24945638940387**3) == False, 'Test3'
print(is_even(24945638940387**3))