import csv
from typing import Any


class Student:
    """
        Класс, представляющий студента.

        Атрибуты:
        - name (str): ФИО студента
        - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

        Методы:
        - __init__(self, name, subjects_file): конструктор класса
        - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
        - __getattr__(self, name): получение значения атрибута
        - __str__(self): возвращает строковое представление студента
        - load_subjects(self, subjects_file): загрузка предметов из файла CSV
        - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
        - get_average_grade(self): возвращает средний балл по всем предметам
        - add_grade(self, subject, grade): добавление оценки по предмету
        - add_test_score(self, subject, test_score): добавление результата теста по предмету
        """
    def __init__(self, name: str, subjects_file):
        self.name = name
        self._load_subjects = self.load_subjects(subjects_file)
        self.subjects = {}

    def __setattr__(self, name, value):
        if name == self.name:
            val = True
            for n in value.split():
                if n.isalpha() and n.istitle():
                    continue
                else:
                    val = False
            if val:
                self.__dict__[name] = value
            else:
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            self.__dict__[name] = value

    def __getattr__(self, item):
        return item

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join([key for key in self.subjects.keys()])}'

    def load_subjects(self, file: Any):
        with open(file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                return line

    def add_grade(self, subject, grade):
        if subject in self._load_subjects:
            if type(grade) is int and 2 <= grade <= 5:
                if subject in self.subjects:
                    self.subjects[subject]['grade'].append(grade)
                else:
                    self.subjects[subject] = {'grade': [grade], 'test_score': []}
            else:
                raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def add_test_score(self, subject, test_score):
        if subject in self.subjects:
            if type(test_score) is int and 0 <= test_score <= 100:
                if subject in self.subjects:
                    self.subjects[subject]['test_score'].append(test_score)
                else:
                    self.subjects[subject] = {'test_score': [test_score], 'grade': []}
            else:
                raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_test_score(self, subject):
        if subject in self.subjects:
            return sum(self.subjects[subject]['test_score']) / len(self.subjects[subject]['test_score'])
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self):
        av_grade = 0
        count = 0
        for value in self.subjects.values():
            print(value['grade'])
            av_grade += sum(value['grade'])
            count += len(value['grade'])
        if count > 0:
            return av_grade / count
        else:
            return 0


if __name__ == '__main__':
    st1 = Student('Иван Иванович Иванов', 'subjects.csv')

    st1.add_grade('История', 3)
    st1.add_grade('Математика', 3)
    st1.add_grade('История', 5)
    st1.add_grade('Физика', 4)
    st1.add_grade('Физика', 2)
    st1.add_test_score("Математика", 85)
    st1.add_test_score("Математика", 60)
    st1.add_test_score("Физика", 90)
    avg = st1.get_average_test_score('Физика')
    avg_g = st1.get_average_grade()
    print(avg_g)
    print(st1.subjects)
    print(st1)
