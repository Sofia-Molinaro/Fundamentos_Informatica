#Se desea trabajar con una lista de equipos de fútbol. Se pide mostrar el equipo campeón, el equipo que más goles tuvo y el equipo que desciende de categoría(el que tiene menos puntos).

def armoLista(equipos):
   
    while True:   
        equipo = []
        nombreEquipo = input("Ingrese el nombre del equipo: ")
        if nombreEquipo == "0":
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
    for i in range(0, len(equipos)):
        if i == 0:
            equipoCampeon = equipos[i][0] # Nombre del primer equipo
            puntajeCampeon = equipos[i][2]
        else: 
            if equipos[i][2] > puntajeCampeon:
                equipoCampeon = equipos[i][0]
                puntajeCampeon = equipos[i][2]
                    
    return equipoCampeon

def goleador(equipos):
    #resulvo quien es el goleador
    #código
    #devuelvo el goleador
    for i in range (0, len(equipos)):
        if i == 0:
            equipoGoleador = equipos[i][0] # Nombre del primer equipo
            goleador = equipos[i][1]
        else:
            if equipos[i][0] > equipoGoleador:
                goleador = equipos[i][0] 
    return goleador

def desciende(equipos):
    #resuelvo que equipo desciende()
    #código
    #devuelvo el goleador
   for i in range(0, len(equipos)):
        if i == 0:
            equipoDesciende = equipos[i][0] # Nombre del primer equipo
            puntajeDesciende = equipos[i][2]
        else: 
            if equipos[i][2] < puntajeDesciende:
                equipoDesciende = equipos[i][0]
                puntajeDesciende = equipos[i][2]
        
        return equipoDesciende

equipos = []
print(f"Los equipos ingresados son: {armoLista(equipos)}")
print(f"Equipo Campeon: {campeon(equipos)}")
print(f"Equipo goleador: {goleador(equipos)}")
print(f"Equipo que desciende: {desciende(equipos)}")