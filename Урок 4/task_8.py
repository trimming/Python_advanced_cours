def change_name_var():
    names = 'Tehggh, Hhjkk, Fhgh'
    surname = 'Tehggh'
    lists = [[1, 2], [2, 5]]
    s = 45
    x = locals()
    for key, value in x.items():
        if key.endswith('s') and len(key) > 1:
            x[key] = None
            
    return x
print(change_name_var())
