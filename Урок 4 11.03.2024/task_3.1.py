def create_dict_unicode(text: str):
    text_list = [int(i) for i in text.split()]
    text_list.sort()
    dict_unicode = {}
    for i in text_list:
        dict_unicode[chr(i)] = i
    return dict_unicode


print(create_dict_unicode('45 78'))
