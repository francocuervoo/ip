from typing import TypeVar
T = TypeVar('T')
import random

# Ejercicio 1

# 1)
def pertence ( s : list[int], e : int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False

def pertenece_v2 (s : list[int], e : int) -> bool:
    i : int = 0
    while i < len(s):
        if s[i] == e: 
            return True
        i += 1
    return False 

def pertenece_v3 (s : list[int], e : int) -> bool:
    for elem in s: # recorro todo los elementos, sirve si tengo que comparar, pero no me sirve para acceder al siguiente elemento
        if elem == e:
            return True
    return False


# 2)
def divide_a_todos (s : list[int], e : int) -> bool:
    for i in range(len(s)):
        if s[i] % e != 0:
            return False
    return True

# 3) 
def suma_total (s : list[int]) -> int:
    total : int = 0
    for i in range(len(s)):
        total += s[i]
    return total
    
# 4)
def maximo (s : list[int]) -> int:
    maximo : int = s[0]
    for i in range(len(s)):
        if s[i] > maximo:
            maximo = s[i]
    return maximo

# 5)
def minimo (s : list[int]) -> int:
    minimo : int = s[0]
    for i in range(len(s)):
        if s[i] < minimo:
            minimo = s[i]
    return minimo

# 6)
def ordenados(s: list[int]) -> bool:
    for i in range(len(s) - 1):  # Recorremos hasta el penúltimo elemento
        if s[i] >= s[i + 1]:  # Verificamos si hay algún elemento mayor o igual al siguiente
            return False  # Si lo encontramos, no está ordenado
    return True  # Si termina el bucle sin encontrar casos, está ordenado

# 7)
def post_maximo (s: list[int]) -> int:
    if len(s) == 0:
        return -1
    
    max : int = maximo(s)
    
    for i in range(len(s)):
        if s[i] == max:
            return i
    
# 8)
def pos_minimo (s: list[int]) -> int:
    if len(s) == 0:
        return -1
    
    min: int = minimo(s)
    
    for i in range(len(s)):
        if s[i] == min:
            return i

# 9)
def longitud_mayor_7 (list : list[list[str]]) -> bool:
    for elem in list:
        if len(elem) > 7:
            return True
    return False

listTest9 : list[list[str]] = ['gato', 'perro', 'raton', 'gato']
# print(longitud_mayor_7(listTest9))

# 10)
def es_palindromo (text : str) -> bool:
    text_invertido : str = ""
    for i in range(1, len(text) + 1):
        text_invertido += text[len(text) - i]
    return text == text_invertido

# 11) 
def hay_tres_numeros_consecutivos_iguales (list : list[int]) -> bool:  
    indice: int = 0
    indice_mayor: int = 1
    contador_iguales: int = 0

    while indice_mayor < len(list):
        if list[indice] == list[indice_mayor]:
            contador_iguales += 1
            if contador_iguales == 2:
                return True
            indice += 1
            indice_mayor += 1
        else:
            contador_iguales = 0
            indice += 1
            indice_mayor += 1
    return False
           
#print(hay_tres_numeros_consecutivos_iguales([3,3,3,4,5]))        

# 12)
def hay_tres_vocales_distintas (palabra : str) -> bool:
    vocales : list[str] = ['a', 'e', 'i', 'o', 'u']
    contador : int = 0
    
    for vocal in vocales:
        if pertenceString(vocal, palabra):
            contador += 1
    return contador > 2        
        
def pertenceString (caracter:str, palabra: str) -> bool:
    for pal in palabra:
        if pal == caracter:
            return True
    return False
        
#  13)
def posicion_ordenada_mas_larga(seq: list[int]) -> int:
    i: int = 0
    max_len: int = 1
    max_pos: int = 0
    current_len: int = 1
    current_pos: int = 0

    while i < len(seq) - 1:  # Cambiado a `len(seq) - 1` para evitar el índice fuera de rango
        if seq[i] <= seq[i + 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_pos = current_pos
            current_len = 1
            current_pos = i + 1  # Actualizamos `current_pos` para la siguiente subsecuencia
        i += 1

    # Verificar la última subsecuencia
    if current_len > max_len:
        max_pos = current_pos

    return max_pos

#print(posicion_ordenada_mas_larga([1, 2, 3, 2, 3, 4, 5]))  # Output: 4

# 14)
def cantidad_digitos_impares ( s : list[int]) -> int:
    impares_obtenidos : list[int] = []
    
    for element in s:
        numero: int = element
        while numero > 0:
            if(es_par(ultimo_digito(numero))):
                numero = eliminar_ultimo_digito(numero)
            else:
                impares_obtenidos.append(ultimo_digito(numero))
                numero = eliminar_ultimo_digito(numero)
    return len(impares_obtenidos)       



def es_par ( numero : int) -> bool :
    return numero % 2 == 0

def ultimo_digito (numero : int) -> int:
    return numero % 10

def eliminar_ultimo_digito (numero : int) -> int:
    return numero // 10

#print(cantidad_digitos_impares([22]))

# ------------------------------------------------------------------------------------------------------

# Ejercicio 2

# 1)
def CerosEnPosicionesPares (s : list[int]) -> None:
    for i in range(0, len(s)):
        if i % 2 == 0:
            s[i] = 0
            
# 2) 
def CerosEnPosicionesPares2 (s: list[int]) -> list[int]:
    res : list[int] = []
    for elem in s:
        if elem % 2 == 0:
            res.append(0)
        else:
            res.append(elem)    
    return res

# 3)
def eliminar_vocales (cadena : str) -> str:
    vocales : list[str] = ["a", "e", "i", "o", "u"]
    nueva_cadena : str = ""
    
    for caracter in cadena:
        if(not pertence_palabra_en_lista(caracter, vocales)):
            nueva_cadena += caracter
            
    return nueva_cadena
        
    
def pertence_palabra_en_lista (caracter : str, lista : list[str]):
    for element in lista:
        if element == caracter:
            return True
    return False

#print(eliminar_vocales("Monterubbianesi"))

# 4)
def reemplaza_vocales ( s : list[str] ) -> list[str]:
    nueva_lista : list[str] = []
    
    for palabra in s:
        nueva_palabra: str = ""
        for caracter in palabra:
            if(es_un_caracter_vocal(caracter)):
                nueva_palabra += "-"
            else:
                nueva_palabra += caracter
        nueva_lista.append(nueva_palabra)
        
    return nueva_lista
    

def es_un_caracter_vocal ( caracter : str) -> bool:
    vocales : list[str] = ["a", "e", "i", "o","u"]
    
    for vocal in vocales:
        if vocal == caracter:
            return True
    return False

#print(reemplaza_vocales(["Monterubbianesi", "Miele", "aeiou"]))

# 5)
def da_vuelta_str ( s : list[str]) -> list[str]:
    nuevo_s : list[str] = []
    
    for palabra in s:
        nuevo_s.append(dar_vuelta_palabra(palabra))
        
    return nuevo_s

def dar_vuelta_palabra ( palabra : str) -> str:
    nuevo_str : str = ""
    i: int = (len(palabra) - 1)
    for caracter in palabra:
        nuevo_str += palabra[i]
        i -= 1
    return nuevo_str    
        
#print(da_vuelta_str(["Monterubbianesi", "Miele", "Carlitos"]))

# 6)
def pertenece_str_en_lista(elemento: str, lista: list[str]) -> bool:
    for item in lista:
        if item == elemento:
            return True
    return False

def eliminar_repetidos(s: list[str]) -> list[str]:
    res = []
    for string in s:
        if not pertenece_str_en_lista(string, res): 
            res.append(string)
    return res


#print(eliminar_repetidos(["Hola", "sala", "sala", "hola", "hla"]))

# ------------------------------------------------------------------------------------------------------

# Ejercicio 3

def resultadoMateria ( notas : list[int]) -> int:
    res : int = 0
    
    if(son_todas_notas_aprobadas(notas) and promedio_notas(notas) >= 7):
        res = 1
        
    if(son_todas_notas_aprobadas(notas) and promedio_notas(notas) >= 4 and promedio_notas(notas) < 7):
        res = 2
        
    if(not son_todas_notas_aprobadas(notas) or promedio_notas(notas) < 4):
        res = 3
    return res
    
def promedio_notas ( notas : list[int]) -> float:
    total : int = 0
    cantidad : int = len(notas)
    
    for nota in notas:
        total += nota
        
    return total / cantidad

def son_todas_notas_aprobadas ( notas : list[int]) -> bool:
    res: bool = True
    
    for nota in notas:
        if (nota < 4) :
            res = False
        
    return res
    
#print(resultadoMateria([10,4, 1]))

# ------------------------------------------------------------------------------------------------------

# Ejercicio 4

def obtener_saldo_total(lista: list[tuple[str, int]]) -> int:
    saldo : int = 0

    for movimiento , dinero in lista:
        if( movimiento == "I"):
            saldo += dinero
        if (movimiento == "R"):
            saldo -= dinero
            
    return saldo
    
#print(obtener_saldo_total([("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]))    

# ------------------------------------------------------------------------------------------------------

# Ejercicio 5

# 1)
res41 : list[bool] = []
listRes41 : list[list[int]] = [[1,2,3], [4,5,6], [7,8,9]]
def pertenece_a_cada_uno_version_1 ( s: list[list[int]], e: int, res: list[bool]) -> None : 
    res.clear()
    for elem in s:
        if(pertence(elem, e)):
            res.append(True)
        else:
            res.append(False)

# pertenece_a_cada_uno_version_1 (listRes41, 4, res41)
# print(res41)

# 2)
# es igual al 1) solo que res tiene que tener la misma longitud que s

# 3)
def pertenece_a_cada_uno_version_3 ( s: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []
    for elem in s:
        if(pertence(elem, e)):
            res.append(True)
        else:
            res.append(False)
    return res
#print(pertenece_a_cada_uno_version_3([[1,2,3], [4,5,6], [7,8,3]], 3))
            
# ------------------------------------------------------------------------------------------------------

# Ejercicio 6

# 1)
def es_matriz (s: list[list[int]]) -> bool:
    res: bool = True
    if(len(s)) == 0 or s[0] == 0:
        res = False
        return res
    
    anchoMatriz : int = len(s[0])
    
    for elem in s:
        if(not len(elem) == anchoMatriz):
            res = False
    return res
    
#print(es_matriz(matriz))    

# 2)
def filas_ordenadas(s: list[list[int]], res:list[bool]) -> None:
    res.clear()
    for elem in s:        
        if(ordenados(elem)):
            res.append(True)
        else:
            res.append(False)
    return res
            
# 3)
def columna (s: list[list[int]], c: int) -> list[int]:
    res : list[int] = []
    
    for elem in s:
        res.append(elem[c])
        
    return res

#print(columna(matriz, 0))

# 4)
def columnas_ordenadas (m: list[list[int]]) -> list[bool] :
    columnas : list[int] = []
    i : int = 0
    res : list[bool] = []
    
    while i < len(m):
        columnas.append(columna(m,i))
        i += 1
            
    for col in columnas:
        if(ordenados(col)):
            res.append(True)
        else:
            res.append(False)
    return res

matriz: list[list[int]] = [[1,2,3], [4,5,6], [7,8,9]]

#print(columnas_ordenadas(matriz))                    

# 5)
def transponer (m : list[list[int]]) -> list[list[int]] :
    columnas : list[int] = []
    i : int = 0
    
    while i < len(m):
        columnas.append(columna(m,i))
        i += 1
           
    return columnas

#print(transponer(matriz))
        
# 6)
def quien_gana_tateti (m: list[list[str]]) -> int :
    columnas : list[list[str]] = []
    res: int = 0
    
    i : int = 0
    while i < len(m):
        columnas.append(columna(m,i))
        i +=1
            
    # Caso O
    for fila in m : 
        if elementos_iguales(fila):
            if(fila[0] == "O"):
                res = 0
                print("Hay una fila horizontal de O")
                return res
    
    for col in columnas:
        if elementos_iguales(col):
            if(col[0] == "O"):
                res = 0
                print("Hay una columna de O")
                return res
            
    if m[0][0] == "O":
        if m[1][1] == "O":
            if m[2][2] == "O":
                res = 0
                print("Hay una diagonal de O")
                return res
            
    if m[0][2] == "O":
        if m[1][1] == "O":
            if m[2][0] == "O":
                res = 0
                print("Hay una diagonal de O")
                return res            
               
    # Caso 1
    for fila in m : 
        if elementos_iguales(fila):
            if(fila[0] == "1"):
                res = 1
                print("Hay una fila horizontal de 1")
                return res
    
    for col in columnas:
        if elementos_iguales(col):
            if(col[0] == "1"):
                res = 1
                print("Hay una columna de 1")
                return res
            
    if m[0][0] == "1":
        if m[1][1] == "1":
            if m[2][2] == "1":
                res = 1
                print("Hay una diagonal de 1")
                return res
            
    if m[0][2] == "1":
        if m[1][1] == "1":
            if m[2][0] == "1":
                res = 1
                print("Hay una diagonal de 1")
                return res            
                   
    res = 2
    print("No hay tateti")
    return res                            
            
def elementos_iguales (s: list[T]) -> bool :            
    e : T = s[0]
    for elem in s:
        if not elem == e:
            return False
    return True

#print(quien_gana_tateti([["O", "X", "O"], ["X", "X", "0"], ["O", "X", "X"]]))

            
# ------------------------------------------------------------------------------------------------------

# Ejercicio 7
def generar_matriz_tamaño_d (d: int) -> list[list[int]]:
    
    i : int = 0
    matriz: list[list[int]] = []
    
    while i < d:
        matriz.append(generar_fila_tamaño_d(d))
        i += 1
    
    return matriz    

def generar_fila_tamaño_d (d: int) -> list[int]:
    i :int = 0
    fila : list[int] = []
    while i < d:
        numero_random = random.randint(1,10)
        fila.append(numero_random)
        i += 1
    return fila    

def multiplicar_matrices(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    d = len(m1)
    resultado = []
    i = 0
    while i < d:
        fila_resultado = []
        j = 0
        while j < d:
            suma = 0
            k = 0
            while k < d:
                suma += m1[i][k] * m2[k][j]
                k += 1
            fila_resultado.append(suma)
            j += 1
        resultado.append(fila_resultado)
        i += 1
    return resultado
    
def elevar_matriz_a_potencia(d: int, p: int) -> list[list[int]]:
    matriz = generar_matriz_tamaño_d(d)
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    resultado = matriz
    contador = p - 1  # Número de multiplicaciones restantes
    while contador > 0:
        resultado = multiplicar_matrices(resultado, matriz)
        contador -= 1
    return resultado
            
            
#print(elevar_matriz_a_potencia(5,5))    


# ------------------------------------------------------------------------------------------------------

# Ejercicio 4 Programas interactivos usando secuencias

# 1)
def agregar_alumnos() -> list[str]:
    lista_alumnos : list[str] = []
    nombre_alumno = input("Ingrese nombre del alumno: ") 

    while nombre_alumno != "" and nombre_alumno != "listo":
        lista_alumnos.append(nombre_alumno)    
        nombre_alumno = input("Ingrese nuevo nombre de alumno o 'listo' para terminar: ")
    return lista_alumnos
        
#print("Lista de alumnos", agregar_alumnos())

# 2)
def historial_monedero() -> list[tuple[str, int]]:
    total : int = 0
    historial : list[tuple[str, int]] = []
    operacion = input("Selecciona una operación: C -> Cargar créditos, D -> Descontar créditos, X -> Terminar ")
       
    while operacion != "X":      
        while operacion == "C":
            credito = int(input("Ingrese un crédito a cargar "))
            historial.append((operacion, credito))
            total += credito
            operacion = input("Selecciona una nueva operación: C -> Cargar créditos, D -> Descontar créditos, X -> Terminar ")
            
        while operacion == "D":
            credito = int(input("Ingrese un crédito a descontar "))
            historial.append((operacion, ( -credito)))
            total -= credito
            operacion = input("Selecciona una nueva operación: C -> Cargar créditos, D -> Descontar créditos, X -> Terminar ")
    
    return historial         
                
#print("El historial es :", historial_monedero())    
    
    
# 3)
def jugar_siete_y_medio() -> list[int] :
    total : float = 0.0
    historial : list[int] = []
    numero_random = obtener_numero_random_juego()
    historial.append(numero_random)
    total += devolver_puntos_juego(numero_random)
    
    print("Juego empezado")
    operacion = input("Ingrese 1 para sacar otra carta, o 2 para plantarse: ")  
    
    while operacion == "1" and total <= 7.5:
        numero_random = obtener_numero_random_juego()
        historial.append(numero_random)
        total += devolver_puntos_juego(numero_random)
        
        if total > 7.5:
            print("Has periddo ")
            return historial
        
        operacion = input("Ingrese 1 para sacar otra carta, o 2 para plantarse: ")
            
    if operacion == "2":
        print("Te has plantado ")
        
        return historial        
            
def obtener_numero_random_juego() -> int:
    numero_random = random.randint(1,12)
    
    while numero_random == 8 or numero_random == 9:
        numero_random = random.randint(1,12)
        
    return numero_random
    

def devolver_puntos_juego(numero : int) -> float:
    res : int = 0
    if numero == 10 or numero == 11 or numero == 12:
        res = 0.5
    else:
        res = numero
    return res

#print(jugar_siete_y_medio())

# 4)
def analizar_password () -> str:
    password_ingresada = input("Ingrese una contraseña a analizar ")
    
    if es_longitud_menor_5(password_ingresada):
        return "ROJA"
    
    if es_longitud_mayor_ocho(password_ingresada) and tiene_mayuscula(password_ingresada) and tiene_minuscula(password_ingresada) and tiene_digito_numero(password_ingresada):
        return "VERDE"
    
    return "AMARILLA"

def es_longitud_mayor_ocho (password: str) -> bool:
    if len(password) > 8:
        return True
    return False

def es_longitud_menor_5 (password: str) -> bool:
    if len(password) < 5:
        return True
    return False

def tiene_digito_numero (password : str) -> bool:
    numeros : list[str] = ["0","1","2","3","4","5","6","7","8","9"]
    
    for char in password:
        if(esta_inlcuido(char, numeros)):
            return True
    return False

def esta_inlcuido (e: T, s: list[T]) -> bool :            
    for elem in s:
        if elem == e:
            return True
    return False

def tiene_mayuscula (password : str) -> bool:
    mayusculas : list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]

    for char in password:
        if(esta_inlcuido(char, mayusculas)):
            return True
    return False

def tiene_minuscula (password : str) -> bool:
    minusculas : list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for char in password:
        if(esta_inlcuido(char, minusculas)):
            return True
    return False


print("Análisis de contrasea ", analizar_password())
