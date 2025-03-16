import string

input_text = input("Enter the string: ")
clean_text = input_text.translate(str.maketrans('', '', string.punctuation))
words = clean_text.split()
capitalized_words = [word.capitalize() for word in words]
hashtag = "#" + "".join(capitalized_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]


print(hashtag)