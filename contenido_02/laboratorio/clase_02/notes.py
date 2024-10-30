# listas en python
# -*- coding: latin-1 -*-
 
from typing import TypeVar, Tuple
 
T = TypeVar('T')
 
 
#ejemplos sobre manejo de listas y matrices
 
 
def prueba():
 
    s:list[int] = [5,6,7]
    print(len(s))
    s.append(5)
    print(len(s))
    
    print(s)
    s[0] = 10
    #se puede indexar en una lista con los índices desde 0 hasta el tamaño de la lista menos 1
    # si hacemos: s[len(s)] = ... FALLA
 
    print(s)
    v:int = s.pop(0) #devuelve y elimina de la lista el elemento que esté en la posicion del parámetro
    print(v)
    print(s)
 
    s.clear()
    print(len(s))
 
 
    s:list[str] = ['a', 'b', 'c', 'd', 'e']
 
    
    #copio parte de una lista
    nueva_lista = s[2:] #NO USAR en ejercicios y parcial  = ['c', 'd', 'e']
    otra_lista = s[:2]  #NO USAR en ejercicios y parcial = ['a', 'b']
 
    print(nueva_lista) 
    print(otra_lista) 
 
    for x in s:
        print(x)
    
    print("")
 
    #imprimo índices desde 0
    for i in range(len(s)):
        print(i)
    
    print("")
 
    #imprimo índices desde el 2
    for i in range( 2, len(s)):
        print(i)
    
    print("")
 
    #imprimo índices pares desde 0
    for i in range( 0, len(s), 2):
        print(i)
    
    print("")
 
    #imprimo los valores
    for v in s:
        print(v)
    
    print("")
 
 
    #recorro la lista de manera inversa. Ojo con los índices.
    for i in range(len(s)-1, -1, -1):
        print(s[i])
 
    #recorro la lista de manera inversa, igual a lo anterior. Ojo con los índices.
    for i in range(len(s), 0, -1):
        print(s[i-1])
 
    print("")
 
prueba()
 
 
#Calcula y devuelve la suma de todos los elementos de una lista
def suma_lista(lista:list[int]) -> int :
    suma:int = 0
    for numero in lista:
        suma += numero
    return suma
 
#Calcula y devuelve la suma de todos los elementos de una matriz tomando los valores 
def sumar_matriz (s:list[list[int]]) -> int:
    res:int = 0
    for f in s:
        for v in f:
            res += v
    return res
 
# print ("sumar_matriz:")
# print (sumar_matriz([[1,2,1],[2,3,4], [3,4,0]]))
# print("")
 
 
# suma todos los elementos de una matriz recorriéndola por los índices 
def sumar_matriz_ind (s:list[list[int]]) -> int:
    res:int = 0
    for f in range (len (s)):
        for c in range (len (s[f])):
            res += s[f][c]
    return res
 
print ("sumar_matriz_ind :")
print (sumar_matriz_ind([[1,2,1],[2,3,4], [3,4, 0]]))
print("")
 
# ver dónde se inicializa res y cont_fila
# devuelve una lista con los valores de la suma de cada fila 
def sumar_filas_matriz_ind(s:list[list[int]]) -> list[int]:
    res:list[int] = []
    for f in s:
        cont_fila = 0
        for v in f:
            cont_fila += v
        res.append(cont_fila)
 
    return res    
 
 
print ("sumar_filas_matriz_ind :" )
print ( sumar_filas_matriz_ind([[1,2,1],[2,3,4], [3,4, 0]]))
print("")
 
# devuelve una lista con los valores de la suma de cada columna 
def sumar_columnas_matriz (s:list[list[int]]) -> list[int]:
    res:list[int] = []
    for c in range (len (s[0])): #asumo que hay, por lo menos, una fila
        suma_col:int = 0
        for f in range (len (s)):
            suma_col += s[f][c]
        res.append (suma_col)
    return res
 
 
print ("sumar_columnas_matriz :" )
print ( sumar_columnas_matriz([[1,2,1],[2,3,4], [3,4, 0]]))
print("")
 
# #dada una matriz devuelve una columna
def columna (matriz:list[list[int]], nro_col:int) -> list[int]:
    res:list[int] = []
    for fila in matriz:
        res.append(fila[nro_col])
    return res
 
# devuelve una lista de tuplas con los valores mín y máx de cada columna 
def min_max_columnas_matriz (s:list[list[int]]) -> list[(int, int)]:
    res:list[(int, int)] = []
    for nro_col in range (len (s[0])): #asumo que hay, por lo menos, una fila
        col:list[int]  = columna(s, nro_col)
        res.append (min_max (col))
 
    return res
 
 
# #devuelve una tupla con el valor mínimo y el máximo
def min_max (s:list[int]) -> Tuple [int, int] : # (int, int):
    # requiere |s| > 0 
    minimo = s[0]
    maximo = s[0]
    
    for numero in s:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero
    
    return minimo, maximo
 
 
print ("min_max_columnas_matriz :" )
print ( min_max_columnas_matriz([[1,2,1],[2,3,4], [3,4, 0]]))
print("")
 
 
 
 
 
 
#1.1 Dada una lista de número y un número, devolver verdadero si el número pertenece a la lista 
# (sin utilizar la función nativa in ). żSe puede usar esta misma función para buscar un caracter dentro de un string?
#def pertenece (cadena: list[int], elem:int) -> bool:
 
 
def pertenece (cadena: list[int], elem:int) -> bool:
    for e in cadena:
        if e == elem: 
            return True
    return False
 
pertenece = pertenece([2,4,5,6], 5)
print (f"Pertenece: {pertenece}" )
 
#Implementación modificada de "pertenece", ahora soporta tipos genéricos.
#Al usar tipos genéricos, podemos usar esta función para int, char, bool, etc.
def pertenece_usando_tipo_generico (cadena: list[T], elem:T) -> bool:
    for i in cadena:
        if i == elem: 
            return True
    return False
 
z = pertenece_usando_tipo_generico(['a', 'b', 'c'], 'a')
print (z)
 
 
def pertenece_2(s:list[int], e:int) -> bool:
    longitud:int = len(s)
    indice_actual:int = 0
    pertenece:bool = False
 
    while (indice_actual < longitud):
        if (s[indice_actual] == e):
          pertenece = True
        indice_actual = indice_actual + 1
 
    return pertenece
 
 
def pertenece_3(s:list[int], e:int) -> bool:
    longitud:int = len(s)
    indice_actual:int = 0
    pertenece:bool = False
    while ((indice_actual < longitud) and (not pertenece)):
        if (s[indice_actual] == e):
            pertenece = True
        indice_actual = indice_actual + 1
    return pertenece
 
def pertenece_4(s:list[int], e:int) -> bool:
    # para saber si un elemento pertenece a una lista, "in" es el método más común, 
    # pero este ejercicio busca que implementen una solución "a mano"
    return e in s
 
 
# #2.2
def cero_en_posiciones_pares_2(lista: list[int])  -> list[int]: 
    res: list[int] = []
 
    for i in range(len(lista)):
        if i % 2 == 0:
            res[i] = 0
        else:
            res[i] = lista[i]
    return res
 
 
def cero_en_posiciones_pares_2_v2(lista: list[int])  -> list[int]: 
    
    # #Si inicilizamos de esta manera, entonces no es necesaria la copia que hacíamos en el else
    res: list[int] = lista.copy() 
 
    res: list[int] = []
 
    for i in range(len(lista)):
        if i % 2 == 0:
            res[i] = 0
 
    return res
 