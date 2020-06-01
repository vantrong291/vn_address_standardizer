import time

from fuzzywuzzy import process, fuzz


def match_word(error_dict, word_to_check, standard_single_names):
    # start = time.time()
    weight = 0
    match = ""
    for key in error_dict:
        name_to_check = word_to_check
        # standard_single_names_lower = [name.lower() for name in standard_single_names]
        if name_to_check not in standard_single_names:
            extraction = (process.extractOne(name_to_check, error_dict[key], scorer=fuzz.ratio))
            if extraction[1] > weight:
                # print(weight, key, name_to_check)
                weight = extraction[1]
                match = key
        else:
            match = name_to_check
    # end = time.time()
    # print('[{:.4f} s] Function match_word {} executed'.format((end - start), word_to_check))

    return match


def match_sentence(error_dict, sentence_to_check, standard_addresses):
    # start = time.time()
    weight = 0
    match = ""
    for key in error_dict:
        # name_to_check = sentence_to_check
        # standard_single_names_lower = [name.lower() for name in standard_single_names]
        if sentence_to_check not in standard_addresses:
            extraction = (process.extractOne(sentence_to_check, error_dict[key], scorer=fuzz.ratio))
            if extraction[1] > weight:
                # print(weight, key, name_to_check)
                weight = extraction[1]
                match = key
        else:
            match = sentence_to_check
    # end = time.time()
    # print('[{:.4f} s] Function match_sentence {} executed'.format((end - start), sentence_to_check))

    return match
