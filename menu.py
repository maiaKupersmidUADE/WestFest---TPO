def opciones_menu():
    # Funcion que muestra las opciones del menu
    print("-" * 50)
    print("                 MENU DE CONTENIDOS")
    print("-" * 50)
    print("Seleccione una opcion:")
    print("1. Asignar / Modificar Line Up")
    print("2. Consultar Line Up")
    print("3. Buscar artista")
    print("4. Registrar asistencia")
    print("5. Modificar asistencia")
    print("6. Consultar informe de artista con mayor convocatoria")
    print("7. Consultar informe de asistencia total por dia")
    print("8. Consultar informe de top 3 de artistas con mayor convocatoria")
    print("9. Consultar informe de shows que superaron la capacidad")
    print("10. Consultar informe de top 3 de franjas horarias con mayor asistencia")
    print("11. Mostrar ranking de artistas")
    print("0. Salir")
    print("-" * 50)
    
def menu():
    opciones_menu()
    opcion = int(input("Opción: "))
    # Validar que la opcion elegida este dentro de los rangos permitidos
    while opcion < 0 or opcion > 11:
        print("Error, la opcion elegida debe estar entre 0 y 11")
        opciones_menu()
        opcion = int(input("Seleccione una opcion: "))
    return opcion

def main():
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            print()
            # funciones.asignarLineUp()
        elif opcion == 2:
            print()
            # funciones.consultarLineUp()
        elif opcion == 3:
            print()
            # funciones.buscarArtista()
        elif opcion == 4:    
            print()
            # funciones.registrarAsistencia()
        elif opcion == 5:
            print()
            # funciones.modificarAsistencia()
        elif opcion == 6:
            print()
            # funciones.consultarArtistaMayorConvocatoria()
        elif opcion == 7:
            print()
            # funciones.consultarAsistenciaTotalPorDia()
        elif opcion == 8:
            print()
            # funciones.consultarTop3ArtistasMayorConvocatoria()
        elif opcion == 9:
            print()
            # funciones.consultarShowsSobrepasaronCapacidad()
        elif opcion == 10:
            print()
            # funciones.consultarTop3FranjasHorariasMayorAsistencia()
        elif opcion == 11:
            print()
            # funciones.mostrarRankingArtistas()

main()