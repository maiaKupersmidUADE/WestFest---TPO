def asignarLineUp(A, LUS, LUD, E, H):
    codArtista = input("Codigo de Artista a buscar: ").upper()
    art = obtenerIndex(A, codArtista, 0)
    if art == -1:
        print("El codigo no existe o mal ingresado")
    else:
        dia = input("A que dia queres asignarlo? (SABADO/DOMINGO): ").upper()
        while dia != "SABADO" and dia != "DOMINGO":
            dia = input("Dia ingresado invalido. ¿A que dia queres asignarlo? (SABADO/DOMINGO): ").upper()

        horario = input("¿En que horario? (Mediodia/Tarde/Noche): ").capitalize()
        while obtenerIndex(H, horario, 1) == -1:
            horario = input("Horario invalido. ¿En que horario? (Mediodia/Tarde/Noche): ").capitalize()
        indiceHorario = obtenerIndex(H, horario, 1)

        escenario = input("¿En que escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
        while obtenerIndex(E, escenario, 1) == -1:
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

def buscarArtista(A, codArtista, LUS, LUD, E, H):
    indice = obtenerIndex(A, codArtista, 0)
    if indice == -1:
        print("El artista que busca no existe o se ingreso mal el codigo")
    else:
        print(f"Artista: {A[indice][1]}")
        for i in range(len(LUS)):
            for j in range(len(LUS[i])):
                if LUS[i][j] == codArtista:
                    print("SABADO")
                    print(f"Escenario: {E[i][1]} - Horario: {H[j][1]}")
                    print()

        for i in range(len(LUD)):
            for j in range(len(LUD[i])):
                if LUD[i][j] == codArtista:
                    print("DOMINGO")
                    print(f"Escenario: {E[i][1]} - Horario: {H[j][1]}")
                    print()

def artistaAsignado(lineup, codArtista, indiceHorario):
    asignado = False
    for i in range(len(lineup)):
        if lineup[i][indiceHorario] == codArtista:
            asignado = True
    return asignado

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
    indice = -1
    i = 0
    while i < len(lista) and indice == -1:
        if lista[i][posicion] == buscar:
            indice = i 
        i += 1  
    return indice

def obtenerTotal(matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] >= 0:
                total += matriz[i][j]
    return total

def pedir_entero_positivo(mensaje):
    num = int(input(mensaje))
    while num < 0:
        print()
        print("Error: La cantidad de espectadores no puede ser negativa.")
        num = int(input(mensaje))
    return num

def registrarAsistencia(LUS, LUD, AS, AD, E, H, capacidad_maxima):
    dia = input("¿De qué día querés registrar asistencia? (SABADO/DOMINGO): ").upper()
    while dia != "SABADO" and dia != "DOMINGO":
        dia = input("Día inválido. Ingrese SABADO o DOMINGO: ").upper()

    horario = input("¿En qué horario? (Mediodia/Tarde/Noche): ").capitalize()
    indiceHorario = obtenerIndex(H, horario, 1)
    while indiceHorario == -1:
        horario = input("Horario inválido. Ingrese (Mediodia/Tarde/Noche): ").capitalize()
        indiceHorario = obtenerIndex(H, horario, 1)

    escenario = input("¿En qué escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
    indiceEscenario = obtenerIndex(E, escenario, 1)
    while indiceEscenario == -1:
        escenario = input("Escenario inválido. Ingrese (Main Stage/Electronic Arena/Mata Club): ").title()
        indiceEscenario = obtenerIndex(E, escenario, 1)

    lineup = LUS if dia == "SABADO" else LUD
    asistencia_matriz = AS if dia == "SABADO" else AD

    if lineup[indiceEscenario][indiceHorario] == "":
        print(f"No hay ningún artista asignado el {dia.lower()} en {escenario} ({horario}).")
    elif asistencia_matriz[indiceEscenario][indiceHorario] >= 0:
        actual = asistencia_matriz[indiceEscenario][indiceHorario]
        print(f"El show ya tiene asistencia registrada ({actual} espectadores). Utilice la opción 'Modificar asistencia'.")
    else:
        espectadores = pedir_entero_positivo("Ingrese la cantidad de espectadores: ")
        asistencia_matriz[indiceEscenario][indiceHorario] = espectadores
        print(f"Asistencia de {espectadores} espectadores registrada.")
        if espectadores > capacidad_maxima:
            print(f"Atención: Se superó la capacidad del escenario ({capacidad_maxima} espectadores).")

def modificarAsistencia(LUS, LUD, AS, AD, E, H, capacidad_maxima):
    dia = input("¿De qué día querés modificar la asistencia? (SABADO/DOMINGO): ").upper()
    while dia != "SABADO" and dia != "DOMINGO":
        dia = input("Día no válido o inexistente. Ingrese SABADO o DOMINGO: ").upper()

    horario = input("¿En qué horario? (Mediodia/Tarde/Noche): ").capitalize()
    indiceHorario = obtenerIndex(H, horario, 1)
    while indiceHorario == -1:
        horario = input("Horario no válido o inexistente. Ingrese (Mediodia/Tarde/Noche): ").capitalize()
        indiceHorario = obtenerIndex(H, horario, 1)

    escenario = input("¿En qué escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
    indiceEscenario = obtenerIndex(E, escenario, 1)
    while indiceEscenario == -1:
        escenario = input("Escenario no válido o inexistente. Ingrese (Main Stage/Electronic Arena/Mata Club): ").title()
        indiceEscenario = obtenerIndex(E, escenario, 1)

    lineup = LUS if dia == "SABADO" else LUD
    asistencia_matriz = AS if dia == "SABADO" else AD

    if lineup[indiceEscenario][indiceHorario] == "":
        print(f"No hay ningún artista asignado el {dia.lower()} en {escenario} ({horario}).")
    elif asistencia_matriz[indiceEscenario][indiceHorario] < 0:
        print("Este show aún no posee asistencia registrada. Utilice la opción 'Registrar asistencia'.")
    else:
        actual = asistencia_matriz[indiceEscenario][indiceHorario]
        print(f"Asistencia registrada actualmente: {actual} espectadores.")
        nueva_asistencia = pedir_entero_positivo("Ingrese la nueva cantidad de espectadores: ")
        asistencia_matriz[indiceEscenario][indiceHorario] = nueva_asistencia
        print(f"Asistencia actualizada correctamente a {nueva_asistencia} espectadores")
        if nueva_asistencia > capacidad_maxima:
            print(f"Atención: Se superó la capacidad del escenario ({capacidad_maxima} espectadores).")

def obtenerConvocatorias(A, LUS, LUD, AS, AD):
    convocatorias = []
    for c in range(len(A)):
        codigo = A[c][0]
        convocatoria = 0
        for i in range(len(LUS)):
            for j in range(len(LUS[i])):
                if LUS[i][j] == codigo:
                    if AS[i][j] >= 0:
                        convocatoria += AS[i][j]
        for i in range(len(LUD)):
            for j in range(len(LUD[i])):
                if LUD[i][j] == codigo:
                    if AD[i][j] >= 0:
                        convocatoria += AD[i][j]
        if convocatoria > 0:
            convocatorias.append((codigo, convocatoria))
    convocatorias.sort(key=lambda x: x[1], reverse=True)
    return convocatorias

def consultarArtistaMayorConvocatoria(A, LUS, LUD, AS, AD):
    convocatorias = obtenerConvocatorias(A, LUS, LUD, AS, AD)

    if len(convocatorias) == 0:
        print()
        print("No hay artistas con asistencia registrada.")
    else:
        codigo = convocatorias[0][0]
        convocatoria = convocatorias[0][1]
        indice = obtenerIndex(A, codigo, 0)

        print()
        print("ARTISTA CON MAYOR CONVOCATORIA")
        print("-" * 40)
        print(f"Artista: {A[indice][1]}")
        print(f"Convocatoria: {convocatoria} espectadores")
        print()

def consultarTop3ArtistasMayorConvocatoria(A, LUS, LUD, AS, AD):
    convocatorias = obtenerConvocatorias(A, LUS, LUD, AS, AD)
    if len(convocatorias) < 3:
        print()
        print("No hay suficientes artistas con asistencia registrada para mostrar el Top 3.")
    else:
        top3 = convocatorias[:3]
        print()
        print("TOP 3 ARTISTAS CON MAYOR CONVOCATORIA")
        print("-" * 45)
        for i in range(len(top3)):
            codigo = top3[i][0]
            convocatoria = top3[i][1]
            indice = obtenerIndex(A, codigo, 0)
            print(f"{i + 1}. {A[indice][1]} - {convocatoria} espectadores")
            print()

def consultarShowsSobrepasaronCapacidad(LUS, LUD, AS, AD, E, H, capacidad_maxima):
    shows_superados = []
    # sabado
    for i in range(len(LUS)):
        for j in range(len(LUS[i])):
            if LUS[i][j] != "" and AS[i][j] > capacidad_maxima:
                show = (E[i][1], H[j][1], LUS[i][j], AS[i][j])
                shows_superados.append(show)
    # domingo
    for i in range(len(LUD)):
        for j in range(len(LUD[i])):
            if LUD[i][j] != "" and AD[i][j] > capacidad_maxima:
                show = (E[i][1], H[j][1], LUD[i][j], AD[i][j])
                shows_superados.append(show)
    print()
    print("SHOWS QUE SUPERARON LA CAPACIDAD")
    print("-" * 45)
    if len(shows_superados) == 0:
        print("Ningun show supero la capacidad maxima del escenario.")
    else:
        print(f"Cantidad de shows que superaron la capacidad: {len(shows_superados)}")
        print()
        for i in range(len(shows_superados)):
            print(f"Escenario: {shows_superados[i][0]}")
            print(f"Horario: {shows_superados[i][1]}")
            print(f"Artista: {shows_superados[i][2]}")
            print(f"Asistencia: {shows_superados[i][3]} espectadores")
            print()

def consultarTop3FranjasHorariasMayorAsistencia(AS, AD, H):
    asistencia_por_franja = []
    for j in range(len(H)):
        total = 0
        # sumar asistencia del sabado
        for i in range(len(AS)):
            if AS[i][j] >= 0:
                total += AS[i][j]
        # sumar asistencia del domingo
        for i in range(len(AD)):
            if AD[i][j] >= 0:
                total += AD[i][j]
        asistencia_por_franja.append((H[j][1], total))
    # ordenar de mayor a menor
    asistencia_por_franja.sort(key=lambda x: x[1], reverse=True)
    # obtener las 3 franjas con mayor asistencia
    top3 = asistencia_por_franja[:3]
    print()
    print("TOP 3 FRANJAS HORARIAS CON MAYOR ASISTENCIA")
    print("-" * 45)
    for i in range(len(top3)):
        print(f"{i + 1} {top3[i][0]} - {top3[i][1]} espectadores")