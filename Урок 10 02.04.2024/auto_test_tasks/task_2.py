class LotteryGame:
    def __init__(self, list1: list[int], list2: list[int]):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        res = [i for i in self.list1 if i in self.list2]
        if len(res) > 0:
            print(f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {len(res)}')
        else:
            print('Совпадающих чисел нет.')


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 11, 14, 22, 17, 42, 8, 3]
lot = LotteryGame(list1, list2)
lot.compare_lists()
