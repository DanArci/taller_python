'''
Pide el precio de 6 productos
Al final indica cuántos cuestan más de 100000.
Practica: ciclo, contador, condicional.
'''

import os
from funciones import *

os.system('clear')
bienvenidoa("el contador de productos caros de RIWI!")
productosCaros = []
productosBaratos = []

for producto in range(6):
    productoComprado = [inputUsuario(f"Coloque el precio del producto #{producto+1}\n","float","Solo se aceptan numeros sin espacios ni signos.\n"), producto + 1]
    if productoComprado[0] > 100000:
        productosCaros.append(productoComprado)
    else:
        productosBaratos.append(productoComprado)
print("Los productos con precio menor que 100000 son:\n")
for producto in enumerate(productosCaros):
    print(f"Producto #{producto[1][1]}:  ", producto[1][0], "pesos.")
