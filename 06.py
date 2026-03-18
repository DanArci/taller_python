'''
Pide cuántas horas estuvo un carro en un parqueadero.
Reglas:
---- primera hora = 5000
---- cada hora adicional = 3000
Muestra el total a pagar.
Practica: condicionales y operaciones
'''

from funciones import *

bienvenidoa("el estacionamiento de RIWI!")
totalHorasExtras = 0
tiempo = inputUsuario("Cuantas horas estuvo el auto: ","int", "Solo se admiten numeros enteros.")
if tiempo > 1:
    horasExtras = tiempo - 1 
    print(f"Usted estuvo {horasExtras} horas extras")
    totalHorasExtras = horasExtras * 3000
totalHoras = 5000 + totalHorasExtras
print(f"El total a pagar es de {totalHoras} pesos")