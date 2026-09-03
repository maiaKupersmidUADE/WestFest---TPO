import funciones

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
    franjas = [("F01", "Mediodia"), ("F02", "Tarde"), ("F03", "Noche")]
    escenarios = [("E01", "Main Stage"), ("E02", "Electronic Arena"), ("E03", "Mata Club")]
    artistas = [("A01", "Lady Gagá"), ("A02", "50 pesos"), ("A03", "Me robaron entre 5"), ("A04", "Miley Ciruja"), ("A05", "21 pilotos de Ezeiza"), 
        ("A06", "Los kioskeros"), ("A07", "El finde"), ("A08", "Caño del Oeste"), ("A09", "Red Hot Chori Peppers"), ("A10", "Paco Odioso"), ("A11", "Ariana Chiquita"),
        ("A12", "Conejo Malo"), ("A12", "")]

    lineup_sabado = [
        ["A01", "A02", "A03"],
        ["A05", "A06", "A07"],
        ["A09", "A10", ""]
    ]

    lineup_domingo = [
        ["A10", "A09", "A08"],
        ["A06", "A05", "A04"],
        ["A02", "A01", ""]
    ]

    # HECHAS POR COMPRENSION
    asistencia_sabado = [[-1 for j in range(len(franjas))] for i in range(len(escenarios))]
    asistencia_domingo = [[-1 for j in range(len(franjas))] for i in range(len(escenarios))]

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
            funciones.buscarArtista(artistas)
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
        opcion = menu()

main()