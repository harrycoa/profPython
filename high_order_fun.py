from functools import reduce


def run():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    # for simple
    list_imp = [i for i in my_list if i % 2 != 0]
    print(list_imp)

    # filter
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print(odd)

    # list comprehension
    my_list2 = [1, 2, 3, 4, 5, 6]
    squares = [i ** 2 for i in my_list2]
    print(squares)

    # map
    my_list3 = [1, 2, 3, 4, 5, 6]
    squares2 = list(map(lambda x: x**2, my_list3))
    print(squares2)

    # Example

    my_list4 = [2, 2, 2, 2, 2]
    all_multiplied = 1
    for i in my_list4:
        all_multiplied = all_multiplied * i
    print(all_multiplied)

    # reduce
    my_list5 = [2, 2, 2, 2, 2]
    all_multiplied2 = reduce(lambda a,b: a*b, my_list5)
    print(all_multiplied2)

if __name__ == '__main__':
    run()




