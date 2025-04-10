import random 
#creacion de tablero
tablero : list =[];
tamaño : int=int(input("Cual va a ser el ancho y largo del tablero?"));
for fila in range(tamaño):
    columna:list=[]
    for i in range(tamaño):
        columna.append(False)
    tablero.append(columna)
    print(tablero[fila])
#tablero dibujado
for y in range(tablero):
    for x in range(tablero[y]):
        dibujo:list=[]
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