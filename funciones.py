def asignarLineUp():
    pass

def consultarLineUp(LUS, LUD, E, A, H):
    for i in range(len(LUS)):
        for j in range(len(LUS[i])):
            print(f"Sabado {H[j][1]}: nombre en el escenario {E[i][1]}")

            ### FORMATEAR LA SALIDA

def buscarArtista(artistas):
    codigo = input("Ingrese el código del artista a buscar: ")
    encontrado = None
    for artista in artistas:
        if artista[0] == codigo:
            encontrado = artista

    return encontrado
            

def registrarAsistencia(): 
    pass

def modificarAsistencia():
    pass

def consultarArtistaMayorConvocatoria():
    pass

def consultarAsistenciaTotalPorDia():
    pass

def consultarTop3ArtistasMayorConvocatoria():
    pass

def consultarShowsSobrepasaronCapacidad():
    pass

def consultarTop3FranjasHorariasMayorAsistencia():
    pass

def mostrarRankingArtistas():
    pass