def is_pangram(sentence):
    if len(sentence)<26:
        return False
    sentence=sentence.lower()
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in sentence:
            return False
    return True