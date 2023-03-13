
def inicio():
    if (algoritmo == 1):
        binaria(numeroIngresado)
    elif (algoritmo == 2):
        exhautiva(numeroIngresado)
    elif (algoritmo == 3):
        aproximacion(numeroIngresado)
    else: 
        print(f'No ingresastre una respuesta valida')

def binaria(numero):
    objetivo = numero
    epsilon = 0.1
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def exhautiva(numero):
    objetivo = numero
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


def aproximacion(numero):
    objetivo = numero
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')
        
numeroIngresado = int(input('Escoge un entero: '))
algoritmo = int(input(
    f'Escoge un algoritmo para encontrar la raiz cuadrada: \n1_ Busquesa Binaria: \n2_ Busqueda Exhaustiva: \n3_ Busquesa Aproximada: \n Tu respuesta: '))


inicio()
input()