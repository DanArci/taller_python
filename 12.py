'''
Registrar 5 personas en un gimnasio.
Por cada una pedir:
--- nombre
--- días asistidos en la semana
--- minutos promedio entrenados por día

Clasificar:
--- menos de 3 días → bajo compromiso
--- 3 a 4 días → compromiso medio
--- 5 o más → compromiso alto

Al final mostrar cuántas personas quedaron en cada categoría.
Practica: ciclos, contadores, condicionales.
'''
from funciones import *
import os

os.system('clear')

bienvenidoa('el Gimnasio RIWI!')
personas = []
persona = {
    'nombre' : '',
    'asistencia' : '',
    'minPromedio' : ''
}
for i in range(5):
    persona['nombre'] =  inputUsuario(f'Coloque el nombre de la persona #{i+1}: ','word', 'Coloque solo 1 palabra sin signos').strip().upper()
    persona['asistencia'] = inputUsuario('Coloque la cantidad de dias que asistio la persona en la semana: ','int','solo se permiten numeros enteros positivos.')
    persona['minPromedio'] = inputUsuario('Coloque la cantidad de minutos promedio entrenados por dia: ','int','Solo se permiten numero enteros positivos')
    personas.append(persona.copy())

bajoCompromiso = 0
medioCompromiso = 0
altoCompromiso = 0

for i in range(5):
    valores = list(personas[i].values())
    if valores[1] < 3:
        print(f'La persona #{i+1} tiene un bajo compromiso')
        bajoCompromiso = bajoCompromiso + 1
    elif valores[1] >= 3 and valores[1] <= 4:
        print(f'La persona #{i+1} tiene un compromiso medio')
        medioCompromiso = medioCompromiso + 1
    else:
        print(f'La persona #{i+1} tiene un compromiso alto')
        altoCompromiso = altoCompromiso + 1

print(f'Hubo {bajoCompromiso} personas con bajo compromiso\nHubo {medioCompromiso} personas con medio compromiso\nHubo {altoCompromiso} personas con alto compromiso')