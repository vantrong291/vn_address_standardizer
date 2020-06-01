def generate_error_dict(standard_single_names, standard_addresses, single_vowels):
    spell_dict_length = len(single_vowels["à"])
    result = {}
    full_address_result = {}
    for w in standard_single_names:
        word_lower = w.lower()
        new_words = []
        for i in range(spell_dict_length):
            new_word = ""
            for spell_key in single_vowels:
                new_word = word_lower.replace(spell_key, single_vowels[spell_key][i])
                word_lower = new_word
            new_words.append(new_word)
        result.update({w: new_words})

    for w in standard_addresses:
        word_lower = w.lower()
        new_words = []
        for i in range(spell_dict_length):
            new_word = ""
            for spell_key in single_vowels:
                new_word = word_lower.replace(spell_key, single_vowels[spell_key][i])
                word_lower = new_word
            new_words.append(new_word)
            full_address_result.update({w: new_words})

    return result, full_address_result
