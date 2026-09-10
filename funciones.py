def asignarLineUp(A, LUS, LUD, E, H):
    codArtista = input("Codigo de Artista a buscar: ").upper()
    art = obtenerIndex(A, codArtista, 0)
    if art == None:
        print("El codigo no existe o mal ingresado")
    else:
        dia = input("A que dia queres asignarlo? (SABADO/DOMINGO): ").upper()
        while dia != "SABADO" and dia != "DOMINGO":
            dia = input("Dia ingresado invalido. ¿A que dia queres asignarlo? (SABADO/DOMINGO): ").upper()

        horario = input("¿En que horario? (Mediodia/Tarde/Noche): ").capitalize()
        while obtenerIndex(H, horario, 1) == None:
            horario = input("Horario invalido. ¿En que horario? (Mediodia/Tarde/Noche): ").capitalize()
        indiceHorario = obtenerIndex(H, horario, 1)

        escenario = input("¿En que escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
        while obtenerIndex(E, escenario, 1) == None:
            escenario = input("Escenario invalido. ¿En que escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
        indiceEscenario = obtenerIndex(E, escenario, 1)

        if dia == "SABADO":
            if LUS[indiceEscenario][indiceHorario] == "" and not artistaAsignado(LUS, codArtista, indiceHorario):
                LUS[indiceEscenario][indiceHorario] = codArtista
            elif artistaAsignado(LUS, codArtista, indiceHorario):
                print(f"{A[art][1]} ya esta asignado a otro escenario en ese horario")
            else:
                print(f"El sabado en {escenario} {horario} ya hay un artista asignado")
        else:
            if LUD[indiceEscenario][indiceHorario] == "" and not artistaAsignado(LUD, codArtista, indiceHorario):
                LUD[indiceEscenario][indiceHorario] = codArtista
            elif artistaAsignado(LUD, codArtista, indiceHorario):
                print(f"{A[art][1]} ya esta asignado a otro escenario en ese horario")
            else:
                print(f"El domingo en {escenario} {horario} ya hay un artista asignado")

def artistaAsignado(lineup, codArtista, indiceHorario):
    esta = False
    for i in range(len(lineup)):
        if lineup[i][indiceHorario] == codArtista:
            esta = True
            break
    return esta

def consultarLineUp(LUS, LUD, E, A, H):
    print()
    print("SÁBADO")
    print("-" * 100)

    for horario in H:
        print(f"{horario[1]:<25}", end="")
    print()
    print("-" * 100)

    for i in range(len(LUS)):
        print(f"{E[i][1]:<25}", end="")
        for j in range(len(LUS[i])):
            codigo = LUS[i][j]
            for artista in A:
                if artista[0] == codigo:
                    nombre = artista[1]
            if codigo == "":
                nombre = "-"
            print(f"{nombre:<25}", end="")
        print()

    print()
    print("DOMINGO")
    print("-" * 100)

    for horario in H:
        print(f"{horario[1]:<25}", end="")
    print()
    print("-" * 100)

    for i in range(len(LUD)):
        print(f"{E[i][1]:<25}", end="")
        for j in range(len(LUD[i])):
            codigo = LUD[i][j]
            for artista in A:
                if artista[0] == codigo:
                    nombre = artista[1]
            if codigo == "":
                nombre = "-"
            print(f"{nombre:<25}", end="")
        print()

def obtenerIndex(lista, buscar, posicion):
    indice = None
    for i in range(len(lista)):
        if lista[i][posicion] == buscar:
            indice = i
            break
    return indice

def obtenerTotal(matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] >= 0:
                total += matriz[i][j]
    return total


def pedir_entero_positivo(mensaje):
    #Función con try/except para pedir números de manera segura
    while True:
        try:
            num = int(input(mensaje))
            if num >= 0:
                return num
            print("Error: La cantidad de espectadores no puede ser negativa.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
       
def registrarAsistencia(LUS, LUD, AS, AD, E, H, capacidad_maxima):
    dia = input("¿De qué día querés registrar asistencia? (SABADO/DOMINGO): ").upper()
    while dia != "SABADO" and dia != "DOMINGO":
        dia = input("Día inválido. Ingrese SABADO o DOMINGO: ").upper()

    horario = input("¿En qué horario? (Mediodia/Tarde/Noche): ").capitalize()
    indiceHorario = obtenerIndex(H, horario, 1)
    while indiceHorario is None:
        horario = input("Horario inválido. Ingrese (Mediodia/Tarde/Noche): ").capitalize()
        indiceHorario = obtenerIndex(H, horario, 1)

    escenario = input("¿En qué escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
    indiceEscenario = obtenerIndex(E, escenario, 1)
    while indiceEscenario is None:
        escenario = input("Escenario inválido. Ingrese (Main Stage/Electronic Arena/Mata Club): ").title()
        indiceEscenario = obtenerIndex(E, escenario, 1)

    lineup = LUS if dia == "SABADO" else LUD
    asistencia_matriz = AS if dia == "SABADO" else AD

    if lineup[indiceEscenario][indiceHorario] == "":
        print(f"No hay ningún artista asignado el {dia.lower()} en {escenario} ({horario}).")
        return

    if asistencia_matriz[indiceEscenario][indiceHorario] >= 0:
        actual = asistencia_matriz[indiceEscenario][indiceHorario]
        print(f"El show ya tiene asistencia registrada ({actual} espectadores). Utilice la opción 'Modificar asistencia'.")
        return

    espectadores = pedir_entero_positivo("Ingrese la cantidad de espectadores: ")

    asistencia_matriz[indiceEscenario][indiceHorario] = espectadores
    print(f"Asistencia de {espectadores} espectadores registrada.")

    if espectadores > capacidad_maxima:
        print(f" Atención: Se superó la capacidad del escenario ({capacidad_maxima} espectadores).")


def modificarAsistencia(LUS, LUD, AS, AD, E, H, capacidad_maxima):
    
    dia = input("¿De qué día querés modificar la asistencia? (SABADO/DOMINGO): ").upper()
    while dia != "SABADO" and dia != "DOMINGO":
        dia = input("Día no válido o inexistente. Ingrese SABADO o DOMINGO: ").upper()

    horario = input("¿En qué horario? (Mediodia/Tarde/Noche): ").capitalize()
    indiceHorario = obtenerIndex(H, horario, 1)
    while indiceHorario is None:
        horario = input("Horario no válido o inexistente. Ingrese (Mediodia/Tarde/Noche): ").capitalize()
        indiceHorario = obtenerIndex(H, horario, 1)

    escenario = input("¿En qué escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
    indiceEscenario = obtenerIndex(E, escenario, 1)
    while indiceEscenario is None:
        escenario = input("Escenario no válido o inexistente. Ingrese (Main Stage/Electronic Arena/Mata Club): ").title()
        indiceEscenario = obtenerIndex(E, escenario, 1)

    lineup = LUS if dia == "SABADO" else LUD
    asistencia_matriz = AS if dia == "SABADO" else AD

    if lineup[indiceEscenario][indiceHorario] == "":
        print(f"No hay ningún artista asignado el {dia.lower()} en {escenario} ({horario}).")
        return

    if asistencia_matriz[indiceEscenario][indiceHorario] < 0:
        print("Este show aún no posee asistencia registrada. Utilice la opción 'Registrar asistencia'.")
        return

    actual = asistencia_matriz[indiceEscenario][indiceHorario]
    print(f"Asistencia registrada actualmente: {actual} espectadores.")

    nueva_asistencia = pedir_entero_positivo("Ingrese la nueva cantidad de espectadores: ")

    asistencia_matriz[indiceEscenario][indiceHorario] = nueva_asistencia
    print(f"Asistencia actualizada correctamente a {nueva_asistencia} espectadores")

    if nueva_asistencia > capacidad_maxima:
        print(f"Atención: Se superó la capacidad del escenario ({capacidad_maxima} espectadores).")



'''
def consultarArtistaMayorConvocatoria():

def consultarTop3ArtistasMayorConvocatoria():  

def consultarShowsSobrepasaronCapacidad():

def consultarTop3FranjasHorariasMayorAsistencia():
'''