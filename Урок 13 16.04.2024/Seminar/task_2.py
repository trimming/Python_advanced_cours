# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_key(user_dict, key, def_val=None):
    try:
        return user_dict[key]
    except KeyError:
        user_dict[key] = def_val
        return def_val
    finally:
        print(user_dict)


if __name__ == '__main__':
    val = get_key({1: 'one', 2: 'two'}, 3, 'three')
    print(val)