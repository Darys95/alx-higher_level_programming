#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_lst = my_list.copy()

    for i in range(0, len(new_lst)):
        if new_lst[i] == search:
            new_lst[i] = replace

    return new_lst
