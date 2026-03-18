import unicodedata

def eliminar_tildes(texto):
    texto_sin_tilde = unicodedata.normalize('NFD', texto)
    return "".join(c for c in texto_sin_tilde if not unicodedata.combining(c))

def inputUsuario(mensaje,tipo,mensajeError):

    #Variable que rompe el ciclo
    terminar = False
    while terminar == False:
        try:
            #Si se necesita un numero entero
            if tipo == "int":
                number = int(input(mensaje))
                if number <= 0:
                    print("Por favor coloque un numero mayor a 0.")
                    continue 
                terminar = True
                return number
            #Si se necesita un numero decimal
            elif tipo == "float":
                number = float(input(mensaje))
                if number <= 0:
                    print("Por favor coloque un numero mayor a 0.")
                    continue 
                terminar = True
                return number
            #Si se necesita una palabra o una frase
            elif tipo == "word" or tipo == "phrase":
                word = str(input(mensaje)).strip()
                #Verifica que en el caso que sea una palabra, que no se acepten espacios ni signos
                if tipo == "word":
                    terminar = 1
                    return word
                elif tipo == "phrase":
                    return word
                else:
                    raise ValueError
        #Se hace un print del parametro mensaje de error pasado a la funcion en el caso de que exista algun error al convertir los valores
        except ValueError:
            print(mensajeError)
            continue
        
        
def bienvenidoa(msg):
    print("-"*15, f"Bienvenido a {msg}", "-"*15)