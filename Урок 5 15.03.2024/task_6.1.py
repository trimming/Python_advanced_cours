# for i in range(2, 11):
#     for j in range(2, 6):
#         print(f'{j} x {i} = {j + i}', end='\t')
#     print()
# for i in range(2, 11):
#     for j in range(6, 10):
#         print(f'{j} x {i} = {j + i}', end='\t')

for i in range(2, 10, 4):
    if i == 6:
        print('\n')
    for j in range(1, 10):
        for k in range(i, i+4):
            if k < 10:
                print(f"{k} x {j} = {k * j:2} ", end="\t\t\t")
        print('\n')

gen = (for i in range(2, 6))

print('\n\n'.join(['\n'.join(['\t\t'.join([f'{x:^3}x{y:^3}= {x*y:^3}' for x in range(2+k,6+k)]) for y in range(2,11)]) for k in (0,4)]))