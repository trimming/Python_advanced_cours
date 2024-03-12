def create_list_unicode(text: str) -> list:
    list_unicode = [ord(i) for i in text]
    return sorted(list_unicode, key=lambda x: x, reverse=True)


print(create_list_unicode('jkhfss'))


# def text_unicode(text: str) -> list:
#     return sorted({ord(i) for i in text}, reverse=True)
#
#
# print(text_unicode('hjgsjkas'))