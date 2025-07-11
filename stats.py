def count_words(text):
    num_words = text.split()
    return len(num_words)
    
def count_characters(text):
    characters_dict = {}
    for character in text:
        character = character.lower()
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

def Sort_on(characters_dict):
        return characters_dict["num"]

def chars_dict_to_sorted_list(characters_dict):
    sorted_list = []
    for char in characters_dict:
         sorted_list.append({"char": char, "num": characters_dict[char]})
    sorted_list.sort(reverse=True, key=Sort_on)
    return sorted_list
