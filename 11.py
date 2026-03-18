'''
Una heladería quiere registrar varios clientes hasta que el usuario
decida salir.
Productos:
--- cono = 3000
--- vaso = 4000
--- banana split = 9000
Por cada cliente:
--- pedir producto
--- pedir cantidad
--- calcular total
Al final mostrar:
--- total vendido
--- cuántos clientes se atendieron
--- cuál producto se pidió más veces
Practica: ciclos, acumuladores, contadores.
'''

import os
from funciones import *

os.system('clear')
bienvenidoa('la heladeria RIWI!')

ventas = []
terminate = 0

while terminate == 0:
    opcion = inputUsuario('Que accion desea realizar?\n1. Atender nuevo cliente\n2. Salir y mostrar resumen del dia\n\n','int','Solo se aceptan numeros enteros positivos.')
    while opcion == 1:
        producto = inputUsuario('Cual es el producto que desea llevar?\n1. Cono         | 3.000 pesos\n2. Vaso         | 4.000 pesos\n3. Banana Split | 9.000 pesos\n', 'int', 'Solo se permiten numeros enteros positivos (1)(2)(3)')
        cantidad = inputUsuario(f'Que cantidad desea llevar: ','int','Solo se aceptan numeros enteros positivos ')

        if producto == 1:
            total = cantidad * 3000
        elif producto == 2:
            total = cantidad * 4000
        elif producto == 3:
            total = cantidad * 9000
        else: 
            os.system('clear')
            print('❌❌Coloque una opcion valida (1)(2)(3)❌❌')
            continue
        ventas.append((producto,total,cantidad))
        print('Resgistro exitoso✅')
        opcion = 0
    
    if opcion == 2:

        totalDelDia = 0
        numClientes = 0
        ventasCono = 0
        ventasVaso = 0
        ventasBanana = 0

        for venta in ventas:
            if venta[0] == 1:
                ventasCono = ventasCono + venta[2]
            elif venta[0] == 2:
                ventasVaso = ventasVaso + venta[2]
            elif venta[0] == 3:
                ventasBanana = ventasBanana + venta[2]
            totalDelDia = totalDelDia + venta[1]
            numClientes = numClientes + 1
        
        if ventasCono > ventasVaso and ventasCono > ventasBanana:
            productoMasVendido = "Cono"
            mayorVenta = ventasCono
        elif ventasCono < ventasBanana and ventasVaso < ventasBanana:
            productoMasVendido = "Banana Split"
            mayorVenta = ventasBanana
        elif ventasVaso > ventasCono and ventasVaso > ventasBanana:
            productoMasVendido = "Vaso"
            mayorVenta = ventasVaso
        elif ventasVaso == ventasCono and ventasVaso > ventasBanana:
            productoMasVendido = "Vaso y el Cono"
            mayorVenta = ventasVaso
        elif ventasVaso == ventasBanana and ventasVaso > ventasCono:
            productoMasVendido = "Vaso y el Banana Split"
            mayorVenta = ventasVaso
        else: 
            productoMasVendido = "Cono y el Banana Split"
            mayorVenta = ventasCono

        print(f'\nEl total de clientes atendidos en el dia fue de: {numClientes}')
        print(f'El total vendido en el dia fue de: {totalDelDia}')
        print(f'El producto mas vendido fue el {productoMasVendido} con {mayorVenta} ventas')
        terminate = 1 