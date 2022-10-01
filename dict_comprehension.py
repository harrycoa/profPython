import math


def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i ** 3

    print(my_dict)

    challenge = {x: x ** 3 for x in range(1, 101) if x % 3 != 0}
    print(challenge)

    root = {y: math.sqrt(y) for y in range(1, 1001)}
    print(root)


if __name__ == '__main__':
    run()
