def get_word_count(text):
    return len(text.split())

def get_char_count(text):
        text = text.lower()
        character_count = {i: text.count(i) for i in set(text)}
        return character_count

def sort_on(dict):
    return dict["num"]

def char_count_sorted(charcount):
    char_list = []
    for c in charcount:
#         num = charcount[c]
         if c.isalpha(): 
             char_list.append({"char": c, "num": charcount[c]})
         char_list.sort(reverse=True, key=sort_on)    
    return char_list



