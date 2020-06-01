from nltk.tag.util import untag
from .word2features import word2features


def transform_to_dataset(tagged_sentences):
    X, y = [], []

    for tagged in tagged_sentences:
        X.append([word2features(untag(tagged), index) for index in range(len(tagged))])
        y.append([tag for _, tag in tagged])

    # print("y")
    # print(y)

    return X, y
