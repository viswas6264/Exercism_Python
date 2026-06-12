def add_prefix_un(word):
    return ("un"+word)

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = [prefix]+[prefix + word for word in vocab_words[1:]]
    return " :: ".join(words)

def remove_suffix_ness(word):
    if word.endswith("ness"):
        word=word[:-4]
        if word.endswith("i"):
            word=word[:-1]+"y"
    return word

def adjective_to_verb(sentence, index):
    words=sentence.split()
    word=words[index]
    word=word.rstrip(".,?!")
    return word+"en"