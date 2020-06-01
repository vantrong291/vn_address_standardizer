import time

from .constants import ACRONYM_DICT


def acronym_execute(raw_address):
    # start = time.time()

    address = raw_address
    for item in ACRONYM_DICT:
        if item in raw_address:
            address = address.replace(item, ACRONYM_DICT[item])

    # end = time.time()
    # print('[{:.4f} s] Function acronym_execute {} executed'.format((end - start), raw_address))
    return address
