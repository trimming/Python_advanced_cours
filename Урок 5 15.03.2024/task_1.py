# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.


def create_dict(user_str: str) -> dict[int: int]:
    user_list = [int(i) for i in user_str.split('/')]
    a, b, c, *d = user_list
    return {b: a, c: tuple(d)}


# user_dict = create_dict('45/67/2/78/8/9/10/21')
# print(user_dict)
#
# data = '3/45/456/567/56/756/7567/567657/57'
#
# value_1, key_1, key_2, value_2 = map(int, data.split('/'))
#
# print(my_dict := {key_1: value_1, key_2: value_2})

