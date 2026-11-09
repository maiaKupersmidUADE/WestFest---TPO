import pytest
import validaciones
import funciones

def test_validar_codigo_artista_correcto():
    artistas = {
        "A01": "Lady Gaga",
        "A02": "50 pesos",
        "A03": "Me robaron entre 5",
        "A04": "Miley Ciruja",
        "A05": "21 pilotos de Ezeiza",
        "A06": "Los kioskeros",
        "A07": "El finde",
        "A08": "Cano del Oeste",
        "A09": "Red Hot Chori Peppers",
        "A10": "Paco Odioso",
        "A11": "Ariana Chiquita",
        "A12": "Conejo Malo"    
    }

    resultado = validaciones.validarCodigoArtista("A01", artistas)

    assert resultado == True

def test_validar_codigo_escenario_incorrecto():
    escenarios = {
        "E01": "Main Stage",
        "E02": "Electronic Arena",
        "E03": "Mata Club"
    }

    with pytest.raises(ValueError):
        validaciones.validarCodigoEscenario("X01", escenarios)

def test_obtener_total_ignorar_asistencias_sin_registrar():
    matriz = [
        [100, -1, 0],
        [-2, 250, 50]
    ]
    
    resultado = funciones.obtenerTotalRecursivo(matriz)

    assert resultado == 400

def test_obtener_convocatorias_acumula_por_artista():
    artistas = {
        "A01": "Lady Gagá",
        "A02": "50 pesos"
    }

    lineup_sabado = [
        ["A01", "A02"]
    ]

    lineup_domingo = [
        ["A01", ""]
    ]

    asistencia_sabado = [
        [100, 50]
    ]

    asistencia_domingo = [
        [200, -2]
    ]

    resultado = funciones.obtenerConvocatorias(
        artistas,
        lineup_sabado,
        lineup_domingo,
        asistencia_sabado,
        asistencia_domingo
    )

    assert resultado == {"A01": 300, "A02": 50}
    
def test_detectar_capacidad_superada():
    A = {
        "A01": "Lady Gagá",
        "A02": "50 pesos"
    }

    E = {
        "E01": {
            "nombre": "Main Stage",
            "capacidad_maxima": 5000
        }
    }

    H = {
        "F01": "Mediodia",
        "F02": "Tarde",
        "F03": "Noche"
    }
    LUS = [["A01", "A02", ""]]
    LUD = [["", "", ""]]

    AS = [[5500, 4000, -2]]
    AD = [[-2, -2, -2]]

    resultado = funciones.consultarShowsSobrepasaronCapacidad(
        A, LUS, LUD, AS, AD, E, H
    )

    esperado = [
        ("SABADO", "Main Stage", "Mediodia", "Lady Gagá", 5500)
    ]

    assert resultado == esperado

def test_diferenciar_asistencia_pendiente_y_cero():
    A = {
        "A01": "Lady Gagá",
        "A02": "50 pesos"
    }

    E = {
        "E01": {
            "nombre": "Main Stage",
            "capacidad_maxima": 5000
        }
    }

    H = {
        "F01": "Mediodia",
        "F02": "Tarde",
        "F03": "Noche"
    }

    LUS = [["A01", "A02", ""]]
    LUD = [["", "", ""]]

    AS = [[-1, 0, -2]]
    AD = [[-2, -2, -2]]

    resultado = funciones.consultarShowsSinAsistencia(
        A, LUS, LUD, AS, AD, E, H
    )

    esperado = [
        ("SABADO", "Main Stage", "Mediodia", "Lady Gagá")
    ]

    assert resultado == esperado

def test_asistencia_igual_a_capacidad_maxima():
    A = {
        "A01": "Lady Gagá"
    }

    E = {
        "E02": {
            "nombre": "Electronic Arena",
            "capacidad_maxima": 3000
        }
    }

    H = {
        "F01": "Mediodia"
    }

    LUS = [["A01"]]
    LUD = [[""]]

    AS = [[3000]]
    AD = [[-2]]

    resultado = funciones.consultarShowsSobrepasaronCapacidad(
        A, LUS, LUD, AS, AD, E, H
    )

    assert resultado == []