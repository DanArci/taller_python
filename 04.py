'''
El precio de la entrada cambia así:
---- niños menores de 12 → 8000
---- adultos de 12 a 59 → 12000
---- mayores de 60 → 9000
Pide la edad del cliente y muestra cuánto debe pagar.
Practica: condicionales.
'''
from funciones import *

bienvenidoa("el cine RIWI!")

edad = inputUsuario("Coloque su edad: ","int","Solo se permiten numeros enteros positivos")
if edad < 12:
    print("El cliente debe pagar 8.000 pesos por entrada")
elif edad >= 12 and edad <= 59:
    print("El cliente debe pagar 12.000 pesos por entrada")
else: 
    print("El cliente debe pagar 9.000 pesos por la entrada")