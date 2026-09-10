import funciones

def opciones_menu():
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
    print("0. Salir")
    print("-" * 50)
    
def menu():    
    while True:
        opciones_menu()
        try:
            opcion = int(input("Opcion: "))
            if opcion >= 0 and opcion <= 10:
                break
            else:
                print("Error, la opción elegida debe estar entre 0 y 10.")
        except ValueError:
            print("Error, debe ingresar un número.")
    return opcion

def main():
    franjas = [("F01", "Mediodia"), ("F02", "Tarde"), ("F03", "Noche")]
    escenarios = [("E01", "Main Stage"), ("E02", "Electronic Arena"), ("E03", "Mata Club")]
    artistas = [("A01", "Lady Gagá"), ("A02", "50 pesos"), ("A03", "Me robaron entre 5"), ("A04", "Miley Ciruja"), ("A05", "21 pilotos de Ezeiza"), 
        ("A06", "Los kioskeros"), ("A07", "El finde"), ("A08", "Caño del Oeste"), ("A09", "Red Hot Chori Peppers"), ("A10", "Paco Odioso"), ("A11", "Ariana Chiquita"),
        ("A12", "Conejo Malo"),]

    capacidadEscenario = 1000
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
    asistencia_sabado = [[-1 if lineup_sabado[i][j] != "" else -2 for j in range(len(franjas))] for i in range(len(escenarios))]
    asistencia_domingo = [[-1 if lineup_domingo[i][j] != "" else -2 for j in range(len(franjas))] for i in range(len(escenarios))]

    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            funciones.asignarLineUp(artistas, lineup_sabado, lineup_domingo, escenarios, franjas)
        elif opcion == 2:
            funciones.consultarLineUp(lineup_sabado, lineup_domingo, escenarios, artistas, franjas)
        elif opcion == 3:
            codArtista = input("Codigo de Artista a buscar: ").upper()
            indice = funciones.obtenerIndex(artistas, codArtista, 0)
            if indice != None:
                print(f"Artista encontrado: {artistas[indice][1]}")
            else:
                print("El artista que busca no existe o se ingreso mal el codigo")
        elif opcion == 4:    
            funciones.registrarAsistencia(lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, escenarios, franjas, capacidadEscenario)
        elif opcion == 5:
            funciones.modificarAsistencia(lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, escenarios, franjas, capacidadEscenario)
        elif opcion == 6:
            print()
            # funciones.consultarArtistaMayorConvocatoria()
        elif opcion == 7:
            totalS = funciones.obtenerTotal(asistencia_sabado)
            totalD = funciones.obtenerTotal(asistencia_domingo)
            print(f"Asistencia total del sabado: {totalS}")
            print(f"Asistencia total del domingo: {totalD}")
        elif opcion == 8:
            print()
            # funciones.consultarTop3ArtistasMayorConvocatoria()
        elif opcion == 9:
            print()
            # funciones.consultarShowsSobrepasaronCapacidad()
        elif opcion == 10:
            print()
            # funciones.consultarTop3FranjasHorariasMayorAsistencia()
        opcion = menu()
    print("Gracias por usar nuestro sistema, hasta la proxima!")

main()