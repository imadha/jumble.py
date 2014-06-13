def build_dictionary(word_list):
    dictionary = {}
    # open file, santize each word, and key them in lists by their sorted value
    with open(word_list, 'r') as f:
        for word in f:
            word = word.lower().strip()
            key = ''.join(sorted(word))
            dictionary.setdefault(key,[]).append(word)
    return dictionary

def jumble(word, dictionary):
    # make a powerset to get all sorted letter combinations
    combos = [[]]
    for i in sorted(word):
        combos += [j+[i] for j in combos]
    # loop through powerset and check dictionary, ignoring keys 1 character or less  
    words = set()
    for key in combos:
        key = ''.join(key)
        if len(key) > 1 and key in dictionary:
            words.update(dictionary[key])
    return sorted(words)
