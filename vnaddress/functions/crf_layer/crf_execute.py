import logging
import time

import joblib

from .constants import tag_order, exactly_tags
# from .preprocess import process_csv_file
from .transform_to_dataset import transform_to_dataset
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


# def crf_train(csv_path, model_path):
#     tagged_sentences, standard_addresses = process_csv_file(csv_path)
#     print("Tagged sentences: ", len(tagged_sentences))
#
#     # Split the dataset for training and testing
#     cutoff = int(1 * len(tagged_sentences))
#     training_sentences = tagged_sentences[:cutoff]
#     # test_sentences = tagged_sentences[cutoff:]
#
#     X_train, y_train = transform_to_dataset(training_sentences)
#     # X_test, y_test = transform_to_dataset(test_sentences)
#
#     from sklearn_crfsuite import CRF
#
#     model = CRF(
#         algorithm='lbfgs',
#         c1=0.1,
#         c2=0.1,
#         max_iterations=150,
#         # all_possible_transitions=True
#     )
#     model.fit(X_train, y_train)
#     joblib.dump(model, model_path)
#
#     return model_path, standard_addresses

# def full_crf_execute(train, model_path, sentence):
#     start = time.time()
#
#     if train:
#         tagged_sentences = process_csv_file(
#             "{}/{}/dvhc.csv".format(settings.BASE_DIR, os.environ.get("STANDARDIZER_FILE_PATH")))
#         print("Tagged sentences: ", len(tagged_sentences))
#
#         # Split the dataset for training and testing
#         cutoff = int(1 * len(tagged_sentences))
#         training_sentences = tagged_sentences[:cutoff]
#         test_sentences = tagged_sentences[cutoff:]
#
#         X_train, y_train = transform_to_dataset(training_sentences)
#         X_test, y_test = transform_to_dataset(test_sentences)
#
#         # print(len(X_train))
#         # print(len(X_test))
#         # print(X_train[0])
#         # print(y_train[0])
#
#         from sklearn_crfsuite import CRF
#
#         model = CRF(
#             algorithm='lbfgs',
#             c1=0.1,
#             c2=0.1,
#             max_iterations=150,
#             # all_possible_transitions=True
#         )
#         model.fit(X_train, y_train)
#         joblib.dump(model, model_path)
#         loaded_model = joblib.load(model_path)
#
#     else:
#         loaded_model = joblib.load(model_path)
#
#     unsorted_result = pos_tag(loaded_model, sentence)
#     sorted_result = sorted(unsorted_result, key=lambda x: tag_order[extract_relative_tag(x[1])], reverse=False)
#
#     end = time.time()
#     print('[{:.4f} s] Function crf_execute {} executed'.format((end - start), sentence))
#
#     return sorted_result
