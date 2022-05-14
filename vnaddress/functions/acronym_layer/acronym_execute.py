import time

from .constants import ACRONYM_DICT

def acronym_execute_raw_address(raw_address):
    start = time.time()

    address = raw_address
    for item in ACRONYM_DICT:
        item_lower = item.lower()
        if item in raw_address:
            address = address.replace(item, ACRONYM_DICT[item])
        elif item_lower in raw_address:
            address = address.replace(item_lower, ACRONYM_DICT[item])

    end = time.time()
    # print('[{:.4f} s] Function acronym_execute_raw_address {} executed'.format((end - start), raw_address))

    return address

def acronym_execute_list_address(list_address):
    start = time.time()

    result = []
    for address_item in list_address:
        address = address_item
        for item in ACRONYM_DICT:
            item_lower = item.lower()
            if item_lower in address_item:
                address = address_item.replace(item_lower, ACRONYM_DICT[item])
        result.append(address)

    end = time.time()
    # print('[{:.4f} s] Function acronym_execute_list_address {} executed'.format((end - start), list_address))

    return result
