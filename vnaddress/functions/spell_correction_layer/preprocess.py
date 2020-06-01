# import csv
# import os
# import re
#
# from django.conf import settingssettings
#
#
# def handle_numeric_name(raw_name, subfix_pattern):
#     # name = raw_name.replace(subfix_pattern + " ", "")
#     name = re.sub(subfix_pattern, "", raw_name, 1)
#     if name.isdigit():
#         return raw_name
#     else:
#         return name
#
#
# def handle_province(raw_name):
#     if re.compile("^(T|t)hành (P|p)hố ").match(raw_name):
#         province_name = re.sub(r"^(T|t)hành (P|p)hố ", "", raw_name, 1)
#
#     elif re.compile("^(T|t)ỉnh ").match(raw_name):
#         province_name = re.sub(r"^(T|t)ỉnh ", "", raw_name, 1)
#
#     else:
#         province_name = raw_name
#
#     return province_name
#
#
# def handle_district(raw_name):
#     if re.compile("^(Q|q)uận ").match(raw_name):
#         district_name = handle_numeric_name(raw_name, r"^(Q|q)uận ")
#
#     elif re.compile("^(H|h)uyện ").match(raw_name):
#         district_name = re.sub(r"^(H|h)uyện ", "", raw_name, 1)
#         # result_tuple = (district_name, "QH_H")
#
#     elif re.compile("^(T|t)hành (P|p)hố ").match(raw_name):
#         district_name = re.sub(r"^(T|t)hành (P|p)hố ", "", raw_name, 1)
#
#     elif re.compile("^(T|t)hị (X|x)ã ").match(raw_name):
#         district_name = re.sub(r"^(T|t)hị (X|x)ã ", "", raw_name, 1)
#
#     else:
#         district_name = raw_name
#
#     return district_name
#
#
# def handle_commune(raw_name):
#     if re.compile("^(X|x)ã ").match(raw_name):
#         commune_name = re.sub(r"^(X|x)ã ", "", raw_name, 1)
#
#     elif re.compile("^(P|p)hường ").match(raw_name):
#         commune_name = handle_numeric_name(raw_name, r"^(P|p)hường ")
#
#     elif re.compile("^(T|t)hị (T|t)rấn ").match(raw_name):
#         commune_name = re.sub(r"^(T|t)hị (T|t)rấn ", "", raw_name, 1)
#
#     else:
#         commune_name = raw_name
#
#     return commune_name
#
#
# def process_csv_file(csv_path):
#     print(csv_path)
#     result = []
#     with open(csv_path) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for index, row in enumerate(csv_reader):
#             province = handle_province(row[0])
#             district = handle_district(row[2])
#             commune = handle_commune(row[4])
#
#             result.append(province) if province != "" and province not in result else None
#             result.append(district) if district != "" and district not in result else None
#             result.append(commune) if commune != "" and commune not in result else None
#
#     with open('{}/{}/dvhc.txt'.format(settings.BASE_DIR, os.environ.get("STANDARDIZER_FILE_PATH")), 'w') as dvhc:
#         for word in result:
#             dvhc.write('{}\n'.format(word))
#
#     with open('{}/{}/names.txt'.format(settings.BASE_DIR, os.environ.get("STANDARDIZER_FILE_PATH")), 'w') as name_file:
#         names = []
#         for word in result:
#             names.append("{}".format(word))
#         name_file.write('{}'.format(names))
#
#     print(len(result))
#     return result
#
