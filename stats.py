def get_word_count(text):
    return len(text.split())

def get_char_count(text):
        text = text.lower()
        character_count = {i: text.count(i) for i in set(text)}
        return character_count
    