def sum_list_nums(list_nums, a, b):
    if a > b and a > 0 > b:
        return sum(list_nums[a:b:-1])
    elif b < a < 0:
        return sum(list_nums[a:b:-1])
    else:
        return sum(list_nums[a:b])


print(sum_list_nums([2, 5, 2, 6, 8, 4], 2, 4))
