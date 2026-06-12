def is_isogram(string):
    string=string.lower().replace("-", "").replace(" ", "")
    frequency={}
    for letter in string:
        if letter in frequency:
            frequency[letter]+=1
        else:
            frequency[letter]=1
    for letter in string:
        if frequency[letter]!=1:
            return False
    return True