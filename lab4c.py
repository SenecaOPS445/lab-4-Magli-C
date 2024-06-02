#!/usr/bin/env python3


# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']


def create_dictionary(key_list, value_list):
    index = 0
    created_dict = {}
    while index < len(key_list):
        values = value_list[index]
        created_dict[key_list[index]] = values
        index += 1
    return created_dict

def shared_values(dict1, dict2):
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    shared = set1 & set2
    return shared

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)