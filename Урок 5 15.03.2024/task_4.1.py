gen = (i for i in range(0, 101, 2) if i % 2 == 0 and (i % 10 + i // 10) != 8)
for i in gen:
    print(i, end=' ')

# gen = (i for i in range(0, 101, 2) if sum(map(int, list(str(i)))) != 8)
# for i in gen:
#     print(i, end=' ')