def translate(text):
    vowels = "aeiou"
    words = text.split()
    result = []
    for word in words:
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            result.append(word + "ay")
            continue
        i = 0
        while i < len(word):
            if word[i] in vowels:
                break
            if i + 1 < len(word) and word[i] == 'q' and word[i+1] == 'u':
                i += 2
                break
            if word[i+1:i+2] == 'y':
                i += 1
                break
            i += 1
        result.append(word[i:] + word[:i] + "ay")
    return " ".join(result) 