#clase 28/X/2024    colas, pilas y diccionarios
 
# -*- coding: latin-1 -*-
from typing import TypeVar #, Tuple
from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
 
 
T = TypeVar('T')
 
#modifica la lista o cola recibida
def imprimir(lista_o_cola):
    while not (lista_o_cola.empty()):
        print(lista_o_cola.get())
 
def copiar_cola (original:Cola )-> Cola:
    res: Cola = Cola()
    cola_tmp: Cola = Cola()
 
    while not (original.empty()):
        v = original.get()
        res.put(v) 
        cola_tmp.put(v) #guardo en una cola temporal para luego restaurar
 
    #restauro la cola original
    while not (cola_tmp.empty()):
        v = cola_tmp.get()
        original.put(v)
 
    return res
 
mi_cola = Cola()
 
# Agregamos elementos a la cola
mi_cola.put(11)
mi_cola.put(22)
mi_cola.put(3)
copia = copiar_cola(mi_cola)
print(copia.queue)
print(mi_cola.queue)
 
 
#ejemplo uso de pila
pila:Pila = Pila()
 
print(pila.empty())
 
#agrego elementos
pila.put(1)
pila.put(2)
pila.put(3)
 
print(pila.empty())
print("Size", pila.qsize())
 
#saco e imprimo los elementos de la pila
print(pila.get())
print(pila.get())
print(pila.get())
 
print("Size", pila.qsize())
print(pila.empty())
 
 
 
#ejemplos con diccionario
 
#creo un dicc con algunos pares de clave-valor
mi_dicc: dict[str, str] = {
    'auto': 'car',
    'sol': 'sun',
    'luna': 'moon'
}
 
#agrego clave-valor
mi_dicc['una_clave'] = 'un_valor'
 
#reemplazo el valor de una clave
mi_dicc['una_clave'] = "nuevo valor"
 
 
#recupero un valor
v:str = mi_dicc['una_clave']
 
 
#recupero un valor y lo elimino del dicc
v:str = mi_dicc.pop('una_clave')
 
 
#Ejemplos de uso de diccionario
 
#recorro un dicc, lo imprimo y lo copio a otro diccionario
nuevo_dic: dict[str, str] = {} #creo un dicc vacio
 
# recupero las claves y, con cada clave, recupero su valor, lo imprimo y lo agrego a otro diccionario
claves:list[str] = mi_dicc.keys() 
for clave in claves:    
    valor:str = mi_dicc[clave]
    print(f'{clave} - {valor}') 
    nuevo_dic[clave] = valor #lo agrego al nuevo diccionario
 
 
#vacío el dicc
nuevo_dic.clear()
 
 
#otra forma de recorrer un dicc
otro_dic: dict[str, str] = {} #creo un dicc vacio
for clave, valor in mi_dicc.items():    
    print(f'{clave} - {valor}') 
 
# recupero solo los valores y los imprimo
valores:list[str] = otro_dic.values() 
for v in valores:    
    print(v)  
 
 
#creo un dicc donde la clave representa un día y el valor es una tupla con la temp mín y max
temp_por_dia: dict[int, (float, float)] = {
    1: (10.5, 20),
    2: (10.3, 20.6),
    3: (1.5, 20)
}
 
def dia_de_menor_minima (temps :dict[int, (float, float)] ) -> int:
    #asumo que hay por lo menos un día con su temp.
    res: int = list(temps.keys()) [0]  
    temp_min = temps [res] [0] 
    for c, v in temps.items():    
        min_dia:float = v[0]  
        if temp_min > min_dia:
            temp_min = min_dia
            res = c
 
    return res
 
dia = dia_de_menor_minima (temp_por_dia)
print(dia)
 
 
 
#8 implementar una funcion `generarNrosAlAzar(in n: int, in desde: int, in hasta: int) -> list[int]` 
# que genere una lista de n numeros enteros al azar en el rango [desde, hasta]. 
# Pueden user la funcion `random.randint()`
 
def generar_nros_al_azar(n: int, desde: int, hasta: int) -> Pila[int]:
    res:Pila[int] = Pila()
    for _ in range(n):
        x = random.randint(desde, hasta)
        res.put(x)
    return res
 
#print (generarNrosAlAzar(5,7,1000))
 
 
def buscar_el_maximo(p: Pila[int]) -> int:
    maximo = p.get() #precondición: la pila no está vacía
    
    pila_tmp: Pila = Pila()
    pila_tmp.put(maximo) #guarda para restaurar
 
    while not p.empty():
        elemento = p.get()
        pila_tmp.put(elemento) 
 
        if elemento > maximo:
            maximo = elemento
 
    #restauro
    while not pila_tmp.empty():
        elem = pila_tmp.get()
        p.put(elem)
 
    return maximo
 
pila = Pila()
pila.put(5)
pila.put(10)
pila.put(3)
pila.put(8)
 
 
def armar_secuencia_de_bingo() -> Cola[int]:
    numeros: list[int] = []
    cola: Cola[int] = Cola()
 
    while len (numeros) < 100:
        n = random.randint(0,99)
        if not pertenece(numeros, n): 
            cola.put(n)
            numeros.append(n)
 
    return cola
 
def armar_secuencia_de_bingo_mas_rapido() -> Cola[int]:
    numeros: list[int] = list (range (0,100)) #creo una lista con todos los números
    res: Cola[int] = Cola()
 
    for hasta in range (99, -1, -1):
        i = random.randint(0,hasta)
        v = numeros[i] 
        res.put (v)
        numeros.pop (i) #lo elimino de la lista
 
    return res
 
print(armar_secuencia_de_bingo_mas_rapido().queue)
 
 
 
def armar_secuencia_de_bingo_con_shuffle() -> Cola[int]:
    numeros: list[int] = list(range(100))
    random.shuffle(numeros) # confirmar si se puede usar en el parcial
    cola: Cola[int] = Cola()
 
    for num in numeros:
        cola.put(num)
 
    return cola
 
def jugar_carton_de_bingo(carton:list,bolillero:Cola[int])->int:
 
    jugadas:int=0
    numeros_marcados:int=0
    bolillero_aux:Cola[int]=Cola()
 
    #Sigo sacando bolillas hasta que marque todos los numeros
    while numeros_marcados < 12:
        bolilla_sacada=bolillero.get()
        bolillero_aux.put(bolilla_sacada)
        if pertenece (carton, bolilla_sacada):
            numeros_marcados+=1
        jugadas+=1
 
    #Una vez que marque todos, paso todas las bolillas restantes al bolillero auxiliar
    while not bolillero.empty():
        bolilla_sacada:int = bolillero.get()
        bolillero_aux.put(bolilla_sacada)
 
    #Luego las devuelvo del bolillero auxiliar al original, para que quede igual que al principio        
    while not bolillero_aux.empty():
        bolilla_sacada:int  = bolillero_aux.get()
        bolillero.put(bolilla_sacada)
 
    return jugadas
 
def pertenece (cadena: list[T], elem:T) -> bool:
    for i in cadena:
        if i == elem: 
            return True
    return False
 
 
 
"""
Ejercicio 17. Dada una secuencia de tuplas, donde cada tupla tiene en la primera componente el nombre de un estudiante
y en la segunda componente la nota que sacó en un examen, se pide devolver un diccionario con los promedios de todos los
estudiantes. La clave del diccionario debe ser el nombre del estudiante y el valor el promedio de todos sus exámenes.
calcular promedio por estudiante(notas : list[tuple[str, float]]) → dict[str, float]
"""
# Ejercicio 17
def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, float]:
    
    # Inicializamos un diccionario vacío para guardar la respuesta
    res: dict[str, float] = {}
    
    # Recorremos las notas
    for nota in notas:
        # El estudiante es el primer elemento de la tupla
        estudiante:str = nota[0]
 
        # Si todavía no calcule su promedio, lo hago. Si ya lo calculé, lo ignoro
        # Noten que aca nos estamos fijando si estudiante es una CLAVE del diccionario res
        if not pertenece (list(res.keys()), estudiante):
            # Calculamos el promedio con la función auxiliar
            prom:float = calcular_promedio_de_un_estudiante(estudiante,notas)
 
            # Guardo el promedio como el valor asociado a la clave estudiante
            res[estudiante] = prom
        
    # Devolvemos el diccionario
    return res
 
def calcular_promedio_de_un_estudiante(estudiante:str, notas:list[tuple[str,float]]) -> float:
    # Inicializamos variables para llevar el recuento de la suma y la cantidad de notas
    suma_notas:float = 0.0
    cant_notas:int = 0
 
    for nota in notas:
        estudiante_actual:str = nota[0]
        # Sumamos la nota actual solo si esta asociada al estudiante que nos estamos fijando
        if estudiante_actual == estudiante:
            suma_notas += nota[1]
            cant_notas += 1
    
    return suma_notas / cant_notas