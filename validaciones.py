import re

def validarLista(config, clave, campos):
    lista = config[clave]
    codigosVistos = []

    if type(lista) != list or len(lista) == 0:
        raise ValueError(f"'{clave}' debe ser una lista con al menos un elemento.")

    for item in lista:
        if type(item) != dict:
            raise ValueError(f"Los elementos de '{clave}' deben ser diccionarios.")

        for campo in campos:
            if campo not in item or type(item[campo]) != str or item[campo].strip() == "":
                raise ValueError(f"El campo '{campo}' de '{clave}' es inválido.")

        if item["codigo"] in codigosVistos:
            raise ValueError(f"El código {item['codigo']} está repetido en '{clave}'.")

        codigosVistos.append(item["codigo"])


def validarConfiguracion(config):
    if type(config) != dict:
        raise ValueError("El archivo de configuración debe contener un objeto JSON.")

    for clave in ("artistas", "escenarios", "franjas", "dias"):
        if clave not in config:
            raise ValueError(f"Falta la clave '{clave}' en la configuración.")

    validarLista(config, "artistas", ("codigo", "nombre"))
    validarLista(config, "escenarios", ("codigo", "nombre"))
    validarLista(config, "franjas", ("codigo", "nombre"))

    for escenario in config["escenarios"]:
        if "capacidad_maxima" not in escenario:
            raise ValueError("Falta la capacidad máxima de un escenario.")
        capacidad = escenario["capacidad_maxima"]
        if type(capacidad) != int or capacidad <= 0:
            raise ValueError(f"La capacidad del escenario {escenario['codigo']} debe ser un entero mayor a cero.")

    dias = config["dias"]
    if type(dias) != list or len(dias) != 2:
        raise ValueError("'dias' debe contener sábado y domingo.")
    if dias != ["sabado", "domingo"]:
        raise ValueError("'dias' debe contener sabado y domingo.")

def pedir_entero_positivo(mensaje): # validar con pytest
    while True:
        try:
            num = int(input(mensaje))
            if num < 0:
                print("\nError: La cantidad de espectadores no puede ser negativa.")
            else:
                return num
        except ValueError:
            print("\nError: Debe ingresar un numero entero valido.")

def validarCodigoArtista(codigo, A):
    if not re.fullmatch(r"^A[0-9]{2}$", codigo):
        raise ValueError("Formato de código incorrecto.")

    if codigo not in A:
        raise ValueError("El artista no existe.")

    return True

def validarCodigoEscenario(codigo, E):
    if not re.fullmatch(r"^E[0-9]{2}$", codigo):
        raise ValueError("Formato de codigo incorrecto.")

    if codigo not in E:
        raise ValueError("El escenario no existe.")

    return True