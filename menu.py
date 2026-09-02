def opciones_menu():
    # Funcion que muestra las opciones del menu
    print("-" * 50)
    print("                 MENU DE CONTENIDOS")
    print("-" * 50)
    print("Seleccione una opcion:")
    print("1. Consultar Line Up")
    print("2. Buscar artista")
    print("3. Registrar asistencia")
    print("4. Modificar asistencia")
    print("5. Consultar informes")
    print("6. Modificar ranking de artistas")
    print("0. Salir")
    print("-" * 50)
    
def menu():
    opciones_menu()
    opcion = int(input("Opción: "))
    # Validar que la opcion elegida este dentro de los rangos permitidos
    while opcion < 0 or opcion > 6:
        print("Error, la opcion elegida debe estar entre 0 y 6")
        opciones_menu()
        opcion = int(input("Seleccione una opcion"))
    return opcion

def main():
    

main()