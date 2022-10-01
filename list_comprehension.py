def run():
    squares = []
    for i in range(1, 101):
        if (i % 3) != 0:
            squares.append(i ** 2)

    print(squares)

    # Listcomprehension
    # [element for element in iterable if condition]
    multi = [i ** 2 for i in range(1, 101) if (i % 3) != 0]
    print(multi)

    reto = [j for j in range(1, 100000) if (j % 4) == 0 and (j % 6) == 0 and (j % 9) == 0]
    print(reto)

    reta = {x: x ** 3 for x in range(1, 101)}
    print(reta)


if __name__ == '__main__':
    run()
