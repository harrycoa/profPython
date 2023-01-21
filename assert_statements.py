def divisors(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


def run():
    num = input("Ingresa un numero:  ")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un numero entero positivo"
    print(divisors(int(num)))


if __name__ == '__main__':
    run()
