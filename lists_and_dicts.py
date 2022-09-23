def run():
    my_list = [1, "hi", True, 4.5]
    my_dict = {"firstname": "harry", "lastname": "coa"}

    super_list = [
        {"firstname": "harry2", "lastname": "coa2"},
        {"firstname": "harry3", "lastname": "coa3"},
        {"firstname": "harry4", "lastname": "coa4"},
        my_list, my_dict
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "integer_nums": [-1, -2, 0, 1, 2],
        "float_nums": [1.7, 2.6, 3.9, 4.7, 5.99]

    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for x in super_list:
        print(x)


    for x in range(100):
        print(x*x)


if __name__ == '__main__':
    run()
