def calculate_awards(*lists) -> dict:
    employee_dict = {}
    for name, rate, percent in list(zip(*lists)):
        employee_dict[name] = rate + rate * float(percent.replace('%', '')) / 100
    return employee_dict


print(calculate_awards(['Ben', 'John'], [120_000, 125_000], ['10.5%', '11.0%']))
