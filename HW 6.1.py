import string

alphabet = string.ascii_letters
print(alphabet)

interval = input("Enter the interval from a to Z: ")
letters = interval.split("-")
print(letters)

start_index = alphabet.index(letters[0])
end_index = alphabet.index(letters[1])

if start_index < end_index:
    result = alphabet[start_index:end_index + 1]
    print(result)
elif start_index > end_index:
    result1 = alphabet[start_index:]
    result2 = alphabet[:end_index + 1]
    print(result1, result2, sep="")
elif start_index == end_index:
    print(letters[0])


