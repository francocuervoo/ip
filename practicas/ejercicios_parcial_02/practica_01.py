from queue import Queue as Cola

def torneo_de_gallinas ( estrategias : dict[str, str]) -> dict[str, int]:
    res : dict[str, int] = dict()  

    for jugador1 , estrategia1 in estrategias.items():
        res[jugador1] = 0
        
        for jugador2, estrategia2 in estrategias.items():
            if not jugador1 == jugador2:
                if estrategia1 == "me desvio siempre" and estrategia1 == estrategia2:
                    res[jugador1] += -10
                elif estrategia1 == "me la banco y no me desvio" and estrategia1 == estrategia2:
                    res[jugador1] += -5
                elif estrategia1 == "me desvio siempre" and estrategia2 == "me la banco y no me desvio":
                    res[jugador1] += -15
                elif estrategia1 == "me la banco y no me desvio" and estrategia2 == "me desvio siempre":
                    res[jugador1] += 10
    
    return res

estrategiasTest : dict[str, str] = {
    "franco": "me desvio siempre",
    "micaela": "me la banco y no me desvio",
    "juan": "me desvio siempre",
    "pedro": "me desvio siempre",
    "camila": "me la banco y no me desvio",
}

#print(torneo_de_gallinas(estrategiasTest))

# ------------------------------------------------------------------------

def reordenar_cola_priorizando_vips ( filaClientes : Cola[tuple[str, str]]) -> Cola[str]:
    
    cola_back_up = Cola()
    cola_procesada = Cola()
        
    res = Cola()
    
    while not filaClientes.empty():        
        cliente = filaClientes.get()
        cola_back_up.put(cliente)
        
        if cliente[1] == "vip":
            res.put(cliente[0])
        
        else:
            cola_procesada.put(cliente[0])
        
    while not cola_procesada.empty():
        nombre = cola_procesada.get()
        res.put(nombre)
    
    while not cola_back_up.empty():
        filaClientes.put(cola_back_up.get())    
    
    return res
        
filaClientesTest = Cola()
filaClientesTest.put(("Franco", "comun")) 
filaClientesTest.put(("Micaela", "vip"))    
filaClientesTest.put(("Camila", "comun"))    
filaClientesTest.put(("Natalia", "comun"))
filaClientesTest.put(("Elsa", "vip"))    
    
resFilaClientesTest = Cola()
resFilaClientesTest = reordenar_cola_priorizando_vips(filaClientesTest)

# ------------------------------------------------------------------------

def palindromo(texto:str)->bool:
    for i in range(len(texto)//2):
        if (texto[i]!=texto[len(texto)-i-1]):
            return False
    return True

def cuantos_sufijos_son_palindromos(texto:str)->int:
    candidato:str = ''
    res:int = 0
    for i in range(len(texto)-1,-1,-1):
        candidato = texto[i] + candidato
        if (palindromo(candidato)):
            res += 1
    return res

# ------------------------------------------------------------------------

def quien_gano_el_tateti_facilito ( tablero : list[list[str]]) -> int:
    columnas : list[list[str]] = obtener_columnas(tablero)
    res: int = 0
    
    if hay_tres_iguales_a("X", columnas) and not hay_tres_iguales_a('O', columnas):
        res = 1
        
    if hay_tres_iguales_a("O", columnas) and not hay_tres_iguales_a("X", columnas):
        res = 2
        
    if not hay_tres_iguales_a ("O", columnas) and not hay_tres_iguales_a ("X", columnas):
        res = 0
        
    if hay_tres_iguales_a ("X", columnas) and hay_tres_iguales_a("O", columnas):
        res = 3
    
    return res

def obtener_columnas (tablero : list[list[str]]) -> list[list[str]]:
    
    res : list[list[str]] = []
    columna: list[str] = []
        
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            columna.append(tablero[j][i])
        res.append(columna)
        columna = [] 
        
    return res
            
def hay_tres_iguales_a (valor: str, columnas: list[list[str]]) -> bool:
    
    contador : int = 0
    res: bool = False
    
    for columna in columnas:
        for elem in columna:
            if contador == 3:
                res = True
            if elem == valor:
                contador += 1
            else:
                contador = 0
        if contador == 3:
            res = True
    return res
            
tableroTest = [
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "]
]
    
#print(quien_gano_el_tateti_facilito(tableroTest))
