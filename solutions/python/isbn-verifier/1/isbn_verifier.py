def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    total = 0
    for digit in range(10):
        character = isbn[digit]
        if digit == 9 and character == "X":
            value = 10
        elif character.isdigit():
            value = int(character)
        else:
            return False
        total += value * (10 - digit)
    return total % 11 == 0