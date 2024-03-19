def answer_quest(quest: str, answers: list, count=3):
    print('Отгадай загадку:\n')
    answer_count = 1
    while count > 0:
        count -= 1
        user_answer = input(f'"{quest}"\n')
        for i in answers:
            if user_answer == i:
                return answer_count
            else:
                answer_count += 1
    else:
        return 0


def quests_dict():
    quests = {
        'Кто там?': ['я', 'никто', 'сто грамм'],
        'Зимой и летом одним цветом?':['ель', 'Ёлка', 'сосна']
        }
    for key, value in quests.items():
        print(key, answer_quest(key, value))
        gen_result(key, answer_quest(key, value))

def gen_result(quest: str, answer_count: int):
    _result = {}
    _result.update([(quest, answer_count)])
    return _result


def print_result():
    return quests_dict()


print(print_result())
