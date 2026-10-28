WestFest es un sistema que permite gestionar el line up de un festival, registrar la asistencia de los distintos shows y obtener información sobre la convocatoria. El festival se desarrolla durante los días sábado y domingo, cuenta con diferentes escenarios y franjas horarias, y cada combinación de escenario y horario puede tener un artista asignado. El sistema permite administrar esta información y generar distintos informes a partir de las asistencias registradas.

## Objetivos
- Gestionar el line up del festival.
- Asignar y modificar artistas.
- Consultar la programación de cada día.
- Buscar artistas dentro del line up.
- Registrar y modificar la asistencia de los shows.
- Obtener estadísticas de convocatoria.
- Identificar los shows que superaron la capacidad máxima de los escenarios.

## Datos del festival
- Días:
* Sábado
* Domingo

- Franjas horarias:
* Mediodía
* Tarde
* Noche

Escenarios:
* Main Stage
* Electronic Arena
* Mata Club

La capacidad máxima de los escenarios es gereal y de 1000 espectadores.

## Artistas
Los artistas se identifican mediante un código único.
| Código | Artista               |
| -----  | --------------------- |
|   A01  | Lady Gagáa            |
|   A02  | 50 pesos              |
|   A03  | Me robaron entre 5    |
|   A04  | Miley Ciruja          |
|   A05  | 21 pilotos de Ezeiza  |
|   A06  | Los kioskeros         |
|   A07  | El finde              |
|   A08  | Cano del Oeste        |
|   A09  | Red Hot Chori Peppers |
|   A10  | Paco Odioso           |
|   A11  | Ariana Chiquita       |
|   A12  | Conejo Malo           |

## Funcionalidades
El sistema cuenta con las siguientes opciones:

1. Asignar / Modificar Line Up:
Permite asignar un artista a un día, escenario y franja horaria.

Se valida que:
* El artista exista.
* El día sea válido.
* El horario exista.
* El escenario exista.
* El lugar seleccionado esté disponible.
* El artista no esté asignado a otro escenario en el mismo horario.

2. Consultar Line Up
Muestra la programación completa del festival para sábado y domingo, indicando los artistas asignados a cada escenario y franja horaria.

3. Buscar artista
Permite buscar un artista mediante su código y consultar:
* Día de presentación.
* Escenario.
* Franja horaria.

4. Registrar asistencia
Permite registrar la cantidad de espectadores de un show. Se controla que la cantidad ingresada no sea negativa y que el show tenga un artista asignado. También se informa cuando la asistencia supera la capacidad máxima del escenario.

5. Modificar asistencia
Permite modificar la cantidad de espectadores de un show que ya posee una asistencia registrada.

6. Artista con mayor convocatoria
Muestra el artista que acumuló la mayor cantidad de espectadores considerando sus presentaciones durante ambos días.

7. Asistencia total por día
Muestra la cantidad total de espectadores registrados para el sábado y para el domingo.

8. Top 3 de artistas con mayor convocatoria
Genera un ranking con los tres artistas que tuvieron mayor convocatoria durante el festival.

9. Shows que superaron la capacidad
Muestra los shows cuya cantidad de espectadores superó la capacidad máxima del escenario.

Para cada show se informa:
* Escenario.
* Horario.
* Artista.
* Cantidad de espectadores.

10. Top 3 de franjas horarias con mayor asistencia
Calcula la asistencia total de cada franja horaria considerando ambos días y muestra las tres franjas con mayor convocatoria.

## Estructura de datos
franjas = [
    ("F01", "Mediodia"),
    ("F02", "Tarde"),
    ("F03", "Noche")
]

escenarios = [
    ("E01", "Main Stage"),
    ("E02", "Electronic Arena"),
    ("E03", "Mata Club")
]

Se utilizan dos matrices, una para cada día:
- lineup_sabado
- lineup_domingo
Las filas representan los escenarios y las columnas representan las franjas horarias.

Se utilizan dos matrices relacionadas con cada line up:
asistencia_sabado
asistencia_domingo

Los valores utilizados son:
|    Valor    | Significado                                           |
| :---------: | ----------------------------------------------------- |
|     `-2`    | No hay artista asignado                               |
|     `-1`    | Hay un show pero todavía no se registró la asistencia |
| `0` o mayor | Cantidad de espectadores registrada                   |

### `menu.py`
Contiene:
* Los datos iniciales del festival.
* Las matrices del line up.
* Las matrices de asistencia.
* El menú principal.
* La interacción con el usuario.

### `funciones.py`
Contiene las funciones encargadas de:
* Gestionar el line up.
* Buscar artistas.
* Registrar asistencias.
* Modificar asistencias.
* Calcular convocatorias.
* Generar rankings.
* Generar informes.

## Validaciones
El sistema valida diferentes situaciones para evitar datos incorrectos:
* Código de artista inexistente.
* Día inválido.
* Franja horaria inexistente.
* Escenario inexistente.
* Lugar del line up ocupado.
* Artista asignado a otro escenario en el mismo horario.
* Cantidad de espectadores negativa.
* Registro de asistencia en un show inexistente.
* Modificación de una asistencia que todavía no fue registrada.

## Informes
A partir de las asistencias registradas, el sistema permite obtener:
* Artista con mayor convocatoria.
* Asistencia total del sábado.
* Asistencia total del domingo.
* Top 3 de artistas con mayor convocatoria.
* Shows que superaron la capacidad máxima.
* Top 3 de franjas horarias con mayor asistencia.


# ALCANCE SEGUNDA ETAPA 

# WestFest — Sistema de gestión de festivales

## Descripción del proyecto

WestFest es un sistema desarrollado en Python para gestionar la programación y la asistencia de un festival musical de dos días (sábado y domingo).

El sistema permite administrar el lineup, registrar la cantidad de espectadores por presentación, consultar información de los artistas y generar estadísticas e informes para facilitar el seguimiento de la organización del festival.

Este proyecto forma parte de la segunda etapa del Proyecto Integrador de Programación I, orientada a la incorporación de persistencia de datos, validaciones, manejo de excepciones y pruebas unitarias.

## Funcionalidades principales

- **Autenticación:** acceso mediante usuario y contraseña.
- **Gestión del lineup:** asignar, modificar y consultar artistas por día, escenario y franja horaria.
- **Búsqueda de artistas:** consultar todas las presentaciones de un artista durante el festival.
- **Gestión de asistencias:** registrar y modificar la cantidad de espectadores de cada show.
- **Estadísticas e informes:**
  - Artista con mayor convocatoria.
  - Asistencia total por día.
  - Top 3 de artistas con mayor convocatoria.
  - Top 3 de combinaciones de día y franja horaria con mayor asistencia.
  - Shows que superaron la capacidad máxima de su escenario.
- **Alertas:** detección de asistencias pendientes, capacidades superadas y registros inconsistentes.
- **Generación de reportes:** creación de un archivo de texto con resultados e incidencias.

## Archivos del sistema

El proyecto utiliza distintos archivos para separar la configuración, los datos persistentes y los reportes.

| Archivo | Descripción |
|---|---|
| `configuracion.json` | Contiene los artistas, escenarios, franjas horarias y capacidades máximas. |
| `usuarios.csv` | Almacena las credenciales necesarias para acceder al sistema. |
| `lineup.csv` | Guarda la programación de los shows. |
| `asistencias.csv` | Registra la cantidad de espectadores por presentación. |
| `reporte.txt` | Contiene estadísticas, alertas e incidencias detectadas. |

Los archivos CSV permiten conservar la información entre ejecuciones. Al iniciar el programa, se recuperan los datos almacenados y se utilizan para reconstruir las estructuras necesarias.

El archivo `configuracion.json` es obligatorio. Si falta o contiene información inválida, el sistema informa el error y finaliza la ejecución sin sobrescribirlo.

## Tecnologías y conceptos aplicados

- **Python:** lenguaje de programación utilizado para desarrollar el sistema.
- **Listas y matrices:** representación del lineup y las asistencias por escenario y franja horaria.
- **Diccionarios:** búsquedas por código y acumulación de asistencias por artista.
- **Expresiones regulares (`re`):** validación de los formatos de los códigos de artistas y escenarios.
- **Archivos JSON y CSV:** configuración y persistencia de datos.
- **Archivos de texto:** generación de reportes y alertas.
- **Manejo de excepciones:** control de errores de lectura, escritura, datos inválidos y archivos inexistentes.
- **Pruebas unitarias (`pytest`):** verificación automática de las funciones principales.

### Valores utilizados para las asistencias

La matriz de asistencia distingue los siguientes estados:

| Valor | Significado |
|---|---|
| `-2` | No existe un show asignado. |
| `-1` | Show asignado, con asistencia pendiente de registrar. |
| `0` | Show realizado con cero espectadores registrados. |
| Mayor que `0` | Cantidad de espectadores registrada. |

Esta distinción permite calcular correctamente las estadísticas y detectar presentaciones con información pendiente.

## Pruebas unitarias

El proyecto contempla siete pruebas unitarias para verificar las principales reglas y cálculos del sistema:

1. Validación correcta del código de artista.
2. Rechazo de códigos de escenario con formato incorrecto.
3. Cálculo de asistencia total, excluyendo los valores `-1` y `-2`.
4. Acumulación de asistencias por artista.
5. Detección de shows que superan la capacidad del escenario.
6. Diferenciación entre asistencia pendiente (`-1`) y cero espectadores (`0`).
7. Verificación del caso límite en el que la asistencia es exactamente igual a la capacidad máxima.

Las pruebas se ejecutan con `pytest` y no deben depender del ingreso de datos por teclado ni de los mensajes mostrados en pantalla.
