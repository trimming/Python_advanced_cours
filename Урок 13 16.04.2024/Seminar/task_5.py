# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.
from task_4 import User
import json
from task_3 import *

class Company:
    _company = None
    _file_name = None

    def __new__(cls, name: str = None, db_file: str = 'user_list.json'):
        if cls._company is None:
            cls._company = super().__new__(cls)
            cls._company.name = name            
            cls._file_name = db_file
            cls._company.users_list = self._load_users()
            cls._company.loged_in = False
        return cls._company

    
    @classmethod
    def _load_users(self):
        users = set()
        with open(cls._file_name, 'r', encoding='utf-8') as json_file:
            user_data = json.load(json_file)
        for lvl, user in user_data.items():
            for u_id, name in user.items():
                users.add(User(name, u_id, lvl))
        return users

    def login(self, name: str, u_id: str):
        login_user = User(name, u_id, u_lvl:0)
        if login_user in self.users_list:
            for user in self.users_list:
                if user == login_user:
                    print('Авторизация прошла успешно!')
                    return user.lvl        
        raise AccessError(name, u_id)
        
        


a = Company('GB')
print(a.users_list)
            
# 1:29:00
