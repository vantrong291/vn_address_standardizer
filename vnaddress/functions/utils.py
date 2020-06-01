def sentence2list(sentence):
    return sentence.split(', ')

def list_subtract(first, sencond):
    return (list(set(first) - set(sencond)))