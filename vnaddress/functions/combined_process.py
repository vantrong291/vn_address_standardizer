# from crf_layer.crf_execute import crf_execute, list2sentence
# from fuzzywuzzy import fuzz, process
# from spell_correction_layer.generate_error_dict import generate_error_dict
# from spell_correction_layer.match_word import match_word
# from utils import sentence2list
#
# from crf_layer.constants import STANDARD_NAMES
#
#
# def combined_process(address, crf_train = False,):
#     address_list = ["Hải Hậuu, Hari Minh, Namdinh", "Khắc Niệm, Bắc Ninh, Bắc Ninh", "Hải Hậu, Nam Định, Cồn",
#                     "Ba Đình, Hà Nội, Phúc Xá", "Hà Nội", "Mai Dịch, Hà Nội, Cầu Giấy",
#                     "9, Phước Long B, Hồ Chí Minh", "Minh Khai, Hà Nội",
#                     "Nam Đàn, Nghệ An", "Đầm Dơi, Cà Mau, Taj An Khuwowng Nam", "Ninh Kiềuu, Cần Thơ"]
#     for index, address in enumerate(address_list):
#         address2list = sentence2list(address)
#         error_dict = generate_error_dict()
#         corrected_address2list = []
#         for name in address2list:
#             corrected_name = match_word(error_dict, name)
#             corrected_address2list.append(corrected_name)
#
#         crf_result = crf_execute(crf_train, "../models/finalized_model.sav", corrected_address2list)
#         name_only_crf_result = ", ".join([item[0] for item in crf_result])
#         # print(name_only_crf_result)
#         match_check = process.extractOne(name_only_crf_result, STANDARD_NAMES, scorer=fuzz.ratio)
#
#         print("{}. {} -> {}, match {}%".format(index + 1, address, list2sentence(crf_result), match_check[1]))
#
# combined_process("")