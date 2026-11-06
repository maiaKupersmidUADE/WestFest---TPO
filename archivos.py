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

    with open("lineup.csv", "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            dia = fila["dia"].upper()
            codEscenario = fila["codigo_escenario"]
            codFranja = fila["codigo_franja"]
            codArtista = fila["codigo_artista"]

            if codEscenario not in dicEscenarios:
                raise ValueError(f"El escenario {codEscenario} no existe.")

            if codFranja not in dicFranjas:
                raise ValueError(f"La franja {codFranja} no existe.")

            if codArtista not in dicArtistas:
                raise ValueError(f"El artista {codArtista} no existe.")

            indiceEscenario = codigosEscenarios.index(codEscenario)
            indiceFranja = codigosFranjas.index(codFranja)

            if dia == "SABADO":
                lineup_sabado[indiceEscenario][indiceFranja] = codArtista
            elif dia == "DOMINGO":
                lineup_domingo[indiceEscenario][indiceFranja] = codArtista
            else:
                raise ValueError(f"El dia {dia} no es valido.")
    return lineup_sabado, lineup_domingo

def guardarLineUp(LUS, LUD, dicEscenarios, dicFranjas):
    with open("lineup.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow(["dia", "codigo_escenario", "codigo_franja", "codigo_artista"])

        codigosEscenarios = list(dicEscenarios.keys())
        codigosFranjas = list(dicFranjas.keys())

        # Guardar lineup del SABADO
        for i in range(len(LUS)):
            for j in range(len(LUS[i])):
                if LUS[i][j] != "":
                    escritor.writerow(["SABADO", codigosEscenarios[i], codigosFranjas[j], LUS[i][j]])

        # Guardar lineup del DOMINGO
        for i in range(len(LUD)):
            for j in range(len(LUD[i])):
                if LUD[i][j] != "":
                    escritor.writerow(["DOMINGO", codigosEscenarios[i], codigosFranjas[j], LUD[i][j]])