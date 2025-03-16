import string
import keyword

text_data = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
             'get_Value', '3m', 'm3', 'assert', 'assert_exception', 'some_super_puper__value']

for text_variable in text_data:
    if len(text_variable) > 0:
        if text_variable in keyword.kwlist:
            print(f"{text_variable} => False")
        elif text_variable.find("_") == 0 and text_variable.find("_", 1) == -1:
            is_correct = True
            print(f"{text_variable} => True")
        elif text_variable.find("__") != -1:
            is_correct = False
            print(f"{text_variable} => False")
        elif not text_variable[0].isnumeric() and text_variable.islower() and text_variable.find(" ") == -1:
            is_correct = True
            for symbol in string.punctuation.replace("_", ""):
                if symbol in text_variable:
                    is_correct = False
                    print(f"{text_variable} => False")
                    break

            if is_correct:
                print(f"{text_variable} => True")
        else:
            print(f"{text_variable} => False")