def rotate(text, key):
    result=''
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                shifted=(ord(letter)-ord('a')+key)%26
                result+=chr(ord('a')+shifted)
            else:
                shifted=(ord(letter)-ord('A')+key)%26
                result+=chr(ord('A')+shifted)
        else:
            result+=letter
    return result
