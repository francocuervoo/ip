from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1
def multiplos_de_primos(v: list[int]) -> dict[int,int]:
    lista_parcial : list[list[int]] = []
    res : dict[int,int] = dict()

    for u in v:
        lista_parcial.append(obtener_primos_que_dividen(u))

    lista_unificada : list[int] = unificar_lista(lista_parcial)

    for numero in lista_unificada:
        res[numero] = 0

    for dictKey , dictValue in res.items():
        res[dictKey] = cantidad_de_veces_que_dividie(dictKey, v)

    return res

def es_primo ( numero : int) -> bool:
    if numero < 2:
        return False
    
    contador : int = 2

    while not contador == numero:
        if numero % contador == 0:
            return False
        else:
            contador += 1
        
    return True
  
def obtener_primos_que_dividen ( numero : int) -> list[int]:
    lista_primos : list[int] = []

    numero_primo : int = 2

    while not numero_primo > numero:
        if es_primo(numero_primo) and numero % numero_primo == 0:
            lista_primos.append(numero_primo)
        numero_primo += 1

    return lista_primos
    
def unificar_lista ( lista_numeros : list[list[int]]) -> list[int]:
    nueva_lista : list[int] = []

    for lista in lista_numeros:
        for numero in lista:
            if not esta_incluido(numero, nueva_lista):
                nueva_lista.append(numero)

    return nueva_lista

def esta_incluido ( elemento : int, conjunto : list[int]) -> bool:
    for elem in conjunto:
        if elem == elemento:
            return True
    return False

def cantidad_de_veces_que_dividie ( primo : int, lista_numeros: list[int]) -> int:
    cantidad : int = 0

    for numero in lista_numeros:
        if numero % primo == 0:
            cantidad += 1

    return cantidad

v_test : list[int] = [40,30,15,49, 11, 121, 200, 53]
print(multiplos_de_primos(v_test))

#---------------------------------------------------------------------------------------------------------

# Ejercicio 2
def longitud_mas_grande(A: list[list[int]]) -> int:
    lista_nueva : list[int] = []
    mayor : int = 0

    for a in A:
        longitud = longitud_mas_larga_de_una_lista(a)
        lista_nueva.append(longitud)

    mayor = obtener_numero_mayor(lista_nueva)

    return mayor

def longitud_mas_larga_de_una_lista ( lista_numeros : list[int]) -> int:
    res: int = 0
    inicio_actual : int = 0
    inicio_temporal: int = 0

    if not (esta_incluido(1, lista_numeros)):
        return res
    
    for numero in lista_numeros:
        if numero == 1 and inicio_actual == 0:
            inicio_actual += 1
        elif numero == 1 and inicio_actual != 0:
            inicio_actual += 1
        elif numero != 1:
            if inicio_actual > inicio_temporal:
                inicio_temporal = inicio_actual
            inicio_actual = 0
        elif inicio_actual > inicio_temporal:
            inicio_temporal = inicio_actual

    if(inicio_actual > inicio_temporal):
        inicio_temporal = inicio_actual

    res = inicio_temporal

    return res

def obtener_numero_mayor ( lista_numeros : list[int] ) -> int:
    mayor_parcial = lista_numeros[0]

    for numero in lista_numeros:
        if numero > mayor_parcial:
            mayor_parcial = numero

    return mayor_parcial

longitud_test : list[list[int]] = [[1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [2], [2,11], [1541]]
print(longitud_mas_grande(longitud_test))

#---------------------------------------------------------------------------------------------------------

# Ejercicio 3
def resolver_cuentas(A: Pila[str]) -> list[int]:
    pila_back_up : Pila[str] = Pila()
    res : list[int] = []

    while not A.empty():
        cuenta: str = A.get()
        pila_back_up.put(cuenta)

        res.append(resolver_operacion_aritmetica(cuenta))

    while not pila_back_up.empty():
        A.put(pila_back_up.get())

    return res

def esta_bien_formado ( s : str) -> bool:
    largo_caracter : int = len(s)

    for i in range(largo_caracter):
        if not es_mas_menos_o_digitos(s[i]):
            return False
        
        if not es_un_digito(s[largo_caracter -1]):
            return False
        
    if hay_dos_operadores_juntos(s):
        return False

    return True

def es_mas_menos_o_digitos ( caracter : str ) -> bool:
    digitos : list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]

    for digito in digitos:
        if digito == caracter:
            return True
    return False

def es_un_digito ( caracter : str) -> bool:
    digitos : list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for digito in digitos:
        if caracter == digito:
            return True
    return False

def hay_dos_operadores_juntos ( s : str) -> bool:
    contador : int = 0

    for r in s:
        if contador > 1:
            return True

        if r == "+" or r == "-":
            contador +=1
 
        else:
            contador = 0

    if contador > 1:
        return True
    
    return False

def resolver_operacion_aritmetica ( s : str) -> int:

    nueva_lista : list[str] = s_a_lista(s)

    suma_total : int = 0
    valor_lista_sumas: int = 0
    valor_lista_restas: int = 0

    lista_sumas: list[int] = []
    lista_restas: list[int] = []

    esSuma : bool = False
    esResta: bool = False

    for i in range(len(nueva_lista)):
        if i == 0 and int(nueva_lista[0]) >= 0:
            lista_sumas.append(int(nueva_lista[0]))
        elif i == 0 and int(nueva_lista[0]) < 0:
            lista_restas.append(int(nueva_lista[0])* -1)          
        elif i != 0 and nueva_lista[i] == "+":
            esSuma = True
            esResta = False
        elif i != 0 and nueva_lista[i] == "-":
            esSuma = False
            esResta = True            
        elif esSuma:
            lista_sumas.append(int(nueva_lista[i]))
            esSuma = False
            esResta = False 
        elif esResta:
            lista_restas.append(int(nueva_lista[i]))
            esSuma = False
            esResta = False             

    for elem in lista_sumas:
        valor_lista_sumas += elem            

    for elem in lista_restas:
        valor_lista_restas += elem

    suma_total = valor_lista_sumas - valor_lista_restas

    return suma_total

def s_a_lista (s : str) -> list[str]:
    res : str[int] = []
    numero_parcial : str = ""

    for i in range(len(s)):
        if i == 0 and es_un_digito(s[i]):
            numero_parcial += s[i]
        elif i != 0 and es_un_digito(s[i]):
            numero_parcial += s[i]
        elif i != 0 and not es_un_digito(s[i]):
            res.append(numero_parcial)
            res.append(s[i])
            numero_parcial = ""
    res.append(numero_parcial)

    if s[0] == '-':
        res[0] = "-" + res[0]

    return res

pila_test : Pila[str] = Pila()
pila_test.put("1+2+3+4+5")
pila_test.put("1-2+3-4+5")
pila_test.put("-1+2-3-4-5")
pila_test.put("-100-100-100+5-100")
pila_test.put("-100-100-100+5-100")

print(resolver_cuentas(pila_test)) 

#---------------------------------------------------------------------------------------------------------

# Ejercicio 4
def dame_el_que_falta(s: list[tuple[int,int]]) -> tuple[int,int]:
    maximo : int = obtener_maximo_tupla(s)
    tuplas_totales : list[tuple[int,int]] = generar_tuplas_combinatoria(maximo)
    res : tuple[int,int] = (1,1)

    for tupla in tuplas_totales:
        if not esta_la_tupla_incluida(tupla, s):
            res = tupla
    return res

def obtener_maximo_tupla (tupla : list[tuple[int,int]]) -> int:
    maximo_primera_componente : int = tupla[0][0]
    maximo_segunda_componene : int = tupla[0][1]
    res : int = 0

    for i in range(len(tupla)):
        if tupla[i][0] > maximo_primera_componente:
            maximo_primera_componente = tupla[i][0]
        if tupla[i][1] > maximo_segunda_componene:
            maximo_segunda_componene = tupla[i][1]

    if maximo_primera_componente > maximo_segunda_componene:
        res = maximo_primera_componente
    else:
        res = maximo_segunda_componene

    return res
    
def esta_la_tupla_incluida ( tupla: tuple[int,int], tuplas : list[tuple[int,int]]) -> bool:

    for tup in tuplas:
        if tup == tupla:
            return True
    return False

def generar_tuplas_combinatoria (maximo: int) -> list[tuple[int,int]]:
    tuplas : list[tuple[int,int]] = []

    for i in range(1, maximo +1):
        for j in range(1, maximo +1):
            tuplas.append((i,j))
            
    return tuplas

s_test = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5,4), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
print(dame_el_que_falta(s_test))

