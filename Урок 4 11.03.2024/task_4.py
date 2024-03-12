def bubble_sorted(user_list: list) -> list:
    for _ in range(0, len(user_list) - 1):
        for j in range(len(user_list) - 1):
            if user_list[j] > user_list[j + 1]:
                temp = user_list[j]
                user_list[j] = user_list[j + 1]
                user_list[j + 1] = temp

    return user_list


print(bubble_sorted([2, 10, 4, 6, 3]))
