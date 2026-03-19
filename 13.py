'''
Registrar varios pedidos en una cafetería hasta que el usuario escriba
“salir”.
Productos:
--- café = 4000
--- capuchino = 7000
--- pastel = 6000
Reglas:
--- si la compra supera 20000, aplicar 10% de descuento
--- si no, cobrar normal
Mostrar total por cliente y al final total acumulado del día.
Practica: menú simple, ciclos, descuentos.
'''

from funciones import *
import os

os.system('clear')
bienvenidoa('la Cafeteria RIWI!')
opcion = 1
terminate = 0
movimientos = []
while opcion == 1:
    opcion = inputUsuario('Coloque la accion que desea realizar\n1. Nueva venta\n2. Terminar y mostrar resumen del dia\n','int','❌❌Elija una opcion valida❌❌: (1)(2)')
    if opcion == 1:
        carrito = []
        terminate = 0
        while terminate == 0:
            producto = inputUsuario('Que producto va a llervar?\n1. café = 4000\n2. capuchino = 7000\n3. pastel = 6000\n4. Terminar y salir\n','int','Coloque una opcion valida: (1)(2)(3)(4)')
            if producto == 4:
                terminate = 1
                producto = 0
                continue
            elif producto > 4:
                print('Coloque una opcion valida: (1)(2)(3)(4)')
                continue
            carrito.append(producto)
            print('\nRegistro exitoso\n')
        if producto != 4:
            movimientos.append(carrito)
        continue
    elif opcion == 2:
        os.system('clear')
        totalDelDia = 0
        x = 0
        for ventas in movimientos:
            x = x + 1
            total = 0
            print(ventas)
            for productos in enumerate(ventas):
                if ventas[productos[0]] == 1:
                    total = total + 4000
                elif ventas[productos[0]] == 2:
                    total = total + 7000
                elif ventas[productos[0]] == 3:
                    total = total + 6000
                if total > 20000:
                    total = total * 0.9
            totalDelDia = totalDelDia + total
            print(f"El Cliente #{x} pago un total de:\n{total}")
        print(f'El total recaudado en el dia fue de: {totalDelDia}')
    else:
        os.system('clear')
        print('❌❌Coloque una opcion valida❌❌')
        opcion = 1
        continue