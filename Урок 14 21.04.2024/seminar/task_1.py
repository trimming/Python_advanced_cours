# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
import re


def remove_chars(text: str) -> str:
    letters = re.compile(r'[^a-zA-Z\s]')
    data = re.sub(letters, '', text).lower()
    return data


user_text = 'hsgsdjhag7575hhgjk hiadрорпврtdy'
a = remove_chars(user_text)
print(a)
