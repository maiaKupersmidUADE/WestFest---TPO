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