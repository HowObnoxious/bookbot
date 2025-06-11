stats.py 

def words_in_string(string):

    word_count = 0

    for word in string.split():
        word_count += 1
    
    print(f"Found {word_count} total words")

def character_count(string):

    low_string = string.lower()

    character_dict = {}

    for character in low_string:
        if character.isalpha():
            if character not in character_dict: 
                character_dict[character] = 1
            else:
                character_dict[character] += 1

    return character_dict

def sort_characters(dict):
    characters = [{"char": character, "num": count} for character, count in dict.items()]

    n = len(characters)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if characters[j]["num"] > characters[max_index]["num"]:
                max_index = j
        characters[i], characters[max_index] = characters[max_index], characters[i]


    return characters


