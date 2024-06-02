#!/usr/bin/env python3

def join_lists(l1, l2):
    temp_joined = set(l1) | set(l2)
    joined = list(temp_joined)
    return joined
def match_lists(l1,l2):
    temp_matched = set(l1) & set(l2)
    matched = list(temp_matched)
    return matched
def diff_lists(l1,l2):
    temp_diffed = set(l1) ^ set(l2)
    diffed = list(temp_diffed)
    return diffed
if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('Join: ', join_lists(list1,list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))