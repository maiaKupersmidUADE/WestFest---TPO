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