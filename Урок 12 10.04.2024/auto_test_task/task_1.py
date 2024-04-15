import csv
from typing import Any


class Student:
    # name = Validate()
    # subjects = Validate()
    def __init__(self, name: str, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == self.name:
            if value.isalpha() and value.istitle():
                self.__dict__[name] = value
            else:
                print('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            self.__dict__[name] = value

    def __getattr__(self, item):
        return item

    def __str__(self):
        return f'Студент: {self.name}\nПредметы:'

    def load_subjects(self, file: Any) -> dict[str: tuple]:
        with open(file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f, dialect='excel-tab', )
            data = {}
            for line in csv_file:
                data[line[0]] = ()
            return data
    def add_grade(self, subject, grade):

if __name__ == '__main__':
    st1 = Student('Jhskd', 'subjects.csv')
    print(st1.subjects)
