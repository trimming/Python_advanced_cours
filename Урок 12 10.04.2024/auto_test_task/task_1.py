
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
            val = True
            for n in value.split():
                if n.isalpha() and n.istitle(): 
                    continue
                else:
                    val = False
            if val:        
                self.__dict__[name] = value
            else:
                print('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            self.__dict__[name] = value

    def __getattr__(self, item):
        return item

    def __str__(self):
        return f'Студент: {self.name}\nПредметы:'

    def load_subjects(self, file: Any):
        with open(file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            data = {}
            for line in csv_file:
                data[line[0]] = [[], []]
            return data
        
    def add_grade(self, subject, grade):
        if subject in self.subjects:
            if type(grade) is int and 2 <= grade <= 5:
                self.subjects[subject][0].append(grade)
            else:
                print('Оценка должна быть целым числом от 2 до 5')
        else:
            print(f'Предмет {subject} не найден')

    def add_test_score(self, subject, test_score):
        if subject in self.subjects:
            if type(test_score) is int and 0 <= test_score <= 100:
                self.subjects[subject][1].append(test_score)
            else:
                print('Результат теста должен быть целым числом от 0 до 100')
        else:
            print(f'Предмет {subject} не найден')

    def get_average_test_score(self, subject):
        return sum(self.subjects[subject][1]) / len(self.subjects[subject][1])

    def get_average_grade(self):
        av_grade = 0
        count = 0
        for value in self.subjects.values():
            av_grade += sum(value[0])
            count += len(value[0])
        return av_grade / count
            
if __name__ == '__main__':
    st1 = Student('Иван Иванович Иванов', 'subjects.csv')
    print(st1)
    st1.add_grade('История', 3)
    st1.add_grade('Математика', 3)
    st1.add_grade('История', 5)
    st1.add_grade('Физика', 4)
    st1.add_grade('Физика', 2)
    st1.add_test_score("Математика", 85)
    st1.add_test_score("Математика", 60)
    avg = st1.get_average_test_score('Математика')
    avg_g = st1.get_average_grade()
    print(avg_g)
    print(st1.subjects)
