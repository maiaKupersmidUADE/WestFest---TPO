import json
import validaciones
import csv

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
        with open("lineup.csv", "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo) #SACAR

            numeroFila = 1 #Definido asi por el encabezado del csv y que empiece por la segunda linea que son los datos
            for fila in lector:
                numeroFila +=1
                try:
                    dia = fila["dia"]
                    codEscenario = fila["codigo_escenario"]
                    codFranja = fila["codigo_franja"]
                    codArtista = fila["codigo_artista"]

                    if None in (dia, codEscenario, codFranja, codArtista):
                        raise ValueError("La fila está incompleta.")

                    dia = dia.upper()
                    if codEscenario not in dicEscenarios:
                        raise ValueError(f"El escenario {codEscenario} no existe.")

                    if codFranja not in dicFranjas:
                        raise ValueError(f"La franja {codFranja} no existe.")

                    if codArtista not in dicArtistas:
                        raise ValueError(f"El artista {codArtista} no existe.")
                
                    indiceEscenario = codigosEscenarios.index(codEscenario)
                    indiceFranja = codigosFranjas.index(codFranja)

                    if dia != "SABADO" and dia != "DOMINGO":
                        raise ValueError(f"El dia {dia} no es valido.")

                    if dia == "SABADO":
                        lineup_sabado[indiceEscenario][indiceFranja] = codArtista
                    else:
                        lineup_domingo[indiceEscenario][indiceFranja] = codArtista
                except ValueError as error:
                    incidencias.append(f"Fila {numeroFila} de lineup.csv: {error}")
    except FileNotFoundError:
        guardarLineUp(lineup_sabado, lineup_domingo, dicEscenarios, dicFranjas)
        incidencias.append("No se encontró lineup.csv, se creó un archivo nuevo vacío.")
    except KeyError:
        incidencias.append("Al encabezado de lineup.csv le faltan columnas.")
    except OSError:
        incidencias.append("No se pudo leer lineup.csv.")

    return lineup_sabado, lineup_domingo, incidencias

def guardarLineUp(LUS, LUD, dicEscenarios, dicFranjas):
    with open("lineup.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo) #writer?

        escritor.writerow(["dia", "codigo_escenario", "codigo_franja", "codigo_artista"]) #writerowwww??

        codigosEscenarios = list(dicEscenarios.keys())
        codigosFranjas = list(dicFranjas.keys())

        # Guardar lineup del SABADO
        for i in range(len(LUS)):
            for j in range(len(LUS[i])):
                if LUS[i][j] != "":
                    escritor.writerow(["SABADO", codigosEscenarios[i], codigosFranjas[j], LUS[i][j]]) # ACA LO MISMO

        # Guardar lineup del DOMINGO
        for i in range(len(LUD)):
            for j in range(len(LUD[i])):
                if LUD[i][j] != "":
                    escritor.writerow(["DOMINGO", codigosEscenarios[i], codigosFranjas[j], LUD[i][j]])  # ACA LO MISMO

def cargarAsistencia(dicEscenarios, dicFranjas):
    asistencia_sabado = [[-2 for j in range(len(dicFranjas))] for i in range(len(dicEscenarios))]
    asistencia_domingo = [[-2 for j in range(len(dicFranjas))] for i in range(len(dicEscenarios))]

    codigosEscenarios = list(dicEscenarios.keys())
    codigosFranjas = list(dicFranjas.keys())
    incidencias = []

    try:
        with open("asistencias.csv", "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo) # DICT

            numeroFila = 1  # el encabezado es la línea 1, los datos empiezan en la 2
            for fila in lector:
                numeroFila += 1
                try:
                    dia = fila["dia"]
                    codEscenario = fila["codigo_escenario"]
                    codFranja = fila["codigo_franja"]
                    textoAsistencia = fila["asistencia"]

                    if None in (dia, codEscenario, codFranja, textoAsistencia):
                        raise ValueError("La fila está incompleta.")

                    dia = dia.upper()

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
                    else:
                        grilla = asistencia_domingo

                    if grilla[indiceEscenario][indiceFranja] != -2:
                        raise ValueError("Esa posición está repetida en el archivo.")

                    grilla[indiceEscenario][indiceFranja] = asistencia

                except ValueError as error:
                    incidencias.append(f"Fila {numeroFila} de asistencias.csv: {error}")

    except FileNotFoundError:
        guardarAsistencia(asistencia_sabado, asistencia_domingo, dicEscenarios, dicFranjas)
        incidencias.append("No se encontró asistencias.csv, se creó un archivo nuevo vacío.")
    except KeyError:
        incidencias.append("Al encabezado de asistencias.csv le faltan columnas.")
    except OSError:
        incidencias.append("No se pudo leer asistencias.csv.")

    return asistencia_sabado, asistencia_domingo, incidencias

def guardarAsistencia(AS, AD, dicEscenarios, dicFranjas):
    with open("asistencias.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["dia", "codigo_escenario", "codigo_franja", "asistencia"]) # aca tambien sacar

        codigosEscenarios = list(dicEscenarios.keys())
        codigosFranjas = list(dicFranjas.keys())

        for i in range(len(AS)):
            for j in range(len(AS[i])):
                if AS[i][j] != -2:
                    escritor.writerow(["SABADO", codigosEscenarios[i], codigosFranjas[j], AS[i][j]])

        for i in range(len(AD)):
            for j in range(len(AD[i])):
                if AD[i][j] != -2:
                    escritor.writerow(["DOMINGO", codigosEscenarios[i], codigosFranjas[j], AD[i][j]])