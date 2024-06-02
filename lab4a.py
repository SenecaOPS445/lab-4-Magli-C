#!/usr/bin/env python3

def join_sets(s1, s2):
    joined = s1 | s2
    return joined
def match_sets(s1,s2):
    matched = s1 & s2
    return matched
def diff_sets(s1,s2):
    diffed = s1 ^ s2
    return diffed
if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('Join: ', join_sets(set1,set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))
