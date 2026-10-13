#Funcion para crear la lista

def crear_lista(cantidad:int) -> list:
    '''
    Crea una lista y la cantidad de datos que habra en esa lista
    '''
    lista = []
    for i in range(cantidad):
        lista = [0] * cantidad #reemplazo del append
        
    return lista

#Funciones de validaciones

def solo_digitos(dato:str)-> bool:
    '''
    Retorna un True si es que el dato no esta vacio y contiene solo digitos enteros
    '''
    if dato == "":
        return False
    for c in dato:
        if not "0" <= c <= "9":
            return False
    return True
    
def validacion_legajo(dato:str)-> bool:
    if solo_digitos(dato):
        if int(dato) >= 1:
            return True
        else:
            return False
    else:
        return False

def validacion_alfabetica(texto:str) -> bool:
    '''
    Retorna un true si el texto contiene solo las letras (A-Z, a-z) y el espacio entre el nombre y apellido.
    Usando bandera y el codigo ASCII
    '''
    caracteres = False
    for caracter in texto:
        codigo = ord(caracter)
        if 65 <= codigo <= 90 or 97 <= codigo <= 122:
            caracteres = True
        elif codigo != 32:
            return False
    
    return caracteres

def validacion_genero(dato: str) -> bool:
    if dato == "F" or dato == "M" or dato == "X":
        return True
    else:
        return False

def validacion_nota(dato: str) -> bool:
    if solo_digitos(dato):
            if 1 <= int(dato) <= 10:
                return True
            else:
                return False
    else:
        return False

#funciones de lista

def legajo_estudiante() -> int:
    '''
    Pide el Legajo del estudiante, validandolo y delvolviendolo al numero tipo entero
    '''
    dato = (input("Ingrese el Legajo del estudiante: "))
    while not validacion_legajo(dato):
        print("Error, el legajo debe ser entero positivo")
        dato = (input("Ingrese el Legajo del estudiante: "))
    
    return int(dato)

def nombre_estudiante() -> str:
    '''
    Pide nombrer y apellido del estudiante, validando que sea de forma alfabetica
    '''
    dato = input("Ingrese nombre y apellido del estudiante: ")
    while not validacion_alfabetica(dato):
        print("ERROR, solo se permite caracteres alfabeticos")
        dato = input("Ingrese nombre y apellido del estudiante: ")
    
    return dato

def genero_estudiante() -> str:
    '''
    Pide el género del/la estudiante, validando que sea F, M o X, y lo retorna.
    '''
    dato = input("Ingrese el género (F/M/X): ")
    while not validacion_genero(dato):
        print("Error: ingrese F, M o X (en mayúscula).")
        dato = input("Ingrese el género (F/M/X): ")
    return dato

def nota_parcial(mensaje: str) -> int:
    '''
    Pide una nota del parcial, validando que sea un entero entre 1 y 10,
    y la retorna. El mensaje indica si se trata del primer o segundo parcial.
    '''
    dato = input(mensaje)
    while not validacion_nota(dato):
        print("Error: ingrese un entero entre 1 y 10.")
        dato = input(mensaje)
    return int(dato)

#Funciones del menu

def cargar_datos(lista_legajos:list, lista_nombres:list, lista_generos:list, primer_parcial:list, segundo_parcial:list) -> None:
    '''
    Carga de datos de cada una de los estudiantes con un for. 
    '''
    for i in range(len(lista_legajos)):
        print(f"\n---Estudiante {i+1} de {len(lista_legajos)}")
        lista_legajos[i] = legajo_estudiante()
        lista_nombres[i] = nombre_estudiante()
        lista_generos[i] = genero_estudiante()
        primer_parcial[i] = nota_parcial("Nota del primer parcial: ")
        segundo_parcial[i] = nota_parcial("Notas del Segundo parcial: ")
        
    print("Datos cargados correctamente")


def mostrar_estudiante(i:int, lista_legajos: list, lista_nombres: list, lista_generos: list, primer_parcial: list, segundo_parcial: list) -> None:
    '''
    Muestra todos los datos de un alumno de forma individual
    '''
    print(f"{lista_legajos[i]}\t{lista_nombres[i]}\t\t{lista_generos[i]}\t\t{primer_parcial[i]}\t\t{segundo_parcial[i]}")


def mostrar_estudiantes(lista_legajos:list, lista_nombres:list, lista_generos:list, primer_parcial:list, segundo_parcial:list) -> None:
    '''
    Pasa con for mostrando todos los datos de los alumnos en forma de informe, 
    llamando la funcion de mostra_estudiante para mostrar los datos de los estudiantes
    '''
    print("\t\t LISTA DE ESTUDIANTES")
    print("-"*50)
    print("LEGAJO\tNOMBRE APELLIDO\t\tGENERO\t\tNOTA PRIMER PARCIAL\t\tNOTA SEGUNDO PARCIAL")
    for i in range(len(lista_legajos)):
        mostrar_estudiante(i, lista_legajos, lista_nombres, lista_generos, primer_parcial, segundo_parcial)


def calcular_promedio(nota1:int, nota2:int) -> float:
    '''
    Calcula el promedio de las dos notas de un estudiante
    Lo retorna entre 1.00 y 10.00, redondeando a dos decimales
    '''
    suma = nota1 + nota2
    resultado = suma / 2
    return round(resultado, 2)


def calcular_los_promedios(primer_parcial:list, segundo_parcial:list, lista_promedios:list) -> None:
    '''
    Calcula el promedio de cada estudiante y lo guarda en lista_promedios,
    en la misma posicion, mostrando todos los datos incluyendo el promedio
    '''
    for i in range(len(primer_parcial)):
        lista_promedios[i] = calcular_promedio(primer_parcial[i], segundo_parcial[i])


def mostrar_promedio_estudiante(lista_legajos:list, lista_nombres:list, lista_genero:list, primer_parcial:list, segundo_parcial:list, lista_promedios:list)-> None:
    '''
    Muestra en la consola todos los datos, mas el promedio del estudiante
    '''
    print("\t\t PROMEDIO DE CADA ESTUDIANTE")
    print("LEGAJO\tNOMBRE APELLIDO\t\tGENERO\t\tNOTA 1\t\tNOTA 2\t\tPROMEDIO")
    for i in range(len(lista_legajos)):
        print(f"{lista_legajos[i]}\t{lista_nombres[i]}\t\t{lista_genero[i]}\t\t{primer_parcial[i]}\t\t{segundo_parcial[i]}\t\t{lista_promedios[i]:.2f}")


def ordenamiento_mayor_promedio(lista_promedios:list,lista_legajos:list, lista_nombres:list,lista_generos:list,primer_parcial:list,segundo_parcial:list, orden:str)-> None:
    '''
    Ordena toda las listas paralela de forrma descente, segun el promedio del estudiante.
    Funcion con ordamiento de burbuja de manera "ASC" ascendente y "DESC" descendente
    '''
    
    n = len(lista_promedios)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (lista_promedios[j] < lista_promedios[i]) and orden == "ASC":
                lista_promedios[i], lista_promedios[j] = lista_promedios[j], lista_promedios[i]  
                lista_legajos[i], lista_legajos[j] = lista_legajos[j], lista_legajos[i]
                lista_nombres[i], lista_nombres[j] = lista_nombres[j], lista_nombres[i]
                lista_generos[i], lista_generos[j] = lista_generos[j], lista_generos[i]
                primer_parcial[i], primer_parcial[j] = primer_parcial[j], primer_parcial[i]
                segundo_parcial[i], segundo_parcial[j] = segundo_parcial[j], segundo_parcial[i]
            elif (lista_promedios[j] > lista_promedios[i]) and orden == "DESC": 
                lista_promedios[i], lista_promedios[j] = lista_promedios[j], lista_promedios[i]  
                lista_legajos[i], lista_legajos[j] = lista_legajos[j], lista_legajos[i]
                lista_nombres[i], lista_nombres[j] = lista_nombres[j], lista_nombres[i]
                lista_generos[i], lista_generos[j] = lista_generos[j], lista_generos[i]
                primer_parcial[i], primer_parcial[j] = primer_parcial[j], primer_parcial[i]
                segundo_parcial[i], segundo_parcial[j] = segundo_parcial[j], segundo_parcial[i]


def mayor_promedio(lista_legajo:list, lista_nombres:list, lista_genero:list, primer_parcial:list, segundo_parcial:list, lista_promedios:list)-> None:
    '''
    Muestra el/los estudiante/s con mayor promedio.
    primero busca el maximo, luego con un contador, verifica cuantos estudiantes hay con mayor promedio
    y luego muestra si el/los estudiante/s con mayor promedio, mostrando los datos llamando a la funcion mostrar_estudiante
    '''
    mayor = lista_promedios[0]
    for i in range(len(lista_promedios)):
        if i == 0:
            mayor = lista_promedios[i]    
        if lista_promedios[i] > mayor:
            mayor = lista_promedios[i]
        
    contador = 0
    for i in range(len(lista_promedios)):
        if lista_promedios[i] == mayor:
            contador += 1
            
    if contador == 1:
        print(f"\nEl estudiante con mayor promedio ({mayor:.2f}) es:")
    else:
        print(f"\nHay {contador} estudiantes con el mayor promedio ({mayor:.2f})")
    
    for i in range(len(lista_promedios)):
        if lista_promedios[i] == mayor:
            print(" ")
            print("LEGAJO\tNOMBRE APELLIDO\t\tGENERO\t\tNOTA PRIMER PARCIAL\t\tNOTA SEGUNDO PARCIAL")
            mostrar_estudiante(i, lista_legajo, lista_nombres, lista_genero, primer_parcial, segundo_parcial)
            

def buscar_legajo(legajo:int, lista_legajo:list) -> int:
    '''
    Busca el legajo del estudiante en lista_legajo
    Retornado la posicion donde se encuetra, o queda en -1 si no lo encuentra
    '''
    posicion = -1
    for i in range(len(lista_legajo)):
        if lista_legajo[i] == legajo:
            posicion = i
    
    return posicion


def buscar_por_legajo(lista_legajo:list, lista_nombres:list, lista_generos:list, primer_parcial:list, segundo_parcial:list) -> None:
    '''
    Esta funcion pide el legajo, lo busca y muestra todo los datos de un estudiante por legajo 
    utilizando la funcion mostrar_estudiante.
    
    Si no existe el estudiante con ese legajo, informa que no se encontro.
    '''
    
    dato = input("Ingrese el legajo a buscar: ")
    while not validacion_legajo(dato):
        print("ERROR, el legajo debe ser entero positivo")
        dato = input("Ingrese el legajo a buscar: ")
    legajo = int(dato)
    
    posicion = buscar_legajo(legajo, lista_legajo)
    
    if posicion != -1:
        print("\n\tEstudiante encontrado:")
        print("LEGAJO\tNOMBRE APELLIDO\t\tGENERO\t\tNOTA PRIMER PARCIAL\t\tNOTA SEGUNDO PARCIAL")
        mostrar_estudiante(posicion, lista_legajo, lista_nombres, lista_generos, primer_parcial, segundo_parcial)
    
    else:
        print(f"No se encontro ningun estudiante con el legajo {legajo}.")