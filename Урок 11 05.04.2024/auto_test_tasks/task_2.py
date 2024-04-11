class Archive:
    archive_number = None
    archive_text = None
    _instance = None    

    def __new__(cls, archive_number, archive_text, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            archive_text = []
            archive_number = []
        cls.archive_text.append(args[0])
        cls.archive_number.append(args[1])
        return cls._instance

    def __init__(self, text: str, number: float):
        self.text = text
        self.number = number


if __name__ == '__main__':
    rec_1 = Archive('Record 1', 45)
    rec_2 = Archive('Record 2', 45.34)
    rec_3 = Archive('Record 3', 5.05)
    print(rec_1.archive_text, rec_1.archive_number)
    print(rec_2.archive_text, rec_2.archive_number)
    print(rec_3.archive_text, rec_3.archive_number)
