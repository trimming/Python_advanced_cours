def calculate_awards(*lists) -> dict:
    employee_dict = {}
    for name, rate, percent in list(zip(*lists)):
        employee_dict[name] = rate + rate * float(percent.replace('%', '')) / 100
    return employee_dict


print(calculate_awards(['Ben', 'Tom'], [120_000, 125_000], ['10.0%', '12.5%']))


# def prizes(names: list, moneys: list, bonuses: list) -> dict:
#     return {nam: money * float(bonus[:-1]) * 0.01 for nam, money, bonus in zip(names, moneys, bonuses)}