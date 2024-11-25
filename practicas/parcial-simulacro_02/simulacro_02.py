from queue import Queue as Cola
from queue import LifoQueue as Pila


# Ejercicio 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:

    lista_estudiantes_con_notas_materias : list[tuple[str, str, int]] = notas_estudiante_materia

    lista_estudiantes : list[str] = []
    dict_gestion_notas : dict[str, list[tuple[str,int]]] = {}

    # Obtengo la lista de estudiantes
    for elem in lista_estudiantes_con_notas_materias:
        nombre: str = elem[0]
        if not pertenece_str(nombre, lista_estudiantes):   
            lista_estudiantes.append(nombre)

    # Agrego las keys al objeto
    for estudiante in lista_estudiantes:
        dict_gestion_notas[estudiante] = []

    # Agrego la materia y la nota al objeto
    for alumno , value in dict_gestion_notas.items():
        for estudiante_con_nota_materia in lista_estudiantes_con_notas_materias:
            materia : str = estudiante_con_nota_materia[1]
            nota_materia : int = estudiante_con_nota_materia[2]
            if (alumno == estudiante_con_nota_materia[0]):
                dict_gestion_notas[alumno].append((materia, nota_materia))

    return dict_gestion_notas

def pertenece_str(elemento : str, conjunto : list[str]) -> bool:
    for elem in conjunto:
        if elemento == elem:
            return True
    return False


# Ejercicio 2
def cantidad_digitos_pares(numeros: list[int]) -> int:
    contador : int = 0

    for numero in numeros:
        numero_parcial : int = numero
        ultimo_digito : int = 0

        while not numero_parcial < 10:
            ultimo_digito = obtener_ultimo_digito(numero_parcial)

            if es_par(ultimo_digito):
                contador += 1
            numero_parcial = eliminar_ultimo_digito(numero_parcial)

        if es_par(numero_parcial):
            contador += 1    

    return contador

def es_par (numero : int) -> bool:
    return numero % 2 == 0

def obtener_ultimo_digito (numero : int) -> int:
    return numero % 10

def eliminar_ultimo_digito ( numero : int) -> int:
    return numero // 10


# Ejercicio 3
def reordenar_cola_primero_pesados(paquetes: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    cola_umbraleada  = Cola()

    cola_livianos = Cola()
    cola_pesados = Cola()

    while not paquetes.empty():
        paquete_get : tuple[str,int] = paquetes.get()

        if paquete_get[1] <= umbral:
            cola_livianos.put(paquete_get)

        else:
            cola_pesados.put(paquete_get)

    while not cola_pesados.empty():
        paquete_pesado_get : tuple[str,int] = cola_pesados.get()
        cola_umbraleada.put(paquete_pesado_get)
    
    while not cola_livianos.empty():
        paquete_liviano_get : tuple[str,int] = cola_livianos.get()
        cola_umbraleada.put(paquete_liviano_get)

    print(cola_umbraleada.queue)

    return cola_umbraleada

#cola_test = Cola()
#cola_test.put(("1", 30))
#cola_test.put(("2", 130))
#cola_test.put(("3", 330))
#cola_test.put(("4", 430))
#cola_test.put(("5", 230))

#print(reordenar_cola_primero_pesados(cola_test, 300))

# Ejercicio 4
def matriz_pseudo_ordenada(matriz: list[list[int]]) -> bool:
    columnas : list[list[int]] = obtener_columnas_matriz(matriz)
    minimo_parcial : int = 0

    for columna in columnas:
        if minimo_parcial >= obtener_minimo_fila(columna):
            return False
        minimo_parcial = obtener_minimo_fila(columna)

    return True

def obtener_columnas_matriz(matriz: list[list[int]]) -> list[list[int]]:

    matriz_columnas : list[list[int]] = []
    columna_parcial : list[int] = []
    largo_matriz : int = len(matriz)
    
    for i in range(largo_matriz):
        for j in range(largo_matriz):
            columna_parcial.append(matriz[j][i])        
        
        matriz_columnas.append(columna_parcial)
        columna_parcial = []

    return matriz_columnas

def obtener_minimo_fila (fila: list[int]) -> int:
    minimo_numero_fila : int = fila[0]

    for numero in fila:
        if numero < minimo_numero_fila:
            minimo_numero_fila = numero

    return minimo_numero_fila


