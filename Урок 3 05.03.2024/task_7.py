# user_line = input('Введите строку: \n')
# user_dict = {}
# for i in user_line:
#     if i in user_dict:
#         user_dict[i] += 1
#     else:
#         user_dict[i] = 1
# print(user_dict)

data_text = input('Введите строку:\n')

result = {}
# for item in set(data_text):
#     result[item] = data_text.count(item)
# print(result)

for item in data_text:
    result[item] = result.get(item, 0) + 1
print(result)