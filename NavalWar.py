import random 
#creacion de tablero
tablero : list =[]
tamaño : int
def preguntarTamaño():
    try:
        tamaño=int(input("Cual va a ser el ancho y largo del tablero?"))
    except ValueError:
        print("Error:Ingrese un número")
        preguntarTamaño()
    if not (0 < tamaño < 100):
        print("Error: Ingrese un número entre 0 y 100")
        preguntarTamaño()
preguntarTamaño()
dibujo : list=[]
for fila in range(tamaño):
    columna:list=[]
    for i in range(tamaño):
        columna.append(False)
    tablero.append(columna)
#crear tablero dibujado
for y in range(tamaño):
    dibujofila: list = []
    for x in range(tamaño):
            dibujofila.append("🌊")
    dibujo.append(dibujofila)
#dibujar tablero
def dibujarTablero():
    for F in range(tamaño):
        print(dibujo[F])      



#barcos random
cantidad:int =int(input("Con Cuantos barcos jugas?"))
BarcosColocados = 0
def barcosRandom():
    n = len(tablero)
    while BarcosColocados<cantidad:
        fila = random.randiant(0,n - 1)
        columna = random.randiant(0,n-1)
        if not tablero[fila][columna]:
            tablero[fila][columna]= True
            colocados=+1




















#juego
cantidadTurnos:int=int(input("Con cuantos turnos vas a jugar?"))
listaDeTurnos:list=[]
turnosJugados=0
todo_falso:bool=True
while turnosJugados < cantidadTurnos:
    for y in range(tamaño):                               #chequea si ganaste
        for x in range(tamaño):
            if(tablero[y][x]):                           #si algo de la lista es true sale de los for y seguis
                todo_falso=False
                break
        if not todo_falso:
            break
    if todo_falso:                                              #pero si termina y todofalso sigue siendo true ganaste
        print("Ganaste!!")
        break
    else:
        try:
            Y:int=int(input("Ingrese cordenada y del disparo"))
            X:int=int(input("Ingrese cordenada x del disparo"))
        except ValueError:                                      #por si poner una palabra o cualquier otra cosa que no sea un numero
            print("Error: Solo puedes ingresar números.")
            continue
        if not (0 <= Y < tamaño) or not (0 <= X < tamaño):      #por si le pifias al tablero
            print("Coordenada fuera del tablero. Intenta otra vez.")
            continue
        codTurno:int=(Y*10)+X
        if(any(codTurno == turno for turno in listaDeTurnos)):  #si ese turno ya lo hiciste
            print("Ya jugaste este turno")
            continue                                            #continue lo que hace es que pasa a la siguiente vuelta del for eb el que esta ignorando el codigo de abajo
        if(tablero[Y][X]):                                      #si la coordenada que pusiste es true es un golpe
            print("Inpacto!!")
            tablero[Y][X]=False
            dibujo[Y][X]="💥"
        else:                                                   #si no es agua
            print("Agua")
            dibujo[Y][X]="💧"
        listaDeTurnos.append(codTurno)
        dibujarTablero()
        turnosJugados +=1                                       #solo si llega hasta aca abajo te cuenta el turno, si sale antes por un continue es como repetir ese turno
