'''
En una cafetería venden:
---- café = 4000
---- té = 3500
---- jugo = 5000
Pide al usuario qué bebida quiere y cuántas unidades desea comprar.
Luego muestra el total a pagar.
Practica: condicionales, variables, multiplicación
'''

from funciones import *

bienvenidoa("la cafeteria RIWI!")

opcion = 1
carrito = 0
carrito_bebidas = []
bebida = 1
while opcion == 1:
    opcion = inputUsuario("Que accion desea hacer?\n1. Agregar una bebida al carrito\n2. Ver total y salir\n\n", "int", "Coloque una opcion valida: (1)(2)")
    if opcion == 1:
        while bebida < 4:
            bebida = inputUsuario("Que bebida quiere llevar?\n1. café = 4000\n2. té = 3500\n3. jugo = 5000\n\n", "int", "Coloque una opcion valida: (1)(2)(3)")
            if bebida == 1:
                carrito = carrito + 4000 
                bebida = "café"
            elif bebida == 2:
                carrito = carrito + 3500
                bebida = "té"
            elif bebida == 3:
                carrito = carrito + 5000 
                bebida = "jugo"
            else: 
                print("Coloque una opcion valida: (1)(2)(3)\n")
                bebida = 1
                continue
            carrito_bebidas.append(bebida)
            break
    elif opcion == 2:
        print("Usted lleva las siguientes bebidas:\n")
        for bebida in enumerate(carrito_bebidas):
            print(carrito_bebidas[bebida[0]])
        print(f"\nPor un total de: {carrito} pesos")
        break
    else:
        print("Coloque una opcion valida: (1)(2)\n")
        opcion = 1
