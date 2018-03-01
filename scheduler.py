from parser import getInput

# Calcula si el coche puede realizar ese viaje
def arriveOnTime(xCar,yCar,xStart,yStart,xEnd,yEnd,t,tEnd):
  distCarStart = abs(xStart - xCar) + abs(yStart - yCar)
  distStartEnd = abs(xEnd - xStart) + abs(yEnd - yStart)

  tRide = distCarStart + distStartEnd
  tAvaiable = tEnd - t

  return tAvaiable > tRide

# Puntuacion de tomar ese viaje
def stepScore(xCar,yCar,xStart,yStart,xEnd,yEnd,t,tStart,bonus):
    distCarStart = abs(xStart - xCar) + abs(yStart - yCar)
    distStartEnd = abs(xEnd - xStart) + abs(yEnd - yStart)

    tEspera = tStart - (t + distCarStart)
    if tEspera < 0:
        tEspera = 0

    return distCarStart + tEspera - distStartEnd - bonus

# Funcion que devuelve el tiempo a sumar al tiempo actual
def newTime(xCar,yCar,xStart,yStart,xEnd,yEnd,t,tStart):
    distCarStart = abs(xStart - xCar) + abs(yStart - yCar)
    distStartEnd = abs(xEnd - xStart) + abs(yEnd - yStart)

    tEspera = tStart - (t + distCarStart)
    if tEspera < 0:
        tEspera = 0

    return distCarStart + tEspera + distStartEnd

# MAIN
if __name__ == "__main__" :
    parsed = getInput("a_example.in")

    schedule = []
    position = []

    # Inicializar schedule
    for x in range(parsed[0][2]):
        schedule.append([])

    # Incializar coordenadas a 0,0 y T de cada vehiculo a 0
    for x in range(parsed[0][2]):
        position.append((0,0,0))

    while parsed[1]:    # Mientras queden viajes disponibles
        for vehicle in range(parsed[0][2]):     # Para cada vehiculo
            auxRide = None
            auxTime = None
            for ride in parsed[1]:   # Para cada viaje
                if arriveOnTime(position[vehicle][0], position[vehicle][1], ride[0], ride[1], ride[2], ride[3], position[vehicle][2], ride[5]):
                    if auxRide == None:
                        auxRide = ride   # Guardamos el ID del viaje
                        auxTime = stepScore(position[vehicle][0], position[vehicle][1],ride[0], ride[1], ride[2], ride[3], position[vehicle][2], ride[4], parsed[0][4])
                    else:
                        currentTime = stepScore(position[vehicle][0], position[vehicle][1],ride[0], ride[1], ride[2], ride[3], position[vehicle][2], ride[4], parsed[0][4])
                        if currentTime < auxTime:
                            auxRide = ride
                            auxTime = currentTime

            schedule[vehicle].append[auxRide[6]]
            position[vehicle][0] = auxRide[2]
            position[vehicle][1] = auxRide[3]
            position[vehicle][2] += newTime(position[vehicle][0], position[vehicle][1],auxRide[0], auxRide[1], auxRide[2], auxRide[3], position[vehicle][2], auxRide[4])

            parsed[1].pop(auxRide)  # Quitamos el viaje de la lista de viajes disponibles
