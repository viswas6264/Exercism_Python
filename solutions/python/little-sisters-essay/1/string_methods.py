def capitalize_title(title):
    words=title.split()
    new_words=[]
    for word in words:
        new_words.append(word[0].upper()+word[1:])
    return " ".join(new_words)

def check_sentence_ending(sentence):
    return sentence.endswith(".")
    
def clean_up_spacing(sentence):
    return sentence.strip(" ")

def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word,new_word)