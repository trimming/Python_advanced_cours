# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.


def create_dict(text: str):
    return {i: ord(i) for i in text}


text = 'jkhflahhff;akjkkhfj'
my_dict = create_dict(text)
print(my_dict)
COUNT = 5
dict_iter = iter(my_dict.items())
for i in range(COUNT):
    print(next(dict_iter))
          
