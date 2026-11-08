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
    
    resultado = funciones.obtenerTotal(matriz)

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

    assert resultado == [("A01", 300), ("A02", 50)]

def test_detectar_capacidad_superada():
    pass