# my_tuple = (12, 12.2, 'fire', (23, 45), [6, 7, 8], 8, 9.6, 'zero')
# my_dict = dict()
# for i in my_tuple:
#     my_dict[type(i)] = list()
# # print(my_dict)
# for key,value in my_dict.items():
#     for i in my_tuple:
#         if type(i) == key:
#             value.append(i)
# print(my_dict)

my_tuple = (1, 'hello', 3.14, True, [1, 2, 3], 2, {'key': 'value'}, 3, False, 'строка')

result = {}

for item in my_tuple:
    if type(item) in result:
        result[type(item)].append(item)
    else:
        result[type(item)] = [item]

print(result)