num = 245

# Введите ваше решение ниже
temp = num
HEX = 16
hex_num = ''
while temp > 0:
    rem = temp % HEX
    if rem > 9:
        match rem:
            case 10:
                hex_num = 'A' + hex_num
            case 11:
                hex_num = 'B' + hex_num
            case 12:
                hex_num = 'C' + hex_num
            case 13:
                hex_num = 'D' + hex_num
            case 14:
                hex_num = 'E' + hex_num
            case 15:
                hex_num = 'F' + hex_num
    else:
        hex_num = str(rem) + hex_num
    temp //= HEX
print(f'Шестнадцатеричное представление числа: {hex_num}')
print(f'Проверка результата: {hex(num)}')