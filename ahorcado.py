import random
import os


def read():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        palabras = [line.strip('\n') for line in f]
    dict_palabras = {key: value for key, value in enumerate(palabras)}
    return dict_palabras


def normalize(str):
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))

    for a, b in replacements:
        str = str.replace(a, b).replace(a.upper(), b.upper())
    return str


def run():
    try:
        dict_palabras = read()
        palabra_adivinar = normalize(dict_palabras.get(random.randint(1, len(dict_palabras) + 1)))
        palabra_adivinando = len(palabra_adivinar)*"_"
        print(" Ahorcado =========================================> ")

        while palabra_adivinar != palabra_adivinando:
            print(palabra_adivinando)
            letra = normalize(input("Ingresa una letra: "))
            if letra in palabra_adivinar:
                palabra_adivinando = list(palabra_adivinando)
                for i, x in enumerate(palabra_adivinar):
                    if x == letra:
                        palabra_adivinando[i] = x
                palabra_adivinando = "".join(palabra_adivinando)
            os.system("cls")
        print(f'Ganaste =================================> {palabra_adivinando}')

        volver_jugar = int(input("Quieres jugar nuevamente ?: \n1. Si\n2, No\n"))
        if volver_jugar == 1:
            run()
        else:
            print("Adios")
    except ValueError:
        print("solo se ingresa letras")


if __name__ == '__main__':
    run()
