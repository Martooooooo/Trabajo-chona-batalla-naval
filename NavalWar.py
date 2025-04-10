import random 
#creacion de tablero
tablero : list =[];
tamaño : int=int(input("Cual va a ser el ancho y largo del tablero?"));
for fila in range(tamaño):
    columna:list=[]
    for i in range(tamaño):
        columna.append(False)
    tablero.append(columna)
#tablero dibujado
for y in range(len(tablero)):
    dibujo: list = []
    for x in range(len(tablero[y])):
            dibujo.append("🌊")
    print(dibujo)








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
turnoActual:int=0
for t in range(cantidadTurnos):
    #chequea si ganaste
    todo_falso=True
    for y in range(len(tablero)):
        for x in range(tablero[y]):
            #si algo de la lista es true sale de los for y seguis 
            #pero si termina y todofalso sigue siendo true ganaste
            if(tablero[y][x]!=False):
                todo_falso=False
                break
        if not todo_falso:
            break
    if todo_falso:
        print("Ganaste!!")
        break
    else:

    