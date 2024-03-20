from task_41 import questions
from random import choice

_dict_answers = {}


def play_puzzles(puzzles_data: dict[str, list[str]], count: int, tries: int) -> str:
    while len(puzzles_data) and count:
        puzzle = choice(list(puzzles_data))
        answers = puzzles_data.pop(puzzle)
        puzzle_count = questions(puzzle, answers, tries)
        _dict_answers[puzzle] = f'Отгадана с {puzzle_count} попытки' if puzzle_count else ' не отгадана'
        count -= 1


def print_answers():
    for puzzle, answer in _dict_answers.items():
        print(f'\nЗагадка: {puzzle}\n{answer}')


if __name__ == '__main__':
    puzzles = {
        'Ни лает, ни кусает, в дом не пускает?': ['замок', 'сигнализация'],
        'Висит груша, нельзя скушать?': ['лампочка', 'лампа'],
        'Зимой и летом одним цветом?': ['ель', 'ёлка']
    }
    play_puzzles(puzzles, 4, 3)
    print_answers()