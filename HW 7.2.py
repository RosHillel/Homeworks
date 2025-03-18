def correct_sentence(text):
    if not text[0].isupper():
        text = text.capitalize()
    if not text.endswith("."):
        text += "."
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends."
print(correct_sentence("greetings, friends"))
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
print(correct_sentence("greetings, friends"))
assert correct_sentence("hello") == "Hello.", 'Test2'
print(correct_sentence("hello"))
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
print(correct_sentence("Greetings. Friends"))
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
print(correct_sentence("Greetings, friends."))
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print(correct_sentence("greetings, friends."))
print('ОК')