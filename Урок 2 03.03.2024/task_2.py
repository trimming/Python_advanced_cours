import fractions

frac1 = "1/2"
frac2 = "1/3"

list1 = frac1.split('/')
list2 = frac2.split('/')
numerator1 = int(list1[0]) * int(list2[1]) + int(list1[1]) * int(list2[0])
numerator2 = int(list1[0]) * int(list2[0])
denominator = int(list1[1]) * int(list2[1])
print(f'Сумма дробей: {numerator1}/{denominator}')
print(f'Произведение дробей: {numerator2}/{denominator}')

summa = fractions.Fraction(numerator1, denominator)
print(f'Сумма дробей: {summa}')
mult = fractions.Fraction(numerator2, denominator)
print(f'Произведение дробей: {mult}')