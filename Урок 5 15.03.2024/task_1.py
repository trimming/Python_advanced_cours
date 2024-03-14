# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.


def create_dict(user_str: str) -> dict[int: int]:
    user_list = [int(i) for i in user_str.split('/')]
    a, b, c, *d = user_list
    return {b: a, c: tuple(d)}


user_dict = create_dict('45/67/2/78/8/9/10/21')
print(user_dict)
