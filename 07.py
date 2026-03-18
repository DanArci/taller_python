'''
Pide la hora de llegada de un cliente en formato entero de 0 a 23.
Mostrar:
---mañana si está entre 6 y 11
---tarde si está entre 12 y 17
---noche si está entre 18 y 22
fuera de horario en cualquier otro caso
Practica: rangos con condicionales.
'''

import os
from funciones import *

os.system('clear')
bienvenidoa("el control de llegada de clientes de RIWI!")
llegada = inputUsuario("A que hora llego el cliente?\n(Recuerde colocar la hora como numero entero en formato de 0 a 23)\n\n","int","Solo se permiten numeros enteros.")
if llegada >= 6 and llegada <= 11:
    print("Esta en el horario de Mañana")
elif llegada >= 12 and llegada <= 17:
    print("Esta en el horario de Tarde")
elif llegada >= 18 and llegada <= 22:
    print("Esta en el horario de Noche")
else:
    print("Esta fuera del horario")