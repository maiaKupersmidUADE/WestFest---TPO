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