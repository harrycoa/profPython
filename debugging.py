def divisors(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


def run():
    try:
        num = int(input("Ingresa un numero:  "))

        if num <= 0:
            raise ValueError("Debes ingresar un numero positivo")
        print(divisors(num))
        print("================================")
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == '__main__':
    run()
