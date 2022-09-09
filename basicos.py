# Comentarios
# Condicionales
number = int(input('ingrese num: '))
if type(number % 2) == 0:
    print(f'el numero {number} es par ')
else:
    print(f'el numero {number} es impar ')

# bucles
# for
for i in range(10):
    print(i * 2)

# while
#while number < 10 or number > 2:
#    print("detach")

# break
# 1000 primeros numero primos:
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            print(f'{i} no es primo')
            break
    else:
        print(f'{i} es primo')

#continue
for i in range(1, 30):
    if i % 6 == 0:
        print(f'{i} es divisible por 3, 2 , 6')
        continue
    if i % 2 == 0:
        print(f'{i} es divisible por 2')

    if i % 3 == 0:
        print(f'{i} es divisible por 3')

