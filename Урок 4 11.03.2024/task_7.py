def test_companies(dict_companies):
    return all([sum(dict_companies[key]) > 0 for key in dict_companies.keys()])


print(test_companies({'DX': [100, 200, 300], 'TX': [200, 100, -500]}))
