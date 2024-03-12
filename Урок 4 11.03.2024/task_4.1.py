def bubble_sort(my_list: list) -> list:
    for _ in range(len(my_list)):
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i +1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
    return my_list


print(bubble_sort([6, 7, 2, 45, 1, 0]))