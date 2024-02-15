import sys

bool = True

while bool:
    try:
        jugador1 = input("Jugador 1: ")
        jugador2 = input("Jugador 2: ")
        numSets = 3
        bool = False
    except:
        print("La entrada debe ser una cadena")

puntos1 = 0
puntos2 = 0
juegos1 = 0
juegos2 = 0
sets1 = 0
sets2 = 0

saque = jugador1

def aumentaPuntos(jugador):
    global puntos1 
    global puntos2

    if jugador == jugador1:
        if puntos1 < 30:
            puntos1 += 15
        elif puntos1 < 40:
            puntos1 += 10
        elif puntos1 == 40:
            if puntos2 == "Adv.":
                puntos2 = 40
            else:
                puntos1 = "Adv."
    else:
        if puntos2 < 30:
            puntos2 += 15
        elif puntos2 < 40:
            puntos2 += 10
        elif puntos2 == 40:
            if puntos1 == "Adv.":
                puntos1 = 40
            else:
                puntos2 = "Adv."


def vaAGanar(jugador):
    if jugador == jugador1:
        if puntos1 == "Adv.":
            return True
        elif puntos1 < 40:
            return False
        else:
            return puntos2 != "Adv." and puntos2 < 40
    else:
        if puntos2 == "Adv.":
            return True
        elif puntos2 < 40:
            return False
        else:
            return puntos1 != "Adv." and puntos1 < 40


def ganaJuego(jugador):
    global juegos1
    global juegos2
    global puntos1 
    global puntos2
    global saque

    juegos = 0

    if jugador == jugador1:
        juegos1 += 1
        juegos = juegos1
    else:
        juegos2 += 1
        juegos = juegos2

    puntos1 = 0
    puntos2 = 0

    if saque == jugador1:
        saque = jugador2
    else:
        saque = jugador1



    print(jugador + " ganó el juego")
    print("Juegos: " + str(juegos1) + "-" + str(juegos2))

    if (juegos1 + juegos2) % 2 != 0:
        print("Cambio de cancha")

    if juegos >= 6 and abs(juegos1 - juegos2) >= 2:
        ganaSet(jugador)


def ganaSet(jugador):
    global sets1
    global sets2
    global juegos1
    global juegos2
    global puntos1 
    global puntos2
    global saque

    sets = 0

    if jugador == jugador1:
        sets1 += 1
        sets = sets1
    else:
        sets2 += 1
        sets = sets2

    puntos1 = 0
    puntos2 = 0
    juegos1 = 0
    juegos2 = 0

    print(jugador + " ganó el set")
    print("Sets: " + str(sets1) + "-" + str(sets2))


    if sets > numSets / 2:
        print(jugador + " ganó el partido")
        sys.exit()







while True:
    print ("Marcador: " + str(puntos1) + "-" + str(puntos2))
    print(saque + " saca")

    hizoPunto = input("¿Quién hizo el punto? ")
    if hizoPunto == jugador1 or hizoPunto == jugador2:
        print (hizoPunto + " ganó el punto")
        if not vaAGanar(hizoPunto):
            aumentaPuntos(hizoPunto)
        else:
            ganaJuego(hizoPunto)
    else:
        print("Jugador no encontrado")




