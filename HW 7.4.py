def common_elements():
    multiples_of_3_and_5 = {x for x in range(100) if x % 3 == 0 and x % 5 == 0}

    return multiples_of_3_and_5

print(common_elements())
