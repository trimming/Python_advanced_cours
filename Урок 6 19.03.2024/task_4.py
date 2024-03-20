'''Модуль загадка.'''


def answer_quest(quest: str, answers_list: list, count=3) -> int:
    print('Отгадайте загадку:\n')
    while count > 0:
        answer = input(f'"{quest}"\n')
        for i in answers_list:
            if i.lower() == answer:
                return count
        count -= 1
    return 0


def all_quests():
    quests_dict = {
        'Что лежит на дне океана?': ['спанч боб', ]
    }


if __name__ == '__main__':
    print(answer_quest('Кто там?', ['сто грамм', 'я', 'никто']))
