def reverse(text):
    reversed=""
    for letter in text:
        reversed=letter+reversed
    return reversed