class Archive:
    archive_text = []
    archive_number = []

    def __new__(cls, *args):
        new_item = super().__new__(cls)
        cls.archive_number.append(args[1])
        cls.archive_text.append(args[0])
        new_item.archive_text = cls.archive_text.copy()
        new_item.archive_number = cls.archive_number.copy()
        return new_item

    def __init__(self, text: str, number: int | float):
        self.text = text
        self.number = number

    def __repr__(self):
        return f"Archive('{self.text}', '{self.number}')"

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'


if __name__ == '__main__':
    rec_1 = Archive('Record 1', 45)
    rec_2 = Archive('Record 2', 45.34)
    rec_3 = Archive('Record 3', 5.05)
    print(rec_1)
    print(rec_2)
    print(repr(rec_3))


from typing import Union

# class Archive:
#     _instance = None
#     archive_text = []
#     archive_number = []
#
#     def __new__(cls, text: str, number: Union[int, float]):
#         if cls._instance is None:
#             cls._instance = super(Archive, cls).__new__(cls)
#             cls.archive_text = []
#             cls.archive_number = []
#             return cls._instance
#         return cls._instance
#
#     def __init__(self, text: str, number: Union[int, float]):
#         self.text = text
#         self.number = number
#         Archive.archive_text.append(self.text)
#         Archive.archive_number.append(self.number)
#
#     def __repr__(self):
#         return f'Text is {self.text} and number is {self.number}. ' \
#                f'Also {Archive.archive_text} and {Archive.archive_number}'

