# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

def create_dict(text: str) -> dict[str: int]:
    return {i: ord(i) for i in text}


text = 'jkhflahhff;akjkkhfj'
my_dict = create_dict(text)
print(my_dict)
