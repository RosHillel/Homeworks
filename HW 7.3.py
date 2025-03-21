def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None

    second_index = text.find(some_str, first_index + 1)
    if second_index != -1:
        return second_index
    else:
        return None


second_index("text", "some_str")
assert second_index("sims", "s") == 3, 'Test1'
print(second_index("sims", "s"))
assert second_index("find the river", "e") == 12, 'Test2'
print(second_index("find the river", "e"))
assert second_index("hi", "h") is None, 'Test3'
print(second_index("hi", "h"))
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print(second_index("Hello, hello", "lo"))
print('ОК')