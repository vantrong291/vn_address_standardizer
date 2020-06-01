def word2features(sentence, index):
    # print(index)
    return {
        # 'character_length': len(sentence[index]),
        # 'word_length': sentence[index].count(" ") + 1,
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        # 'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        # 'is_all_upper': sentence[index].upper() == sentence[index],
        # 'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'prefix-4': sentence[index][:4],
        'prefix-5': sentence[index][:5],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'suffix-4': sentence[index][-4:],
        'suffix-5': sentence[index][-5:],
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }
