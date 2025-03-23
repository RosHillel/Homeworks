import string

def is_palindrome(text):

    clean_text = "".join(text.translate(str.maketrans('', '', string.punctuation)).lower().split())

    if len(clean_text) == 1:
        return True

    elif len(clean_text) >= 2:
        if clean_text == clean_text[::-1]:
            return True
        else:
            return False
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
print(is_palindrome('A man, a plan, a canal: Panama'))
assert is_palindrome('0P') == False, 'Test2'
print(is_palindrome('0P'))
assert is_palindrome('a.') == True, 'Test3'
print(is_palindrome('a.'))
assert is_palindrome('aurora') == False, 'Test4'
print(is_palindrome('aurora'))
print("ОК")



