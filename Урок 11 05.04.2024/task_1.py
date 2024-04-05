import time
import datetime
class MyString(str):
    def __new__(cls, string,author=None):
        data = super().__new__(cls,string)
        data.author = author
        data.time = time.time()
        data.time_new = datetime.datetime.now()
        return data

my_string = MyString('Рок н ролл',author='Stoun')

print(my_string)
print(my_string.author)
print(my_string.time)
print(my_string.time_new)