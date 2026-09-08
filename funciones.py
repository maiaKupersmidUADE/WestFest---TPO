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

'''            
def registrarAsistencia(): 

def modificarAsistencia():

def consultarArtistaMayorConvocatoria():

def consultarTop3ArtistasMayorConvocatoria():  

def consultarShowsSobrepasaronCapacidad():

def consultarTop3FranjasHorariasMayorAsistencia():
'''