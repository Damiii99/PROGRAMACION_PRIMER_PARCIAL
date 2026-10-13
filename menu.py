from funciones import cargar_datos, crear_lista, mostrar_estudiantes, calcular_los_promedios, mostrar_promedio_estudiante, ordenamiento_mayor_promedio, mayor_promedio, buscar_por_legajo

def menu():

    cantidad = 30
    datos_cargados = False
    
    lista_legajos = crear_lista(cantidad)
    lista_nombres = crear_lista(cantidad)
    lista_generos = crear_lista(cantidad)
    primer_parcial = crear_lista(cantidad)
    segundo_parcial = crear_lista(cantidad)
    lista_promedios = crear_lista(cantidad)
    
    while True:
        print(" ")
        print("\t MENU DE DATOS DE ESTUDIANTES")
        print("1. Realizar la carga de datos de los estudiantes")
        print("2. Mostrar todos datos de los estudiantes")
        print("3. Promedio de cada estudiante")
        print("4. Motrar los datos de los estudiantes, ordenado por promedio")
        print("5. Mostrar el/los estudiante/s con mayor promedio")
        print("6. Buscar y mostrar todos los estudiantes por legajo")
        print("7. Salir del programa")
        print(" ")
        
        opciones = int(input("Elije una opcion: "))
        match opciones:
            case 1:
                cargar_datos(lista_legajos, lista_nombres, lista_generos, primer_parcial, segundo_parcial)
                datos_cargados = True
            case 2:
                if datos_cargados == False:
                    print("ERROR, datos de la lista no cargadas\n")
                else:
                    mostrar_estudiantes(lista_legajos, lista_nombres, lista_generos, primer_parcial, segundo_parcial)
            case 3:
                if datos_cargados == False:
                    print("ERROR, datos de la lista no cargadas\n")
                else:
                    calcular_los_promedios(primer_parcial, segundo_parcial, lista_promedios)
                    mostrar_promedio_estudiante(lista_legajos,lista_nombres,lista_generos,primer_parcial,segundo_parcial,lista_promedios)
            case 4:
                if datos_cargados == False:
                    print("ERROR, datos de la lista no cargadas\n")
                else:
                    ordenamiento_mayor_promedio(lista_promedios,lista_legajos,lista_nombres,lista_generos,primer_parcial,segundo_parcial,"DESC")
                    mostrar_estudiantes(lista_legajos, lista_nombres, lista_generos, primer_parcial, segundo_parcial)
            case 5:
                if datos_cargados == False:
                    print("ERROR, datos de la lista no cargadas\n")
                else:
                    mayor_promedio(lista_legajos, lista_nombres, lista_generos, primer_parcial, segundo_parcial, lista_promedios)
            case 6:
                if datos_cargados == False:
                    print("ERROR, datos de la lista no cargadas\n")
                else: 
                    buscar_por_legajo(lista_legajos, lista_nombres, lista_generos, primer_parcial, segundo_parcial)
            case 7:
                print("Saliendo del programa...")
                break
            case _:
                print("ERROR, opcion no encontrada.")


