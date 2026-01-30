def count_words(book_str:str):
    word_count = 0
    if type(book_str) == str:
        split_book_str = book_str.split()
        word_count = len(split_book_str)
    return word_count
        
def count_characters(book_str:str):
    char_count_dict = {}
    if type(book_str) == str:
        for i in book_str:
            lc_letter = i.lower()
            if lc_letter not in char_count_dict:
                char_count_dict[lc_letter] = 1
            else:
                char_count_dict[lc_letter] = char_count_dict[lc_letter] + 1
        return char_count_dict

def sort_on(items):   
    return items["num"]

def sort_characters(char_count_dict:dict):
    chars_count_list = []
    for i in char_count_dict:
        chars_count_list.append({
            "char": i,
            "num": char_count_dict[i]
        })
    if not chars_count_list.sort(reverse=True, key=sort_on):
        return chars_count_list
    return chars_count_list.sort(reverse=True, key=sort_on)
    