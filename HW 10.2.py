import re

def first_word(text):
    """ Пошук першого слова """
    words = re.findall(r"[a-zA-Z']+", text)
    return words[0] if words else ""


assert first_word("Hello world") == "Hello", 'Test1'
print(first_word("Hello world"))
assert first_word("greetings, friends") == "greetings", 'Test2'
print(first_word("greetings, friends"))
assert first_word("don't touch it") == "don't", 'Test3'
print(first_word("don't touch it"))
assert first_word(".., and so on ...") == "and", 'Test4'
print(first_word(".., and so on ..."))
assert first_word("hi") == "hi", 'Test5'
print(first_word("hi"))
assert first_word("Hello.World") == "Hello", 'Test6'
print(first_word("Hello.World"))

print('OK')