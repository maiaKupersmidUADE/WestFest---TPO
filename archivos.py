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

                        dia = datos[0].upper()
                        codEscenario = datos[1]
                        codFranja = datos[2]
                        codArtista = datos[3]

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

def cargarAsistencia(dicEscenarios, dicFranjas):
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
                        dia = datos[0].upper()
                        codEscenario = datos[1]
                        codFranja = datos[2]
                        textoAsistencia = datos[3]
                        
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
    except OSError:
        incidencias.append("No se pudo leer asistencias.csv.")

    return asistencia_sabado, asistencia_domingo, incidencias

def guardarAsistencia(AS, AD, dicEscenarios, dicFranjas):
    with open("asistencias.csv", "w", encoding="utf-8") as archivo:
        archivo.write("dia,codigo_escenario,codigo_franja,asistencia\n")
        codigosEscenarios = list(dicEscenarios.keys())
        codigosFranjas = list(dicFranjas.keys())
        for i in range(len(AS)):
            for j in range(len(AS[i])):
                if AS[i][j] != -2:
                    archivo.write("SABADO," + codigosEscenarios[i] + "," + codigosFranjas[j] + "," + str(AS[i][j]) + "\n")

        for i in range(len(AD)):
            for j in range(len(AD[i])):
                if AD[i][j] != -2:
                    archivo.write("DOMINGO," + codigosEscenarios[i] + "," + codigosFranjas[j] + "," + str(AD[i][j]) + "\n")