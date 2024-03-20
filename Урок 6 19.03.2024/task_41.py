
def questions(question: str, answers: list[str], tries: int) -> int:
    print(question)
    for user_tries in range(1, tries + 1):
        user_answer = input('Ваш вариант ответа: ')
        if user_answer.lower() in list(map(lambda x: x.lower(), answers)):
            return user_tries
        else:
            print(f"Ответ неверный! Осталось еще {tries - user_tries} попыток")
    return 0
