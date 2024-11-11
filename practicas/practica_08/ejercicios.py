import random

from queue import LifoQueue as Pila
from queue import Queue as Cola

from typing import TypeVar
T = TypeVar('T')

# PILAS
# EJERCICIO 1

# 1)
def generar_nros_al_azar( cantidad : int, desde : int, hasta : int) -> Pila[int]:
    i : int = 0
    pilaNumeros = Pila()
    
    while i < cantidad:
        pilaNumeros.put(random.randint(desde,hasta))
        i+= 1
        
    return pilaNumeros

# pila_nuermos_azar = generar_nros_al_azar(10, 1, 10000)

# print("Contenido de la pila:")
# while not pila_nuermos_azar.empty():
#     print(pila_nuermos_azar.get())


# 2)
def cantidad_elementos ( p : Pila) -> int:
    cantidad : int = 0
    pila_temporal = Pila()
    
    while not p.empty():
        elemento = p.get()
        pila_temporal.put(elemento)
        cantidad += 1
        
    while not pila_temporal.empty():
        p.put(pila_temporal.get())        
    
    return cantidad
    
# pilaCantidad = Pila()
# pilaCantidad.put(1)
# pilaCantidad.put(2)
# pilaCantidad.put(3)

# print("Cantidad de elementos en la pila:", cantidad_elementos(pilaCantidad))

# print("Elementos en la pila después del conteo:")
# while not pilaCantidad.empty():    
#     print(pilaCantidad.get())

# 3)
def buscar_el_maximo ( p: Pila[int]) -> int:        
    pila_temporal = Pila()
    maximo = p.get()    
    pila_temporal.put(maximo)
    
    while not p.empty():
        elemento = p.get()
        if(elemento > maximo):
            maximo = elemento
        pila_temporal.put(elemento)    
        
    while not pila_temporal.empty():
        p.put(pila_temporal.get())    
        
    return maximo    

# pilaMaximo = Pila()
# pilaMaximo.put(10000)
# pilaMaximo.put(510000)
# pilaMaximo.put(3232)

# print("Busco el elemento máximo en la pila ", buscar_el_maximo(pilaMaximo))

# print("Elementos de la lista después de buscar el máximo:")
# while not pilaMaximo.empty():
#     print(pilaMaximo.get())

# 4)
def buscar_nota_maxima (p : Pila[tuple[str,int]]) -> tuple[str,int]:
    pila_temporal = Pila()
    nota_maxima = p.get()
    pila_temporal.put(nota_maxima)
    
    while not p.empty():
        elemento = p.get()
        if elemento[1] > nota_maxima[1]:
            nota_maxima = elemento
        pila_temporal.put(elemento)
        
    while not pila_temporal.empty():
        p.put(pila_temporal.get())    
        
    return nota_maxima

# pilaNotaMaxima = Pila()
# pilaNotaMaxima.put(("Civica", 7))
# pilaNotaMaxima.put(("Educación Física", 8))
# pilaNotaMaxima.put(("Computación", 9))

# print("Busco el elemento con nota máxima en la pila ", buscar_nota_maxima(pilaNotaMaxima))

# print("Elementos de la lista después de buscar la nota máxima:")
# while not pilaNotaMaxima.empty():
#     print(pilaNotaMaxima.get())    

# 5)
def esta_bien_balanceada (s :str) -> bool:
    pila = Pila()
    for char in s:
        if (char == "("):
            pila.put(char)
        if (char == ")"):
            if (pila.empty()):
                return False
            pila.get()
    
    return pila.empty()

# print(esta_bien_balanceada("1 + ( 2 * 3 - ( 20 / 5 ) )"))  # True
# print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( -1 ) ) )"))  # True
# print(esta_bien_balanceada("1 + ) 2 * 3 ( ( )"))  # False            
            
# 6)
def evaluar_expresion ( expresion : str) -> float:
    tokens : list[str] = split_propio(expresion)
    operadores : Pila = Pila()
    
    for token in tokens:
        if esta_incluido(token, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]):
            operadores.put(token)
            
        elif esta_incluido(token, ["+", "-", "*", "/"]):
            n1 : int = int(operadores.get()) # tomo los dos anteriores
            n2 : int = int(operadores.get())
            if token == "+":
                operadores.put(n2 + n1)
            if token == "*":
                operadores.put(n2 * n1)
            if token == "-":
                operadores.put(n2 - n1)
            if token == "/":
                operadores.put(n2 / n1)                                                
    return operadores.get()
    
#print(evaluar_expresion("3 4 + 5 * 2 -"))        
    
def split_propio (caracteres : str) -> list[str]:
    lista_caraceters : list[str] = []
    palabra_parcial : str = ""
    
    for caracter in caracteres:
        if caracter == " ":
            if palabra_parcial:
                lista_caraceters.append(palabra_parcial)
                palabra_parcial = ""
        else:
            palabra_parcial += caracter
                
    if palabra_parcial:
        lista_caraceters.append(palabra_parcial)            
    
    return lista_caraceters

def esta_incluido (elemento : T, conjunto: list[T]) -> bool:
    for element in conjunto:
        if element == elemento:
            return True
    return False        
      

# 7)    
def intercalar (p1: Pila, p2: Pila) -> Pila:   
    pila_final : Pila = Pila()
    
    p1_back_up : Pila = Pila()
    p2_back_up : Pila = Pila()    
    
    while not p1.empty() and not p2.empty():
        elemento_p1 = p1.get()
        elemento_p2 = p2.get()

        pila_final.put(elemento_p1)
        pila_final.put(elemento_p2)

        p1_back_up.put(elemento_p1)
        p2_back_up.put(elemento_p2)
        
    while not p1_back_up.empty():
        p1.put(p1_back_up.get())

    while not p2_back_up.empty():
        p2.put(p2_back_up.get())

    pila_resultado : Pila = Pila()
    
    while not pila_final.empty():
        pila_resultado.put(pila_final.get())

    return pila_resultado

   
# ------------------------------------------------------------------------------------------------------    
    
    
# COLAS
# EJERCICIO 2
    
# 8)    
def generar_nros_al_azar_cola (cantidad : int, desde : int, hasta : int) -> Cola[int]:
    cola_final : Cola = Cola()

    for i in range (0, cantidad):
        random_number : int = random.randint(desde, hasta)
        cola_final.put(random_number)
  
    return cola_final
        
#print(generar_nros_al_azar_cola(10,2,4))    
 
 # 9)   
def cantidad_elementos_cola (c : Cola) -> int:
    cantidad : int = 0
    nueva_cola : Cola = Cola()
    
    while not c.empty():
        nueva_cola.put(c.get())
        cantidad += 1

    while not nueva_cola.empty():
        c.put(nueva_cola.get())
    
    return cantidad

#print(cantidad_elementos_cola(cola_test))

# 10)
def buscar_el_maximo_cola (c : Cola[int]) -> int:
    c_buck_up : Cola[int] = Cola()
    
    maximo_parcial: int = c.get()
    c_buck_up.put(maximo_parcial)

    while not c.empty():
        elemento : int = c.get()
        c_buck_up.put(elemento)
        
        if elemento > maximo_parcial:
            maximo_parcial = elemento
            
    while not c_buck_up.empty():
        c.put(c_buck_up.get())      

    return maximo_parcial

# cola_test = Cola()
# cola_test.put(1)
# cola_test.put(2)
# cola_test.put(3)

# print("El maximo es", buscar_el_maximo(cola_test))

# while not cola_test.empty():
#     print(cola_test.get())

# 11)
def buscar_nota_minima_cola ( c: Cola[tuple[str, int]]) -> int:
    cola_temporal = Cola()
    
    tupla_minima : tuple[str,int] = c.get()
    cola_temporal.put(tupla_minima)
    
    while not c.empty():
        elemento : tuple[str,int] = c.get()
        cola_temporal.put(elemento)
        
        if(elemento[1]) < tupla_minima[1]:
            tupla_minima = elemento
        
    while not cola_temporal.empty():
        c.put(cola_temporal.get())
        
    return tupla_minima

# cola_test : Cola[tuple[str,int]] = Cola()
# cola_test.put(("Computación", 10))
# cola_test.put(("Lógica", 2))
# cola_test.put(("Matemática", 8))

# print("La nota mímima es ", buscar_nota_minima_cola(cola_test))

# 12)
def intercala_cola (c1: Cola, c2: Cola) -> Cola:
    
    cola_buck_up_1 = Cola()
    cola_buck_up_2 = Cola()
    cola_intercalada = Cola()
    
    while not c1.empty() and not c2.empty():
        elemento1 = c1.get()
        elemento2 = c2.get()
        
        cola_buck_up_1.put(elemento1)
        cola_buck_up_2.put(elemento2)
        
        cola_intercalada.put(elemento1)
        cola_intercalada.put(elemento2)
        
        
    while not cola_buck_up_1.empty():
        c1.put(cola_buck_up_1.get())
        
    while not cola_buck_up_2.empty():
        c2.put(cola_buck_up_2.get())        
        
    return cola_intercalada

# cola_test_1 = Cola()
# cola_test_2 = Cola()
# cola_test_1.put(1)
# cola_test_2.put(2)
# cola_test_1.put(3)
# cola_test_2.put(4)
# cola_test_1.put(5)
# cola_test_2.put(6)
# cola_test_1.put(7)
# cola_test_2.put(8)

# cola_test : Cola = intercala_cola(cola_test_1, cola_test_2)

# while not cola_test.empty():
#     print(cola_test.get())

# while not cola_test_1.empty():
#     print(cola_test_1.get())

# while not cola_test_2.empty():
#     print(cola_test_2.get())

# 13)
def armar_secuencia_de_bingo() -> Cola[int]:    
    secuencia = Cola()
    contador : int = 0
    lista_numeros : list[int] = []
    
    while contador < 100:
        lista_numeros.append(contador)
        contador += 1
        
    random.shuffle(lista_numeros)

    for elemento in lista_numeros:
        secuencia.put(elemento)

    return secuencia
    
# cola_test = armar_secuencia_de_bingo()

# while not cola_test.empty():
#     print(cola_test.get())

def jugar_carton_de_bingo( carton : list [int], bolillero : Cola[int]) -> int:
    bolillero_back_up = Cola()
    bolillero_back_up_2 = Cola()
        
    coincidencias : list[int] = []
    jugadas : int = 0

    print("Bolilleros", bolillero.queue)

    while not bolillero.empty():
        bol = bolillero.get()
        bolillero_back_up.put(bol)
        bolillero_back_up_2.put(bol)

    
    while len(coincidencias) < len(carton) and not bolillero_back_up.empty():
        bolilla : int = bolillero_back_up.get()              
        if esta_incluido(bolilla, carton):
            coincidencias.append(bolilla)
            
        jugadas += 1
        
    while not bolillero_back_up_2.empty():
        bolillero.put(bolillero_back_up_2.get())        
        
        
    print("Coincidencias", coincidencias)        
    return jugadas

# carton_test = [4, 12, 98, 3, 2, 55, 89, 43, 40, 32, 11, 90]
# bolillero_test = armar_secuencia_de_bingo()

# print(jugar_carton_de_bingo(carton_test, bolillero_test))

# 14)
def n_pacientes_urgentes ( c: Cola[tuple[int,str,str]]) -> int:
    cola_back_up = Cola()

    cantidad_pacientes : int = cantidad_elementos_cola(c)
    
    cola_pacientes_emergencia = Cola()
    
    for i in range (cantidad_pacientes):

        paciente : tuple[int,str,str] = c.get()
        
        cola_back_up.put(paciente)
        
        if paciente[0] > 0 and paciente[0] < 4:
            cola_pacientes_emergencia.put(paciente)

    print("Cola emergencia", cola_pacientes_emergencia.queue)

    while not cola_back_up.empty():
        c.put(cola_back_up.get())

    return cantidad_elementos_cola(cola_pacientes_emergencia)

# cola_pacientes = Cola()
# cola_pacientes.put((1, "Franco", "Especialidad"))
# cola_pacientes.put((2, "Micalea", "Especialidad"))
# cola_pacientes.put((4, "Nahuel", "Especialidad"))
# cola_pacientes.put((4, "Nahuel", "Especialidad"))


# print("Cantidad", n_pacientes_urgentes(cola_pacientes))

# print("Cola pacientes general", cola_pacientes.queue)

# 15)
def atencion_clientes ( c : Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str,int,bool,bool]]:
    # nombre_apellido , dni , isPreferencia, isPrioidad
    
    cola_clientes_back_up = Cola()

    cola_clientes_ordenada = Cola()
    cola_clientes_preferencial_ordenada = Cola()
    cola_clientes_resto_ordenada = Cola()
    
    while not c.empty():
        
        cliente : tuple[str, int, bool, bool] = c.get()
        
        cola_clientes_back_up.put(cliente)
        
        if cliente[3] == True: # Caso prioridad
            cola_clientes_ordenada.put(cliente)
        
        if cliente[2] == True and cliente[3] == False: # Caso preferencial
            cola_clientes_preferencial_ordenada.put(cliente)
            
        if cliente[2] == False and cliente[3] == False: # Caso resto
            cola_clientes_resto_ordenada.put(cliente)

    while not cola_clientes_preferencial_ordenada.empty():
        cola_clientes_ordenada.put(cola_clientes_preferencial_ordenada.get())
        
    while not cola_clientes_resto_ordenada.empty():
        cola_clientes_ordenada.put(cola_clientes_resto_ordenada.get())        


    while not cola_clientes_back_up.empty():
        c.put(cola_clientes_back_up.get())

    return cola_clientes_ordenada


cola_clientes_test = Cola()
cola_clientes_test.put(("Franco Monterubbianesi", "1", False, False))
cola_clientes_test.put(("Micaela Miele", "2", False, True))
cola_clientes_test.put(("Enrique Miele", "3", True, False))
cola_clientes_test.put(("Elsa Ruffolo", "4", False, True))
cola_clientes_test.put(("José Luis Rodríguez Pagani", "5", True, True))

#print(cola_clientes_test.queue)

#cola_clientes_actualizada_test = atencion_clientes(cola_clientes_test)

#print(cola_clientes_actualizada_test.queue)


# ------------------------------------------------------------------------------------------------------

# DICCIONARIOS

# EJERCICIO 16
def agrupar_por_longitud ( nombre_archivo: str ) -> dict:
    lista_de_palabras_del_archivo = obtener_palabras_del_archivo(nombre_archivo)
    
    diccionario_longitud_palabras : dict = {}
    
    longitud_palabra : int = 0
    
    for palabra in lista_de_palabras_del_archivo:
        longitud_palabra = len(palabra)
        
        if pertenece_key(longitud_palabra, diccionario_longitud_palabras):
            diccionario_longitud_palabras[longitud_palabra] += 1
        
        else:
            diccionario_longitud_palabras[longitud_palabra] = 1
        
    return diccionario_longitud_palabras

def obtener_palabras_del_archivo (nombre_archivo : str) -> list[str]:
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    archivo.close()
    
    lista_de_palabras : list[str] = []
    palabra_parcial : str = ""

    for element in contenido:
        
        if element != " ":
            palabra_parcial += element
            
        else : 
            if palabra_parcial:
                lista_de_palabras.append(palabra_parcial)
                palabra_parcial = ""    
            
    if palabra_parcial:
        lista_de_palabras.append(palabra_parcial)

    return lista_de_palabras

def pertenece_general ( elemento : T, conjunto:list[T]) -> bool:
    for elem in conjunto:
        if elemento == elem:
            return True
    return False

def pertenece_key ( elemento : T, diccionario: dict[T, T]) -> bool:
    lista_keys : list[T] = diccionario.keys()

    for elem in lista_keys:
        if elemento == elem:
            return True
    return False

#print(agrupar_por_longitud('file-test.txt'))


# EJERCICIO 17
def calcular_promedio_por_estudiante (notas : list[tuple[str, float]]) -> dict[str, float]:
    # (nombre_estudiante, nota_examen)
    diccionario_notas: dict[str, list[float]] = {}

    for nombre, nota in notas:
        if pertenece_key(nombre, diccionario_notas):
            diccionario_notas[nombre].append(nota)
        else:
            diccionario_notas[nombre] = [nota]

    # Calcular promedios manualmente sin `sum`
    diccionario_promedio: dict[str, float] = {}
    for nombre, lista_notas in diccionario_notas.items():
        suma_notas = 0
        contador = 0
        for nota in lista_notas:
            suma_notas += nota
            contador += 1
        diccionario_promedio[nombre] = suma_notas / contador

    return diccionario_promedio

#nota_test = [("Franco", 3), ("Micaela", 2), ("Alan", 10), ("Micaela", 7), ("Franco", 4)]

#print(calcular_promedio_por_estudiante(nota_test))


# EJERCICIO 18
def la_palabra_mas_frecuente (nombre_archivo : str) -> str:

    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    archivo.close()

    lista_de_palabras_del_archivo : list[str] = []
    palabra_parcial : str = ""

    diccionaro_de_palabras : dict[str, int] = {}
    
    palabra_frecuente : tuple[int,str] = (0, "")
       
    for caracter in contenido:
        if caracter != " ":
            palabra_parcial += caracter
        
        else: 
            lista_de_palabras_del_archivo.append(palabra_parcial)
            palabra_parcial = ""
            
    if palabra_parcial:
        lista_de_palabras_del_archivo.append(palabra_parcial)
        
    for palabras in lista_de_palabras_del_archivo:
        
        if pertenece_key(palabras, diccionaro_de_palabras):
            diccionaro_de_palabras[palabras] += 1
            
        else:
            diccionaro_de_palabras[palabras] = 1

    for key , value in diccionaro_de_palabras.items():
        if value > palabra_frecuente[0]:
            palabra_frecuente = (value, key) 
        
    return palabra_frecuente[1]
            
#print(la_palabra_mas_frecuente('file-test.txt'))


# EJERCICIO 19
historiales : dict[str, Pila] = {}

historial_franco = Pila()
historial_franco.put("www.google.com")
historial_franco.put("www.promiedos.com.ar")
historial_franco.put("www.cubawiki.com.")

historial_micaela = Pila()
historial_micaela.put("www.guru.com")
historial_micaela.put("www.carestino.com")
historial_micaela.put("www.google.com")
historial_micaela.put("www.premiumbaby.com")

historiales["Franco"] = historial_franco
historiales["Micaela"] = historial_micaela


def visitar_sitio ( historiales : dict[str, Pila[str]] , usuario : str, sitio : str) -> None:
    
    for usuario_historial , pila_historial in historiales.items():

        if usuario == usuario_historial:
            
            pila_historial.put(sitio)
        
#visitar_sitio(historiales, "Micaela", "www.test.com")

#print(historiales["Micaela"].queue)

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str):
    
    sitio_actual = historiales[usuario].get()
    
    if not historiales[usuario].empty():
        sitio_anterior = historiales[usuario].get()

        historiales[usuario].put(sitio_actual)
        historiales[usuario].put(sitio_anterior)
    else:
        historiales[usuario].put(sitio_actual)
                
                
# EJERCICIO 20
inventario: dict[str, dict[str, float | int]] = {
    "camiseta": {
        "precio": 19.99,
        "cantidad": 50
    },
    "pantalones": {
        "precio": 39.99,
        "cantidad": 30
    },
    "zapatos": {
        "precio": 59.99,
        "cantidad": 20
    },
    "sombrero": {
        "precio": 14.99,
        "cantidad": 15
    }
}         
                
def agregar_producto ( inventario : dict[str, dict[ str, float | int]], nombre : str, precio: float, cantidad: int) -> None:
        
    nuevo_producto : dict[str, float | int] = {
        "precio": precio,
        "cantidad": cantidad
    }
                    
    inventario[nombre] = nuevo_producto
                
#print("inventario", inventario)                
#agregar_producto ( inventario, "chaqueta", 89.99, 10)
#print("inventario", inventario)
                
def actualizar_stock ( inventario : dict[str, dict[ str, float | int]], nombre : str, cantidad: int) -> None:
    
    if pertenece_key(nombre, inventario):
        inventario[nombre]["cantidad"] = cantidad
                
#print("inventario", inventario)
#actualizar_stock(inventario, "sombrero", 30)                
#print("inventario", inventario)
                
def actualizar_precios ( inventario : dict[str, dict[ str, float | int]], nombre : str, precio: float) -> None:
    
    if pertenece_key(nombre, inventario):
        inventario[nombre]["precio"] = precio
                
#print("inventario", inventario)
#actualizar_precios(inventario, "pantalones", 15)                
#print("inventario", inventario)                
                
def calcular_valor_intervalo ( inventario : dict[str, dict[str, float | int]]) -> float:
    total : float = 0
    
    for nombre_producto , valores in inventario.items():        
        total += inventario[nombre_producto]["precio"] * inventario[nombre_producto]["cantidad"]
                
    return total                
                
print(calcular_valor_intervalo(inventario))                
                

# ------------------------------------------------------------------------------------------------------

# ARCHIVOS
# EJERCICIO 21

# 1)
def contar_lineas (nombre_archivo:str) -> int:
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    
    lineas = archivo.readlines()
    cantidad_lineas = len(lineas)
    archivo.close()
    
    return cantidad_lineas


# EJERCICIO 22
# LA FUNCIÓN AUXILIAR TIENE QUE VERIFICAR QUE DESPUÉS DE LOS ESPACIOS HAYA UN #