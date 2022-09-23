from collections import deque

# estructura de datos
# Listas
numeList = [1, 2, 3, 4, 5, 6]
namesList = ['A', 'B', 'C', 'D']
namesList2 = ['AA', 'BB', 'CC', 'DD']
print(numeList)
print(namesList)
print(namesList[0])

# mostrar en  intervalo
print(namesList[1:len(namesList)])

# sumar listas
sumList = namesList + namesList2
print(sumList)

# listas anidadas
a = [0, 2, 4, 6, 8]
b = [1, 3, 5, 7, 9]

list_anidada = [a, b]
print(list_anidada)
print(list_anidada[0])

# ordenando
print(sorted(sumList))

# ordenamiento inverso
print(sorted(sumList, reverse=True))

# Limpiar lista
sumList.clear()
print(sumList)

# Pilas
fruts = ['manzana', 'mango', 'pera', 'papaya', 'naranja']
print(fruts.pop())
print(fruts)
print(fruts.pop())
print(fruts)
print(fruts.pop(1))
print(fruts)

# deque
persons = deque(['juan', 'pedro', 'maria'])
print(persons)
persons.append('robert')
print(persons.popleft())
print(persons)
del persons[1]
print(persons)

# comprehension
# normal
cuadrados = []
for i in range(20):
    cuadrados.append(i ** 2)
print(cuadrados)

# comprehension
cuadradosC = [i ** 2 for i in range(20)]
print(cuadradosC)

# otro ejemplo
puntos = []

for i in range(5):
    for j in range(5):
        puntos.append((i, j))

print(puntos)

puntosC = [(x, y) for x in range(5) for y in range(5)]
print(puntosC)

# tuplas
t = 123, True, 'hola'
print(t)
print(type(t))

# accediendo a sus elementos
print(t[0])
print(t[2])

# tuplas no se pueden agregar mas datos

# tuplas anidadas
tupla = 456, t
print(tupla)
print(tupla[1][2])

# desectructuracion
x, y, z = t
print(x)
print(y)
print(z)

# conjuntos

a = {'toyota', 'nisan', 'honda'}
print(a)
a.add('hyundai')
print(a)
a.remove('honda')
print(a)

# operaciones con conjunto

m = {1, 2, 3, 4, 5}
n = {1, 4, 8}

# resta
print(m-n)
print(n-m)

# union
print(m | n)

# interseccion
print(m & n)

# diferencia simetrica
print(m ^ n)

# conjunto vacio
vacio = set()
print(type(vacio))


# Diccionarios
heroe1 = {
    'heroe': 'flash',
    'nombre':'barry',
    'edad': 25
}

print(heroe1)
print(type(heroe1))

# acceder al diccionario
print(heroe1['edad'])
print(heroe1.get('edad'))
print(list(heroe1.values()))
print(list(heroe1.keys()))

# agregar llaves
heroe1['poder'] = 'Velocidad'
print(heroe1)