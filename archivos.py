import json
import validaciones

def cargarConfiguracion():
    try:
        with open("configuracion.json", "r", encoding="utf-8") as archivo:
            config = json.load(archivo)
        validaciones.validarConfiguracion(config)
        return config
    except FileNotFoundError:
        print("Error: no se encontró configuracion.json")
    except json.JSONDecodeError:
        print("Error: el archivo no es un JSON válido.")
    except OSError:
        print("Error: no se pudo abrir el archivo.")
    except ValueError as error:
        print(f"Error de configuración: {error}")
    return None

def cargarLineUp(dicArtistas, dicEscenarios, dicFranjas):
    lineup_sabado = [["" for j in range(len(dicFranjas))] for i in range(len(dicEscenarios))]
    lineup_domingo = [["" for j in range(len(dicFranjas))] for i in range(len(dicEscenarios))]

    codigosEscenarios = list(dicEscenarios.keys())
    codigosFranjas = list(dicFranjas.keys())

    incidencias = []
    try:
        with open("lineup.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            numeroFila = 1
            for fila in lineas[1:]:
                numeroFila += 1
                try:
                    if fila.strip() != "":
                        datos = fila.strip().split(",")

                        if len(datos) != 4:
                            raise ValueError("La fila está incompleta o tiene columnas de más.")

                        registro = {
                            "dia": datos[0].upper(),
                            "codigo_escenario": datos[1],
                            "codigo_franja": datos[2],
                            "codigo_artista": datos[3]
                        }

                        dia = registro["dia"]
                        codEscenario = registro["codigo_escenario"]
                        codFranja = registro["codigo_franja"]
                        codArtista = registro["codigo_artista"]

                        if codEscenario not in dicEscenarios:
                            raise ValueError(f"El escenario {codEscenario} no existe.")

                        if codFranja not in dicFranjas:
                            raise ValueError(f"La franja {codFranja} no existe.")

                        if codArtista not in dicArtistas:
                            raise ValueError(f"El artista {codArtista} no existe.")

                        if dia != "SABADO" and dia != "DOMINGO":
                            raise ValueError(f"El dia {dia} no es valido.")

                        indiceEscenario = codigosEscenarios.index(codEscenario)
                        indiceFranja = codigosFranjas.index(codFranja)

                        if dia == "SABADO":
                            grilla = lineup_sabado
                        else:
                            grilla = lineup_domingo

                        if grilla[indiceEscenario][indiceFranja] != "":
                            raise ValueError("Esa posición está repetida en el archivo.")

                        artistaRepetido = False
                        for i in range(len(grilla)):
                            if grilla[i][indiceFranja] == codArtista:
                                artistaRepetido = True

                        if artistaRepetido:
                            raise ValueError(f"El artista {codArtista} ya está asignado en otra posición de esa franja.")

                        grilla[indiceEscenario][indiceFranja] = codArtista

                except ValueError as error:
                    incidencias.append(f"Fila {numeroFila} de lineup.csv: {error}")
    except FileNotFoundError:
        guardarLineUp(lineup_sabado, lineup_domingo, dicEscenarios, dicFranjas)
        incidencias.append("No se encontró lineup.csv, se creó un archivo nuevo vacío.")
    except OSError:
        incidencias.append("No se pudo leer lineup.csv.")

    return lineup_sabado, lineup_domingo, incidencias

def guardarLineUp(LUS, LUD, dicEscenarios, dicFranjas):
    try:
        with open("lineup.csv", "w", encoding="utf-8") as archivo:
            archivo.write("dia,codigo_escenario,codigo_franja,codigo_artista\n")
            codigosEscenarios = list(dicEscenarios.keys())
            codigosFranjas = list(dicFranjas.keys())

            # Guardar lineup del SABADO
            for i in range(len(LUS)):
                for j in range(len(LUS[i])):
                    if LUS[i][j] != "":
                        archivo.write("SABADO," + codigosEscenarios[i] + "," + codigosFranjas[j] + "," + LUS[i][j] + "\n")

            # Guardar lineup del DOMINGO
            for i in range(len(LUD)):
                for j in range(len(LUD[i])):
                    if LUD[i][j] != "":
                        archivo.write("DOMINGO," + codigosEscenarios[i] + "," + codigosFranjas[j] + "," + LUD[i][j] + "\n")
    except OSError:
        print("Error: no se pudo guardar lineup.csv.")

def cargarAsistencia(dicEscenarios, dicFranjas, lineup_sabado, lineup_domingo):
    asistencia_sabado = [[-2 for j in range(len(dicFranjas))] for i in range(len(dicEscenarios))]
    asistencia_domingo = [[-2 for j in range(len(dicFranjas))] for i in range(len(dicEscenarios))]

    codigosEscenarios = list(dicEscenarios.keys())
    codigosFranjas = list(dicFranjas.keys())
    incidencias = []

    try:
        with open("asistencias.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            numeroFila = 1

            for fila in lineas[1:]:
                numeroFila += 1
                try:
                    if fila.strip() != "":
                        datos = fila.strip().split(",")

                        if len(datos) != 4:
                            raise ValueError("La fila está incompleta o tiene columnas de más.")

                        registro = {
                            "dia": datos[0].upper(),
                            "codigo_escenario": datos[1],
                            "codigo_franja": datos[2],
                            "asistencia": datos[3]
                        }

                        dia = registro["dia"]
                        codEscenario = registro["codigo_escenario"]
                        codFranja = registro["codigo_franja"]
                        textoAsistencia = registro["asistencia"]

                        if codEscenario not in dicEscenarios:
                            raise ValueError(f"El escenario {codEscenario} no existe.")

                        if codFranja not in dicFranjas:
                            raise ValueError(f"La franja {codFranja} no existe.")

                        if dia != "SABADO" and dia != "DOMINGO":
                            raise ValueError(f"El dia {dia} no es valido.")

                        try:
                            asistencia = int(textoAsistencia)
                        except ValueError:
                            raise ValueError(f"La asistencia '{textoAsistencia}' no es un número entero.")

                        if asistencia < -1:
                            raise ValueError(f"La asistencia {asistencia} no es válida (debe ser -1 o mayor o igual a 0).")

                        indiceEscenario = codigosEscenarios.index(codEscenario)
                        indiceFranja = codigosFranjas.index(codFranja)

                        if dia == "SABADO":
                            grilla = asistencia_sabado
                            lineup = lineup_sabado
                        else:
                            grilla = asistencia_domingo
                            lineup = lineup_domingo

                        if lineup[indiceEscenario][indiceFranja] == "":
                            raise ValueError("Hay una asistencia registrada para una posición sin show.")

                        if grilla[indiceEscenario][indiceFranja] != -2:
                            raise ValueError("Esa posición está repetida en el archivo.")

                        grilla[indiceEscenario][indiceFranja] = asistencia

                except ValueError as error:
                    incidencias.append(f"Fila {numeroFila} de asistencias.csv: {error}")

    except FileNotFoundError:
        for i in range(len(lineup_sabado)):
            for j in range(len(lineup_sabado[i])):
                if lineup_sabado[i][j] != "":
                    asistencia_sabado[i][j] = -1

        for i in range(len(lineup_domingo)):
            for j in range(len(lineup_domingo[i])):
                if lineup_domingo[i][j] != "":
                    asistencia_domingo[i][j] = -1

        guardarAsistencia(asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
        incidencias.append("No se encontró asistencias.csv, se creó un archivo nuevo.")

    except OSError:
        incidencias.append("No se pudo leer asistencias.csv.")

    # Los shows que no tenían una asistencia registrada quedan pendientes (-1).
    for i in range(len(lineup_sabado)):
        for j in range(len(lineup_sabado[i])):
            if lineup_sabado[i][j] != "" and asistencia_sabado[i][j] == -2:
                asistencia_sabado[i][j] = -1

    for i in range(len(lineup_domingo)):
        for j in range(len(lineup_domingo[i])):
            if lineup_domingo[i][j] != "" and asistencia_domingo[i][j] == -2:
                asistencia_domingo[i][j] = -1

    return asistencia_sabado, asistencia_domingo, incidencias

def cargarUsuarios():
    dicUsuarios = {}
    try:
        with open("usuarios.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            numeroFila = 1
            for fila in lineas[1:]:
                numeroFila += 1
                if fila.strip() != "":
                    datos = fila.strip().split(",")

                    if len(datos) == 2 and datos[0] != "" and datos[1] != "":
                        registro = {
                            "usuario": datos[0],
                            "contraseña": datos[1]
                        }

                        usuario = registro["usuario"]
                        contraseña = registro["contraseña"]
                        dicUsuarios[usuario] = contraseña
                    else:
                        print(f"Error en la fila {numeroFila} de usuarios.csv.")

    except FileNotFoundError:
        print("Error: no se encontró usuarios.csv.")
        return None
    except OSError:
        print("Error: no se pudo leer usuarios.csv.")
        return None
    if len(dicUsuarios) == 0:
        print("Error: no hay usuarios registrados.")
        return None
    return dicUsuarios

def guardarReporte(reporte):
    try:
        with open("reporte.txt", "w", encoding="utf-8") as archivo:
            archivo.write(reporte)
        print("Reporte generado correctamente.")
    except OSError:
        print("Error: no se pudo generar reporte.txt.")