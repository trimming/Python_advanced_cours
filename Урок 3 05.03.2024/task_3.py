my_list = [2, 6, 2, 8, 9, 6, 2]
for i in my_list:
    if my_list.count(i) > 1:
        while my_list.count(i) > 0:
            my_list.remove(i)
print(my_list)