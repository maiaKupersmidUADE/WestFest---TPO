import re

def validarContrasenia(contrasenia):
    patron = r"^#[A-Z][a-z]+[0-9]{3}$"
    if not re.match(patron, contrasenia):
        raise ValueError("La contraseña debe empezar con '#', seguido de una mayúscula, una o más minúsculas y terminar con tres números.")
    return True

def validarFormatoCodigo(codigo, prefijo):
    patron = "^" + prefijo + "[0-9]{2}$"
    if not re.match(patron, codigo):
        raise ValueError("Formato de código incorrecto.")

def validarLista(config, clave, campos):
    lista = config[clave]
    codigosVistos = []

    if len(lista) == 0:
        raise ValueError(f"'{clave}' debe ser una lista con al menos un elemento.")

    if clave == "artistas":
        prefijo = "A"
    elif clave == "escenarios":
        prefijo = "E"
    else:
        prefijo = "F"

    for item in lista:
        for campo in campos:
            if campo not in item or item[campo].strip() == "":
                raise ValueError(f"El campo '{campo}' de '{clave}' es inválido.")
        validarFormatoCodigo(item["codigo"], prefijo)

        if item["codigo"] in codigosVistos:
            raise ValueError(f"El código {item['codigo']} está repetido en '{clave}'.")
        codigosVistos.append(item["codigo"])

def validarConfiguracion(config):
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
        if capacidad <= 0:
            raise ValueError(f"La capacidad del escenario {escenario['codigo']} debe ser mayor a cero.")

    dias = config["dias"]
    if len(dias) != 2:
        raise ValueError("'dias' debe contener sábado y domingo.")
    if dias != ["sabado", "domingo"]:
        raise ValueError("'dias' debe contener sabado y domingo.")

def pedir_entero_positivo(mensaje):
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
    validarFormatoCodigo(codigo, "A")
    if codigo not in A:
        raise ValueError("El artista no existe.")
    return True

def validarCodigoEscenario(codigo, E):
    validarFormatoCodigo(codigo, "E")
    if codigo not in E:
        raise ValueError("El escenario no existe.")
    return True