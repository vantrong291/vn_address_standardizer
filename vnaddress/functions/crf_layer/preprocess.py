import csv
import re


def handle_numeric_name(raw_name, subfix_pattern):
    # name = raw_name.replace(subfix_pattern + " ", "")
    name = re.sub(subfix_pattern, "", raw_name, 1)
    if name.isdigit():
        return raw_name
    else:
        return name


def handle_province(raw_name):
    if re.compile("^(T|t)hành (P|p)hố ").match(raw_name):
        province_name = re.sub(r"^(T|t)hành (P|p)hố ", "", raw_name, 1)
        result_tuple = (province_name, "TTP_TP")

    elif re.compile("^(T|t)ỉnh ").match(raw_name):
        province_name = re.sub(r"^(T|t)ỉnh ", "", raw_name, 1)
        result_tuple = (province_name, "TTP_T")

    else:
        result_tuple = (raw_name, "TTP_T")

    return result_tuple


def handle_district(raw_name):
    if re.compile("^(Q|q)uận ").match(raw_name):
        result_tuple = (handle_numeric_name(raw_name, r"^(Q|q)uận "), "QH_Q")

    elif re.compile("^(H|h)uyện ").match(raw_name):
        district_name = re.sub(r"^(H|h)uyện ", "", raw_name, 1)
        result_tuple = (district_name, "QH_H")

    elif re.compile("^(T|t)hành (P|p)hố ").match(raw_name):
        district_name = re.sub(r"^(T|t)hành (P|p)hố ", "", raw_name, 1)
        result_tuple = (district_name, "QH_TP")

    elif re.compile("^(T|t)hị (X|x)ã ").match(raw_name):
        district_name = re.sub(r"^(T|t)hị (X|x)ã ", "", raw_name, 1)
        result_tuple = (district_name, "QH_TX")

    else:
        result_tuple = (raw_name, "QH_H")

    return result_tuple


def handle_commune(raw_name):
    if re.compile("^(X|x)ã ").match(raw_name):
        commune_name = re.sub(r"^(X|x)ã ", "", raw_name, 1)
        result_tuple = (commune_name, "PX_X")

    elif re.compile("^(P|p)hường ").match(raw_name):
        result_tuple = (handle_numeric_name(raw_name, r"^(P|p)hường "), "PX_P")

    elif re.compile("^(T|t)hị (T|t)rấn ").match(raw_name):
        commune_name = re.sub(r"^(T|t)hị (T|t)rấn ", "", raw_name, 1)
        result_tuple = (commune_name, "PX_TT")

    else:
        result_tuple = (raw_name, "PX_X")

    return result_tuple


import random


def process_csv_file(csv_path):
    result = []
    standard_addresses = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        tmp_province_code = 0
        tmp_district_code = 0

        for index, row in enumerate(csv_reader):
            row_data = []
            # if row[1] != tmp_province_code:
            #     tmp_province_code = row[1]
            #     result.append([handle_province(row[0])])
            #
            # if row[3] != tmp_district_code:
            #     tmp_district_code = row[3]
            #     result.append([handle_district(row[2])])

            province = handle_province(row[0])
            district = handle_district(row[2])
            commune = handle_commune(row[4])

            # with open('../../datas/standard.txt', 'a') as name_file:
            #     name_file.write('\"{}, {}, {}\",\n'.format(commune[0], district[0], province[0]))

            row_data.append(province) if province[0] != "" else None
            row_data.append(district) if district[0] != "" else None
            row_data.append(commune) if commune[0] != "" else None
            random.shuffle(row_data)

            standard_addresses.append("{}, {}, {}".format(commune[0], district[0], province[0]))
            result.append(row_data)

    # print(result[0])
    # print(len(result))
    return result, standard_addresses

# process_csv_file("/home/vantrong291/workspaces/thesis/weaddress/backend/standardizer/datas/dvhc.csv")
