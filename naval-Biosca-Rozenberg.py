import random 
#creacion de tablero
tablero : list =[]
def preguntarTamanio():
    try:
        tam: int =  int(input("Cual va a ser el ancho y largo del tablero?"))
        if not (0 < tam < 100):
            print("Error: Ingrese un número entre 0 y 100")
            return preguntarTamanio()
        return tam
    except ValueError:
        print("Error:Ingrese un número")

        return preguntarTamanio()

tamanio : int = preguntarTamanio()

dibujo : list=[]
for fila in range(tamanio):
    columna:list=[]
    for i in range(tamanio):
        columna.append(False)
    tablero.append(columna)
#crear tablero dibujado
for y in range(tamanio):
    dibujofila: list = []
    for x in range(tamanio):
            dibujofila.append("🌊")
    dibujo.append(dibujofila)
#dibujar tablero
def dibujarTablero():
    for F in range(tamanio):
        print(dibujo[F])      



#barcos random
cantidad:int =int(input("Con Cuantos barcos jugas?"))               #https://www.w3schools.com/python/ref_random_randint.asp
def barcosRandom():
    global BarcosColocados
    BarcosColocados = 0
    n = len(tablero)
    while BarcosColocados < cantidad:
        fila = random.randint(0, n - 1)
        columna = random.randint(0, n - 1)
        if not tablero[fila][columna]:
            tablero[fila][columna] = True
            BarcosColocados += 1

barcosRandom()

#juego
def preguntarTurnos():
    try:
        tur: int =  int(input("Con cuantos turnos vas a jugar?"))
        if not (0 < tur < 100):
            print("Error: Ingrese un número entre 0 y 100")
            return preguntarTurnos()
        return tur
    except ValueError:
        print("Error:Ingrese un número")

        return preguntarTurnos()

cantidadTurnos : int = preguntarTurnos()

listaDeTurnos:list=[]
turnosJugados=0
disparosPegados:int=0
disparosErrados:int=0
while turnosJugados < cantidadTurnos:                           #https://chatgpt.com/share/68019038-b230-8008-834d-3f1e10a80132
    try:
        Y:int=int(input("Ingrese cordenada y del disparo"))-1
        X:int=int(input("Ingrese cordenada x del disparo"))-1
    except ValueError:                                      #por si poner una palabra o cualquier otra cosa que no sea un numero
        print("Error: Solo puedes ingresar números.")
        continue
    if not (0 <= Y < tamanio) or not (0 <= X < tamanio):      #por si le pifias al tablero
        print("Coordenada fuera del tablero. Intenta otra vez.")
        continue
    codTurno:int=(Y*10)+X
    if(any(codTurno == turno for turno in listaDeTurnos)):  #si ese turno ya lo hiciste
        print("Ya jugaste este turno")
        continue                                            #continue lo que hace es que pasa a la siguiente vuelta del for eb el que esta ignorando el codigo de abajo
    if(tablero[Y][X]):                                      #si la coordenada que pusiste es true es un golpe
        print("Impacto!!")
        tablero[Y][X]=False
        dibujo[Y][X]="💥"
        disparosPegados+=1
    else:                                                   #si no es agua
        print("Agua")
        dibujo[Y][X]="💧"
        disparosErrados+=1
    listaDeTurnos.append(codTurno)
    dibujarTablero()
    turnosJugados +=1                                       #solo si llega hasta aca abajo te cuenta el turno, si sale antes por un continue es como repetir ese turno
    todo_falso:bool=True
    for y in range(tamanio):                               #chequea si ganaste
        for x in range(tamanio):
            if(tablero[y][x]):                           #si algo de la lista es true sale de los for y seguis
                todo_falso=False
                break
        if not todo_falso:
            break
    if todo_falso:                                              #pero si termina y todofalso sigue siendo true ganaste
        print("Ganaste!!")
        break
print(f"Pegaste: {disparosPegados} disparos")
print(f"Erraste: {disparosErrados} disparos")
for fila in range(tamanio):                                #dibuja el tablero con los barcos que te faltaron si te faltaron
    for casilla in range(tamanio):
        if(tablero[fila][casilla]):
            dibujo[fila][casilla]="🚢"
dibujarTablero()
if not todo_falso:
    print("perdiste :(")
