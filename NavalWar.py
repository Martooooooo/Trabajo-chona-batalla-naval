#creacion de tablero
tablero : list =[];
tamaño : int=int(input("Cual va a ser el ancho y largo del tablero?"));
for fila in range(tamaño):
    columna:list=[]
    for i in range(tamaño):
        columna.append(False)
    tablero.append(columna)
    print(tablero[fila])










#barcos random





















#juego