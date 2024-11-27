def promedio_de_salidas ( registro : dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    
    res : dict[str, tuple[int, float]] = dict()
    
    for amigo, tiempos in registro.items():
        
        res[amigo] = (cantidad_de_salidas_exitosas(tiempos), promedio_de_salidas_exitosas(tiempos))
    
    return res

def no_fue_al_juego_de_escape ( tiempo : int) -> bool:
    return tiempo == 0
 
def pudo_salir_del_juego_de_escape (tiempo : int) -> bool:
    return tiempo > 0 and tiempo < 61

def no_pudo_salir_del_juego_de_escape ( tiempo : int ) -> bool:
    return tiempo == 61

def cantidad_de_salidas_exitosas ( tiempos : list[int]) -> int:
    cantidad: int = 0
    
    for tiempo in tiempos:
        if pudo_salir_del_juego_de_escape(tiempo):
            cantidad += 1
    
    return cantidad
 
def tiempo_total_salidas_exitosas (tiempos : list[int]) -> int:
    
    lista : list[int] = []
    tiempo_total : int = 0
    
    for tiempo in tiempos:
        if pudo_salir_del_juego_de_escape(tiempo):
            lista.append(tiempo)       
        
    for elem in lista:
        tiempo_total += elem 
                
    return tiempo_total
 
def promedio_de_salidas_exitosas ( tiempos : list[int]) -> float:
        
    cantidad : int = cantidad_de_salidas_exitosas(tiempos)
    salidas : int = tiempo_total_salidas_exitosas(tiempos)
        
    print("CANTIDAD", cantidad, "SALIDAS", salidas)
        
    res : float = 0.0
    
    if cantidad > 0 and salidas > 0:
        res = salidas / cantidad
    
    return res
 
registro_test : dict[str, list[int]] = {
    "franco": [61, 40, 0],
    "micaela": [0,0,61],
    "carlitos": [20,20,20]
}

#print(promedio_de_salidas(registro_test))

# ---------------------------------------------------------------------------------------------------------------------

def tiempo_mas_rapido ( tiempo_salas : list[int]) -> int:
            
    menor : int = tiempo_salas[0]
    ubicacion : int = 0
    
    for i in range(len(tiempo_salas)):
        if pudo_salir_del_juego_de_escape(tiempo_salas[i]) and tiempo_salas[i] < menor:
            ubicacion = i
            menor = tiempo_salas[i]
     
    return ubicacion

 #print(tiempo_mas_rapido([30,0,25,10,61,0,4]))
  
# ---------------------------------------------------------------------------------------------------------------------

def racha_mas_larga ( tiempos : list[int]) -> tuple[int,int]:

    indiceActual:int = 0
    maxActual:int = 0
    maxTemporal:int = 0
    i:int = 0
    res:tuple[int, int] = ()
    
    while i < len(tiempos):
        if pudo_salir_del_juego_de_escape(tiempos[i]) and indiceActual == 0:
            indiceActual = i
            maxTemporal += 1
            i += 1
            
        elif pudo_salir_del_juego_de_escape(tiempos[i]) and indiceActual != 0:
            maxTemporal += 1
            i += 1
        elif maxActual < maxTemporal: 
            indiceActual = maxTemporal
            maxTemporal = 0
            indiceActual = i - maxActual
        elif pudo_salir_del_juego_de_escape(tiempos[i]) and indiceActual + maxTemporal < i:
            indiceActual = i
            maxTemporal += 1
            i += 1
        else:
            i += 1

        res = (indiceActual, indiceActual+maxActual)

    return res            
            
# ---------------------------------------------------------------------------------------------------------------------

def escape_en_solitario ( amigos_por_salas : list[list[int]]) -> list[int]:
    
    
    
    return


#Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los tiempos (en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), escribir una función en Python que devuelva los índices de todas las filas (que representan las salas) en las cuales el primer, segundo y cuarto amigo no fueron (0), pero el tercero sí fue (independientemente de si salió o no).
