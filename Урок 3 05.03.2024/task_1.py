from random import randint as ri

print(my_list := [ri(1, 10) for _ in range(15)])
# print(list(set(my_list)))

new_list = []
[new_list.append(item) for item in my_list if item not in new_list]
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)
print(new_list)