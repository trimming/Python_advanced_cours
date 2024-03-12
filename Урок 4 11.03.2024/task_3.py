from typing import List, Dict


def create_dict_unicode(text: str) -> dict[str, int]:
    list_unicode = [int(i) for i in text.split()]
    list_unicode.sort()
    dict_unicode = {}
    for i in list_unicode:
        dict_unicode[chr(int(i))] = int(i)
    return dict_unicode


print(create_dict_unicode('231 42'))

# def uni_dict(some_str: str) -> dict[str, int]:
#     min_num, max_num = sorted(map(int, some_str.split()))
#     return {chr(i): i for i in range(min_num, max_num + 1)}
