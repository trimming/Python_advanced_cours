# Задание №6
# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

from company import *
import pytest
from user import *


@pytest.fixture()
def company():
    return Company('Adidas')


@pytest.fixture()
def user_add():
    return 'Яна', '4587'


@pytest.fixture()
def new_user_17000():
    return 'Василий', '17000', 0

@pytest.fixture()
def new_user_17():
    return 'Василий', '17', 7

def test_login_error(company):
    name = 'Василий'
    user_id = '12'
    msg_error = f'Ошибка приложения!'
    with pytest.raises(MyAccessError, match=msg_error):
        company.login(name, user_id)


def test_new_user_error(company, user_add, new_user_17000):
    with pytest.raises(LevelError):
        company.login(*user_add)
        company.new_user(*new_user_17000)


def test_id_error(company, user_add, new_user_17):

    with pytest.raises(IdError):
        company.login(*user_add)
        company.new_user(*new_user_17)


# def test_login(company, user_add):
#     assert company.login(*user_add) == '4587'

if __name__ == '__main__':
    pytest.main(['-v'])
