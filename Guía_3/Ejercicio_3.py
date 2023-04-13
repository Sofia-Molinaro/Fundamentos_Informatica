#Se desea trabajar con una lista de equipos de fútbol. Se pide mostrar el equipo campeón, el equipo que más goles tuvo y el equipo que desciende de categoría(el que tiene menos puntos).

def armoLista(equipo, equipos):
    equipos = []
    equipo = []
    
    nombreEquipo = input("Ingrese el nombre del equipo: ")
    
    while nombreEquipo == " ":   
        if nombreEquipo == 0:
            break
        equipo.append(nombreEquipo)
        golesEquipo = int(input(f"Goles 👉 {nombreEquipo}: "))
        equipo.append(golesEquipo)
        puntajeEquipo =int(input(f"Puntaje 👉 {nombreEquipo}: "))
        equipo.append(puntajeEquipo)
    
        equipos.append(equipo)
    return equipos

def campeon(equipos):
    #resuelve quien es el campeon
    #código
    # luego retorno el resultado
    for i in range (0, len(equipos)):
        if equipos[0][2]> equipoCampeon:
            equipoCampeon = equipos[0][2]
        else: 
            if equipos[i][2] > equipoCampeon:
                equipoCampeon = equipos[i][2]
                    
    return equipoCampeon

def goleador(equipos):
    #resulvo quien es el goleador
    #código
    #devuelvo el goleador
    for i in equipos:
        if equipos[0][1]> equipoGoleador:
            equipoGoleador = equipos [0][1]
        else:
            if equipos[i][0] > equipoGoleador:
                equipoGoleador = equipos[i][0] 
    return equipoGoleador

def desciende(equipos):
    #resuelvo que equipo desciende()
    #código
    #devuelvo el goleador
    for i in equipos:
        if equipos[0][1] < equipoDesciende:
            equipoDesciende = equipos [0][1]
        else:
            if equipos[i][0] < equipoDesciende:
                equipoDesciende = equipos[i][0] 
    return equipoDesciende

equipos = []
print(f"Los equipos ingresados son: {equipos}")
print(f"Equipo Campeon: {campeon(equipos)}")
print(f"Equipo goleador: {goleador(equipos)}")
print(f"Equipo que desciende: {desciende(equipos)}")