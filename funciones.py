import validaciones

def artistaAsignado(lineup, codArtista, indiceHorario):
    asignado = False
    for i in range(len(lineup)):
        if lineup[i][indiceHorario] == codArtista:
            asignado = True
    return asignado

def obtenerCodigo(diccionario, criterio, tipoBusqueda):
    codigoEncontrado = ""
    indice = 0

    if tipoBusqueda == "indice":
        codigoEncontrado = -1

    for codigo in diccionario:
        if tipoBusqueda == "nombre":
            if diccionario[codigo].lower() == criterio.lower():
                codigoEncontrado = codigo
        elif tipoBusqueda == "escenario":
            if diccionario[codigo]["nombre"].lower() == criterio.lower():
                codigoEncontrado = codigo
        elif tipoBusqueda == "indice":
            if codigo == criterio:
                codigoEncontrado = indice
        elif tipoBusqueda == "posicion":
            if indice == criterio:
                codigoEncontrado = codigo

        indice += 1

    return codigoEncontrado


def asignarLineUp(A, LUS, LUD, AS, AD, E, H):
    codArtista = input("Codigo de Artista a buscar: ").upper()

    try:
        validaciones.validarCodigoArtista(codArtista, A)
    except ValueError as error:
        print(error)
        return

    dia = input("A que dia queres asignarlo? (SABADO/DOMINGO): ").upper()

    while dia != "SABADO" and dia != "DOMINGO":
        dia = input("Dia ingresado invalido. ¿A que dia queres asignarlo? (SABADO/DOMINGO): ").upper()

    horario = input("¿En que horario? (Mediodia/Tarde/Noche): ").capitalize()
    codigoHorario = obtenerCodigo(H, horario, "nombre")

    while codigoHorario == "":
        horario = input("Horario invalido. Ingrese Mediodia, Tarde o Noche: ").capitalize()
        codigoHorario = obtenerCodigo(H, horario, "nombre")

    indiceHorario = obtenerCodigo(H, codigoHorario, "indice")

    escenario = input("¿En que escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
    codigoEscenario = obtenerCodigo(E, escenario, "escenario")

    while codigoEscenario == "":
        escenario = input("Escenario invalido. Ingrese un escenario existente: ").title()
        codigoEscenario = obtenerCodigo(E, escenario, "escenario")

    try:
        validaciones.validarCodigoEscenario(codigoEscenario, E)
    except ValueError as error:
        print(error)
        return

    indiceEscenario = obtenerCodigo(E, codigoEscenario, "indice")

    lineup = LUS if dia == "SABADO" else LUD
    asistencia = AS if dia == "SABADO" else AD

    if artistaAsignado(lineup, codArtista, indiceHorario):
        print(f"{A[codArtista]} ya esta asignado a otro escenario en ese horario.")
    else:
        if lineup[indiceEscenario][indiceHorario] != "":
            cod_act = lineup[indiceEscenario][indiceHorario]
            nom_act = A[cod_act] if cod_act in A else cod_act

            resp = input(f"El {dia.lower()} en {escenario} ({horario}) ya tiene asignado a {nom_act}, ¿quiere reemplazarlo? (S/N): ").upper()

            if resp == "S":
                lineup[indiceEscenario][indiceHorario] = codArtista
                asistencia[indiceEscenario][indiceHorario] = -1
                print(f"Artista {A[codArtista]} asignado correctamente.")
            else:
                print("Operacion cancelada.")

        else:
            lineup[indiceEscenario][indiceHorario] = codArtista
            asistencia[indiceEscenario][indiceHorario] = -1
            print(f"Artista {A[codArtista]} asignado correctamente.")


def buscarArtista(A, codArtista, LUS, LUD, AS, AD, E, H):
    showsArtista = []

    if codArtista in A:

        # Sabado
        for i in range(len(LUS)):
            for j in range(len(LUS[i])):
                if LUS[i][j] == codArtista:
                    asist = AS[i][j]
                    codigoEscenario = obtenerCodigo(E, i, "posicion")
                    nombreEscenario = E[codigoEscenario]["nombre"]
                    codigoHorario = obtenerCodigo(H, j, "posicion")
                    nombreHorario = H[codigoHorario]

                    show = ("SABADO", nombreEscenario, nombreHorario, asist)
                    showsArtista.append(show)

        # Domingo
        for i in range(len(LUD)):
            for j in range(len(LUD[i])):
                if LUD[i][j] == codArtista:
                    asist = AD[i][j]
                    codigoEscenario = obtenerCodigo(E, i, "posicion")
                    nombreEscenario = E[codigoEscenario]["nombre"]
                    codigoHorario = obtenerCodigo(H, j, "posicion")
                    nombreHorario = H[codigoHorario]

                    show = ("DOMINGO", nombreEscenario, nombreHorario, asist)
                    showsArtista.append(show)

    return showsArtista


def consultarLineUp(LUS, LUD, E, A, H):
    print()
    print("SÁBADO")
    print("-" * 100)

    for codigo in H:
        print(f"{H[codigo]:<25}", end="")

    print()
    print("-" * 100)

    i = 0
    for codigo in E:
        print(f"{E[codigo]['nombre']:<25}", end="")

        for j in range(len(LUS[i])):
            artista = LUS[i][j]
            nombre = A[artista] if artista in A else "-"
            print(f"{nombre:<25}", end="")

        print()
        i += 1

    print()
    print("DOMINGO")
    print("-" * 100)

    for codigo in H:
        print(f"{H[codigo]:<25}", end="")

    print()
    print("-" * 100)

    i = 0
    for codigo in E:
        print(f"{E[codigo]['nombre']:<25}", end="")

        for j in range(len(LUD[i])):
            artista = LUD[i][j]
            nombre = A[artista] if artista in A else "-"
            print(f"{nombre:<25}", end="")

        print()
        i += 1


def obtenerTotalRecursivo(matriz, i=0, j=0):
    if i == len(matriz):
        return 0

    if j == len(matriz[i]):
        return obtenerTotalRecursivo(matriz, i + 1, 0)

    if matriz[i][j] >= 0:
        return matriz[i][j] + obtenerTotalRecursivo(matriz, i, j + 1)
    else:
        return obtenerTotalRecursivo(matriz, i, j + 1)


def registrarAsistencia(LUS, LUD, AS, AD, E, H):
    dia = input("¿De que dia queres registrar asistencia? (SABADO/DOMINGO): ").upper()

    while dia != "SABADO" and dia != "DOMINGO":
        dia = input("Dia invalido. Ingrese SABADO o DOMINGO: ").upper()

    horario = input("¿En que horario? (Mediodia/Tarde/Noche): ").capitalize()
    codigoHorario = obtenerCodigo(H, horario, "nombre")

    while codigoHorario == "":
        horario = input("Horario invalido. Ingrese Mediodia, Tarde o Noche: ").capitalize()
        codigoHorario = obtenerCodigo(H, horario, "nombre")

    indiceHorario = obtenerCodigo(H, codigoHorario, "indice")

    escenario = input("¿En que escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
    codigoEscenario = obtenerCodigo(E, escenario, "escenario")

    while codigoEscenario == "":
        escenario = input("Escenario invalido. Ingrese un escenario existente: ").title()
        codigoEscenario = obtenerCodigo(E, escenario, "escenario")

    indiceEscenario = obtenerCodigo(E, codigoEscenario, "indice")

    lineup = LUS if dia == "SABADO" else LUD
    asistencia_matriz = AS if dia == "SABADO" else AD
    capacidad_maxima = E[codigoEscenario]["capacidad_maxima"]

    if lineup[indiceEscenario][indiceHorario] == "":
        print(f"No hay ningun artista asignado el {dia.lower()} en {escenario} ({horario}).")

    elif asistencia_matriz[indiceEscenario][indiceHorario] >= 0:
        actual = asistencia_matriz[indiceEscenario][indiceHorario]
        print(f"El show ya tiene asistencia registrada ({actual} espectadores). Utilice la opcion 'Modificar asistencia'.")

    else:
        espectadores = validaciones.pedir_entero_positivo("Ingrese la cantidad de espectadores: ")
        asistencia_matriz[indiceEscenario][indiceHorario] = espectadores
        print(f"Asistencia de {espectadores} espectadores registrada.")

        if espectadores > capacidad_maxima:
            print(f"Atencion: Se supero la capacidad del escenario ({capacidad_maxima} espectadores).")


def modificarAsistencia(LUS, LUD, AS, AD, E, H):
    dia = input("¿De que dia queres modificar la asistencia? (SABADO/DOMINGO): ").upper()

    while dia != "SABADO" and dia != "DOMINGO":
        dia = input("Dia no valido. Ingrese SABADO o DOMINGO: ").upper()

    horario = input("¿En que horario? (Mediodia/Tarde/Noche): ").capitalize()
    codigoHorario = obtenerCodigo(H, horario, "nombre")

    while codigoHorario == "":
        horario = input("Horario no valido. Ingrese Mediodia, Tarde o Noche: ").capitalize()
        codigoHorario = obtenerCodigo(H, horario, "nombre")

    indiceHorario = obtenerCodigo(H, codigoHorario, "indice")

    escenario = input("¿En que escenario? (Main Stage/Electronic Arena/Mata Club): ").title()
    codigoEscenario = obtenerCodigo(E, escenario, "escenario")

    while codigoEscenario == "":
        escenario = input("Escenario no valido. Ingrese un escenario existente: ").title()
        codigoEscenario = obtenerCodigo(E, escenario, "escenario")

    indiceEscenario = obtenerCodigo(E, codigoEscenario, "indice")

    lineup = LUS if dia == "SABADO" else LUD
    asistencia_matriz = AS if dia == "SABADO" else AD
    capacidad_maxima = E[codigoEscenario]["capacidad_maxima"]

    if lineup[indiceEscenario][indiceHorario] == "":
        print(f"No hay ningun artista asignado el {dia.lower()} en {escenario} ({horario}).")

    elif asistencia_matriz[indiceEscenario][indiceHorario] < 0:
        print("Este show aun no posee asistencia registrada. Utilice la opcion 'Registrar asistencia'.")

    else:
        actual = asistencia_matriz[indiceEscenario][indiceHorario]
        print(f"Asistencia registrada actualmente: {actual} espectadores.")

        nueva_asistencia = validaciones.pedir_entero_positivo("Ingrese la nueva cantidad de espectadores: ")
        asistencia_matriz[indiceEscenario][indiceHorario] = nueva_asistencia

        print(f"Asistencia actualizada correctamente a {nueva_asistencia} espectadores.")

        if nueva_asistencia > capacidad_maxima:
            print(f"Atencion: Se supero la capacidad del escenario ({capacidad_maxima} espectadores).")


def obtenerConvocatorias(A, LUS, LUD, AS, AD):
    convocatorias = []

    for codigo in A:
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
        max_convocatoria = convocatorias[0][1]

        print()
        print("ARTISTA(S) CON MAYOR CONVOCATORIA")
        print("-" * 40)
        print(f"Mayor Convocatoria: {max_convocatoria} espectadores")

        for item in convocatorias:
            if item[1] == max_convocatoria:
                print(f"- Artista: {A[item[0]]}")

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
            print(f"{i + 1}. {A[codigo]} - {convocatoria} espectadores")
            print()


def consultarShowsSobrepasaronCapacidad(A, LUS, LUD, AS, AD, E, H):
    shows_superados = []

    # Sabado
    i = 0
    for codigoEscenario in E:
        capacidad_maxima = E[codigoEscenario]["capacidad_maxima"]
        nombreEscenario = E[codigoEscenario]["nombre"]

        for j in range(len(LUS[i])):
            codigoArtista = LUS[i][j]

            if codigoArtista != "" and AS[i][j] > capacidad_maxima:
                art_nombre = A[codigoArtista] if codigoArtista in A else codigoArtista
                codigoHorario = obtenerCodigo(H, j, "posicion")
                nombreHorario = H[codigoHorario]

                show = ("SABADO", nombreEscenario, nombreHorario, art_nombre, AS[i][j])
                shows_superados.append(show)

        i += 1

    # Domingo
    i = 0
    for codigoEscenario in E:
        capacidad_maxima = E[codigoEscenario]["capacidad_maxima"]
        nombreEscenario = E[codigoEscenario]["nombre"]

        for j in range(len(LUD[i])):
            codigoArtista = LUD[i][j]

            if codigoArtista != "" and AD[i][j] > capacidad_maxima:
                art_nombre = A[codigoArtista] if codigoArtista in A else codigoArtista
                codigoHorario = obtenerCodigo(H, j, "posicion")
                nombreHorario = H[codigoHorario]

                show = ("DOMINGO", nombreEscenario, nombreHorario, art_nombre, AD[i][j])
                shows_superados.append(show)

        i += 1

    return shows_superados


def consultarTop3FranjasHorariasMayorAsistencia(AS, AD, H):
    asistencia_por_franja = []

    j = 0
    for codigo in H:
        total = 0

        for i in range(len(AS)):
            if AS[i][j] >= 0:
                total += AS[i][j]

        asistencia_por_franja.append(("Sabado", H[codigo], total))
        j += 1

    j = 0
    for codigo in H:
        total = 0

        for i in range(len(AD)):
            if AD[i][j] >= 0:
                total += AD[i][j]

        asistencia_por_franja.append(("Domingo", H[codigo], total))
        j += 1

    for i in range(len(asistencia_por_franja) - 1):
        mayor = i

        for j in range(i + 1, len(asistencia_por_franja)):
            if asistencia_por_franja[j][2] > asistencia_por_franja[mayor][2]:
                mayor = j

        aux = asistencia_por_franja[i]
        asistencia_por_franja[i] = asistencia_por_franja[mayor]
        asistencia_por_franja[mayor] = aux

    top3 = asistencia_por_franja[:3]

    return top3


def crearDiccionariosAuxiliares(config):
    dicArtistas = {}

    for artista in config["artistas"]:
        dicArtistas[artista["codigo"]] = artista["nombre"]

    dicEscenarios = {}

    for escenario in config["escenarios"]:
        dicEscenarios[escenario["codigo"]] = {
            "nombre": escenario["nombre"],
            "capacidad_maxima": escenario["capacidad_maxima"]
        }

    dicFranjas = {}

    for franja in config["franjas"]:
        dicFranjas[franja["codigo"]] = franja["nombre"]

    return dicArtistas, dicEscenarios, dicFranjas


def pedirCredenciales():
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    return usuario, contraseña


def iniciarSesion(dicUsuarios):
    acceso = False

    while acceso == False:
        usuario, contraseña = pedirCredenciales()

        try:
            validaciones.validarContrasenia(contraseña)

            if usuario in dicUsuarios and dicUsuarios[usuario] == contraseña:
                print("\nInicio de sesión exitoso.")
                acceso = True
            else:
                print("\nUsuario o contraseña incorrectos. Intente nuevamente.\n")

        except ValueError as error:
            print(f"\nError de formato: {error}\nIntente nuevamente.\n")

    return acceso


def consultarAsistenciaTotalPorDia(AS, AD):
    total_sabado = 0
    total_domingo = 0

    # Sabado
    for i in range(len(AS)):
        for j in range(len(AS[i])):
            if AS[i][j] >= 0:
                total_sabado += AS[i][j]

    # Domingo
    for i in range(len(AD)):
        for j in range(len(AD[i])):
            if AD[i][j] >= 0:
                total_domingo += AD[i][j]

    return total_sabado, total_domingo


def consultarShowsSinAsistencia(A, LUS, LUD, AS, AD, E, H):
    shows_sin_asistencia = []

    # Sabado
    i = 0
    for codigoEscenario in E:
        for j in range(len(LUS[i])):
            if LUS[i][j] != "" and AS[i][j] == -1:
                codigoHorario = obtenerCodigo(H, j, "posicion")
                codigoArtista = LUS[i][j]

                show = (
                    "SABADO",
                    E[codigoEscenario]["nombre"],
                    H[codigoHorario],
                    A[codigoArtista]
                )

                shows_sin_asistencia.append(show)

        i += 1

    # Domingo
    i = 0
    for codigoEscenario in E:
        for j in range(len(LUD[i])):
            if LUD[i][j] != "" and AD[i][j] == -1:
                codigoHorario = obtenerCodigo(H, j, "posicion")
                codigoArtista = LUD[i][j]

                show = (
                    "DOMINGO",
                    E[codigoEscenario]["nombre"],
                    H[codigoHorario],
                    A[codigoArtista]
                )

                shows_sin_asistencia.append(show)

        i += 1

    return shows_sin_asistencia


def generarReporte(A, LUS, LUD, AS, AD, E, H, incidencias):
    reporte = ""

    # Totales de asistencia mediante recursividad
    totalSabado = obtenerTotalRecursivo(AS)
    totalDomingo = obtenerTotalRecursivo(AD)

    reporte += "========================================\n"
    reporte += "             REPORTE GENERAL\n"
    reporte += "========================================\n\n"

    reporte += "ASISTENCIA TOTAL\n"
    reporte += f"Sabado: {totalSabado} espectadores\n"
    reporte += f"Domingo: {totalDomingo} espectadores\n"
    reporte += f"Total del festival: {totalSabado + totalDomingo} espectadores\n\n"

    # Convocatoria de artistas
    convocatorias = obtenerConvocatorias(A, LUS, LUD, AS, AD)

    reporte += "ARTISTAS CON MAYOR CONVOCATORIA\n"

    if len(convocatorias) > 0:
        mayor = convocatorias[0][1]

        reporte += f"Mayor convocatoria: {mayor} espectadores\n"

        for artista in convocatorias:
            if artista[1] == mayor:
                reporte += f"- {A[artista[0]]}\n"

        reporte += "\nTop 3 de artistas:\n"

        for i in range(min(3, len(convocatorias))):
            codigo = convocatorias[i][0]
            reporte += f"{i + 1}. {A[codigo]} - {convocatorias[i][1]} espectadores\n"

    else:
        reporte += "No hay artistas con asistencia registrada.\n"

    # Top 3 de dias y franjas
    top3Franjas = consultarTop3FranjasHorariasMayorAsistencia(AS, AD, H)

    reporte += "\nTOP 3 DE DIAS Y FRANJAS HORARIAS\n"

    for i in range(len(top3Franjas)):
        franja = top3Franjas[i]
        reporte += f"{i + 1}. {franja[0]} - {franja[1]}: {franja[2]} espectadores\n"

    # Obtener shows superados y pendientes
    showsSuperados = consultarShowsSobrepasaronCapacidad(
        A, LUS, LUD, AS, AD, E, H
    )

    showsPendientes = consultarShowsSinAsistencia(
        A, LUS, LUD, AS, AD, E, H
    )

    # Reporte filtrado por dia
    reporte += "\n========================================\n"
    reporte += "             REPORTE FILTRADO\n"
    reporte += "========================================\n"

    dias = [
        ("SABADO", LUS, AS),
        ("DOMINGO", LUD, AD)
    ]

    for dia, lineup, asistencia in dias:
        cantidadShows = 0

        for i in range(len(lineup)):
            for j in range(len(lineup[i])):
                if lineup[i][j] != "":
                    cantidadShows += 1

        totalDia = obtenerTotalRecursivo(asistencia)

        reporte += f"\nREPORTE DEL {dia}\n"
        reporte += "-" * 40 + "\n"
        reporte += f"Cantidad de shows: {cantidadShows}\n"
        reporte += f"Espectadores registrados: {totalDia}\n"

        # Shows que superaron la capacidad de ese dia
        reporte += "\nShows que superaron la capacidad:\n"
        cantidadSuperadosDia = 0

        for show in showsSuperados:
            if show[0] == dia:
                reporte += f"- {show[3]} en {show[1]} ({show[2]}): {show[4]} espectadores\n"
                cantidadSuperadosDia += 1

        if cantidadSuperadosDia == 0:
            reporte += "Ninguno.\n"

        # Shows pendientes de asistencia de ese dia
        reporte += "\nShows sin asistencia registrada:\n"
        cantidadPendientesDia = 0

        for show in showsPendientes:
            if show[0] == dia:
                reporte += f"- {show[3]} en {show[1]} ({show[2]})\n"
                cantidadPendientesDia += 1

        if cantidadPendientesDia == 0:
            reporte += "Ninguno.\n"

    # Resumen de artistas con y sin shows
    artistasConShows = set()

    for i in range(len(LUS)):
        for j in range(len(LUS[i])):
            if LUS[i][j] != "":
                artistasConShows.add(LUS[i][j])

    for i in range(len(LUD)):
        for j in range(len(LUD[i])):
            if LUD[i][j] != "":
                artistasConShows.add(LUD[i][j])

    artistasSinShows = []

    for codigo in A:
        if codigo not in artistasConShows:
            artistasSinShows.append(A[codigo])

    reporte += "\n========================================\n"
    reporte += "          RESUMEN DE ARTISTAS\n"
    reporte += "========================================\n"

    reporte += f"Artistas con shows: {len(artistasConShows)}\n"
    reporte += f"Artistas sin shows: {len(artistasSinShows)}\n"

    if len(artistasSinShows) > 0:
        reporte += "\nArtistas sin shows asignados:\n"

        for artista in artistasSinShows:
            reporte += f"- {artista}\n"

    # Alertas
    reporte += "\n========================================\n"
    reporte += "                ALERTAS\n"
    reporte += "========================================\n"

    reporte += f"Shows que superaron la capacidad: {len(showsSuperados)}\n"
    reporte += f"Shows sin asistencia registrada: {len(showsPendientes)}\n"
    reporte += f"Incidencias de archivos: {len(incidencias)}\n"

    if len(incidencias) > 0:
        reporte += "\nDETALLE DE INCIDENCIAS:\n"

        for incidencia in incidencias:
            reporte += f"- {incidencia}\n"
    else:
        reporte += "No se registraron incidencias de archivos.\n"

    # Recomendaciones
    reporte += "\n========================================\n"
    reporte += "           RECOMENDACIONES\n"
    reporte += "========================================\n"

    if len(showsPendientes) > 0:
        reporte += "- Registrar la asistencia de los shows pendientes.\n"

    if len(showsSuperados) > 0:
        reporte += "- Revisar los shows que superaron la capacidad.\n"

    if len(artistasSinShows) > 0:
        reporte += "- Revisar los artistas que no tienen shows asignados.\n"

    if len(incidencias) > 0:
        reporte += "- Revisar las incidencias de los archivos.\n"

    if (len(showsPendientes) == 0 and
        len(showsSuperados) == 0 and
        len(artistasSinShows) == 0 and
        len(incidencias) == 0):
        reporte += "No se detectaron situaciones que requieran atencion.\n"

    return reporte