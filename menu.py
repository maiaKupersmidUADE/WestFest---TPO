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
    while True:
        opciones_menu()
        try:
            opcion = int(input("Opcion: "))
            if opcion < 0 or opcion > 10:
                print()
                print("Error, la opción elegida debe estar entre 0 y 10.")
                print()
            else:
                return opcion
        except ValueError:
            print()
            print("Error, debe ingresar un número entero entre 0 y 10.")
            print()

def main():
    dicUsuarios = archivos.cargarUsuarios()
    if dicUsuarios is not None:
        acceso = funciones.iniciarSesion(dicUsuarios)
        if acceso:
            config = archivos.cargarConfiguracion()
            if config is not None:
                dicArtistas, dicEscenarios, dicFranjas = funciones.crearDiccionariosAuxiliares(config)
                lineup_sabado, lineup_domingo, incidenciasLineUp = archivos.cargarLineUp(dicArtistas, dicEscenarios, dicFranjas)
                asistencia_sabado, asistencia_domingo, incidenciasAsistencia = archivos.cargarAsistencia(dicEscenarios, dicFranjas)
                incidencias = incidenciasLineUp + incidenciasAsistencia

                if len(incidencias) > 0:
                    print()
                    print("INCIDENCIAS DETECTADAS AL CARGAR LOS ARCHIVOS")
                    print("-" * 50)
                    for mensaje in incidencias:
                        print("-", mensaje)
                    print()

                opcion = menu()
                while opcion != 0:
                    if opcion == 1:
                        funciones.asignarLineUp(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                        archivos.guardarLineUp(lineup_sabado, lineup_domingo, dicEscenarios, dicFranjas)
                        archivos.guardarAsistencia(asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                    elif opcion == 2:
                        funciones.consultarLineUp(lineup_sabado, lineup_domingo, dicEscenarios, dicArtistas, dicFranjas)
                    elif opcion == 3:
                        codArtista = input("Codigo de Artista a buscar: ").upper()
                        funciones.buscarArtista(dicArtistas, codArtista, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                    elif opcion == 4:
                        funciones.registrarAsistencia(lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                        archivos.guardarAsistencia(asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                    elif opcion == 5:
                        funciones.modificarAsistencia(lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                        archivos.guardarAsistencia(asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                    elif opcion == 6:
                        funciones.consultarArtistaMayorConvocatoria(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo)
                    elif opcion == 7:
                        totalS = funciones.obtenerTotalRecursivo(asistencia_sabado)
                        totalD = funciones.obtenerTotalRecursivo(asistencia_domingo)
                        print(f"Asistencia total del sabado: {totalS}")
                        print(f"Asistencia total del domingo: {totalD}")
                    elif opcion == 8:
                        funciones.consultarTop3ArtistasMayorConvocatoria(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo)
                    elif opcion == 9:
                        funciones.consultarShowsSobrepasaronCapacidad(dicArtistas, lineup_sabado, lineup_domingo, asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
                    elif opcion == 10:
                        funciones.consultarTop3FranjasHorariasMayorAsistencia(asistencia_sabado, asistencia_domingo, dicFranjas)

                    opcion = menu()
                print("Gracias por usar nuestro sistema, hasta la proxima!")
                print()
            else:
                print("El programa se cerrará.")
        else:
            print("El programa se cerrará.")
    else:
        print("El programa se cerrará.")

main()