import logging
import time

import joblib

from .constants import tag_order, exactly_tags
from .word2features import word2features

logger = logging.getLogger(__name__)


def pos_tag(model, sentence):
    sentence_features = [word2features(sentence, index) for index in range(len(sentence))]
    # print("model.predict([sentence_features])", model.predict([sentence_features]))
    return list(zip(sentence, model.predict([sentence_features])[0]))


def extract_relative_tag(tag):
    return tag.split('_')[0]


def extract_exactly_tag(tag):
    return tag.split('_')[1]


def sentence2list(sentence):
    return sentence.split(', ')


def list2sentence(list):
    result_list = []
    for item in list:
        relative_tag = extract_exactly_tag(item[1])
        # logger.info(item[0])
        name_list = item[0].split(" ")
        if len(name_list) > 1 and name_list[1].isdigit():
            address = item[0]
        else:
            address = "{} {}".format(exactly_tags[relative_tag], item[0])
        result_list.append(address)

    return ", ".join(result_list)


def crf_execute(model_path, sentence):
    # start = time.time()

    loaded_model = joblib.load(model_path)
    unsorted_result = pos_tag(loaded_model, sentence)
    sorted_result = sorted(unsorted_result, key=lambda x: tag_order[extract_relative_tag(x[1])], reverse=False)

    # end = time.time()
    # print('[{:.4f} s] Function crf_execute {} executed'.format((end - start), sentence))

    return sorted_result
