import funciones
import archivos

def opciones_menu():
    print("-" * 50)
    print(" " * 16, "MENU DE CONTENIDOS")
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
    opciones_menu()
    opcion = int(input("Opcion: "))

    while opcion < 0 or opcion > 10:
        print()
        print("Error, la opción elegida debe estar entre 0 y 10.")
        print()
        opciones_menu()
        opcion = int(input("Opcion: "))
        
    return opcion

def main():

    config = archivos.cargarConfiguracion()
    if config is None:
        print("El programa se cerrará.")
        return

    dicArtistas, dicEscenarios, dicFranjas = funciones.crearDiccionariosAuxiliares(config)
    lineup_sabado, lineup_domingo = archivos.cargarLineUp(dicArtistas, dicEscenarios, dicFranjas)
    asistencia_sabado, asistencia_domingo = archivos.cargarAsistencia(dicEscenarios, dicFranjas)

    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            funciones.asignarLineUp(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
        elif opcion == 2:
            funciones.consultarLineUp(lineup_sabado, lineup_domingo, dicEscenarios, artistas, dicFranjas)
        elif opcion == 3:
            codArtista = input("Codigo de Artista a buscar: ").upper()
            funciones.buscarArtista(dicArtistas, codArtista, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
        elif opcion == 4:    
            funciones.registrarAsistencia(lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas, capacidadEscenario)
        elif opcion == 5:
            funciones.modificarAsistencia(lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas, capacidadEscenario)
        elif opcion == 6:
            funciones.consultarArtistaMayorConvocatoria(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo)
        elif opcion == 7:
            totalS = funciones.obtenerTotal(asistencia_sabado)
            totalD = funciones.obtenerTotal(asistencia_domingo)
            print(f"Asistencia total del sabado: {totalS}")
            print(f"Asistencia total del domingo: {totalD}")
        elif opcion == 8:
            funciones.consultarTop3ArtistasMayorConvocatoria(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo)
        elif opcion == 9:
            funciones.consultarShowsSobrepasaronCapacidad(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas, capacidadEscenario)
        elif opcion == 10:
            funciones.consultarTop3FranjasHorariasMayorAsistencia(asistencia_sabado, asistencia_domingo, dicFranjas)
        opcion = menu()
    print("Gracias por usar nuestro sistema, hasta la proxima!")
    print()

main()