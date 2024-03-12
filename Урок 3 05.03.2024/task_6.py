# user_line = input('Введите строку текста: \n')
# res = user_line.split()
# res.sort()
# num = 1
# lenth = len(max(res, key=lambda j: len(j)))
#
# for i in res:
#     print(f'{num}. {i:>{lenth}}')
#     num += 1

data_text = 'sdfdsgdfh dfghdf hgdfghfgh fghgfh fgh zfghfgh fghfg hgfhf fghfghfghfhfgh'
data_text = data_text.split()
max_len = len(max(data_text, key=len))

for i, item in enumerate(sorted(data_text), 1):
    print(f'{i}. {item:>{max_len}}')