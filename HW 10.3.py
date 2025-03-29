def is_even(digit):
    """ Перевірка чи є парним число """
    if digit %2 == 0:
        return True
    else:
        return False

assert is_even(2) == True, 'Test1'
print(is_even(2))
assert is_even(5) == False, 'Test2'
print(is_even(5))
assert is_even(0) == True, 'Test3'
print(is_even(0))

print('OK')