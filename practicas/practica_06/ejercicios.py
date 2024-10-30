# PRÁCTICA 6

# Tipar todas las funciones
# def funcion(numero: int) ->bool:

# Se pueden usar funciones matemáticas como por ejemplo:
# sqrt, round, floor, ceil, %
# import math 
# print(round(3.14159, 2))  # Output: 3.14
# print(round(3.5))         # Output: 4
# from math import floor
# print(floor(3.7))  # Output: 3
# from math import ceil
# print(ceil(3.2))  # Output: 4

# ------------------------------------------------------------------------------------------------------

import math 

# Ejercicio 1

# 1)
def imprimir_hola_mundo () -> None :
    print("¡Hola mundo!")

imprimir_hola_mundo()

# 2)
def imprimir_un_verso () -> None :
    verso : str = "Because maybe\nYou're gonna be the one that saves me\nAnd after all\nYou're my wonderwall"
    print(verso)

imprimir_un_verso()

# 3)
def raizDe2() -> float :
    raiz2 : float = math.sqrt(2)
    redondeo : float = round(raiz2, 4)
    return redondeo

print("La raiz de 2 es ", raizDe2())

# 4)
def factorial_2() -> int :
    res = 2 * 1
    return res

print("El factorial de 2 es ", factorial_2())

# 5)
def perimetro() -> float :
    res = 2 * math.pi
    return res

print("El perímetro de una circunferencia de radio 1 es ", perimetro())

# ------------------------------------------------------------------------------------------------------

# Ejercicio 2

# 1)
def imprimir_saludo( nombre : str ) -> None :
    print("Hola", nombre)

imprimir_saludo("Franco")
imprimir_saludo("Micaela")

# 2)
def raiz_cuadrada_de(numero : float) -> float :
    return math.sqrt(numero)

print("La raíz cuadrada del número 81 es", raiz_cuadrada_de(81))                     
print("La raíz cuadrada del número 8 es", raiz_cuadrada_de(8))
print("La raíz cuadrada del número 10,5 es", raiz_cuadrada_de(10.5))

# 3)
def fahrenheit_a_celsius (t : float) -> float :
    res : float = ((t-32) * 5) / 9
    return res
    
print("Paso 32ºF a Celcius:", fahrenheit_a_celsius(32))
print("Paso 212ºF a Celcius:", fahrenheit_a_celsius(212))

# 4)
def imprimir_dos_veces( estribillo : str) -> None :
    print (estribillo * 2)

imprimir_dos_veces("Because maybe\nYou're gonna be the one that saves me\nAnd after all\nYou're my wonderwall")

# 5)
def es_multiplo_de ( n : int, m : int) -> bool : 
    res = n % m == 0
    return res

print("El número 2 es múltiplo de 4", es_multiplo_de(2 , 4))
print("El número 9 es múltiplo de 3", es_multiplo_de(9 , 3))

# 6)
def es_par ( n : int) -> bool :
    res = es_multiplo_de(n, 2)
    return res

print("El número 4 es par", es_par(4))
print("El número 17 es par", es_par(17))

# 7)
def cantidad_de_pizzas(comensales : int, min_cant_de_porciones) -> int :
    porciones = comensales * min_cant_de_porciones
    return math.ceil(porciones/8)

print("Si viniesen 10 personas y cada una come 4 porciones, la cantidad de pizzas son", cantidad_de_pizzas(10, 4))
print("Si viniesen 4 personas y cada una come 3 porciones, la cantidad de pizzas son", cantidad_de_pizzas(4, 3))

# ------------------------------------------------------------------------------------------------------

# Ejercicio 3

# 1) 
def alguno_es_0(numero1 : float, numero2 : float) -> bool :
    return numero1 == 0 or numero2 == 0

print("El número 4 o 6 es 0", alguno_es_0(4,6))
print("El número 4 o 0 es 0", alguno_es_0(4,0))
print("El número 0 o 3 es 0", alguno_es_0(0,3))
print("El número 0 o 0 es 0", alguno_es_0(0,0))

# 2)
def ambos_son_0(numero1 : float, numero2 : float) -> bool :
    return numero1 == 0 and numero2 == 0

print("El número 4 y 6 son 0", ambos_son_0(4,6))
print("El número 4 y 0 son 0", ambos_son_0(4,0))
print("El número 0 y 3 son 0", ambos_son_0(0,3))
print("El número 0 y 0 son 0", ambos_son_0(0,0))

# 3)
def es_nombre_largo (nombre : str ) -> bool :
    largo : int = len(nombre)
    return largo >= 3 and largo <= 8

print("Franco es un nombre largo", es_nombre_largo("Franco"))
print("Al es un nombre largo", es_nombre_largo("Al"))

# 4)
def es_bisiesto(año : int) -> bool:
    multiplo400 : bool = es_multiplo_de(año, 400)
    multiplo4 : bool = es_multiplo_de(año, 4)
    multiplo100 : bool = es_multiplo_de(año, 100)
    return multiplo400 or (multiplo4 and not multiplo100)

print("El año 1984 es bisiesto", es_bisiesto(1984))
print("El año 1967 es bisiesto", es_bisiesto(1967))
print("El año 200 es bisiesto", es_bisiesto(200))

# ------------------------------------------------------------------------------------------------------

# Ejercicio 4

# 1)
def peso_pino (altura_mts : float) -> float :
    altura_cm = altura_mts * 100

    # Calculamos los primeros 300 cm con un factor de 3 kg por cm
    peso_primeros_3m = min(altura_cm, 300) * 3

    # Calculamos los centímetros por encima de 300 cm con un factor de 2 kg por cm
    peso_extra = max(0, altura_cm - 300) * 2    

    return peso_primeros_3m + peso_extra

    
print("El peso de un pino de 2 metros es", peso_pino(2))
print("El peso de un pino de 3 metros es", peso_pino(3))    
print("El peso de un pino de 4 metros es", peso_pino(4))  
print("El peso de un pino de 6 metros es", peso_pino(6))    

# 2)
def es_peso_util (peso : float) -> float :
    return peso >= 400 and peso <= 1000 

print("Un árbol de 400 kg le sirve a la fábrica", es_peso_util(400))
print("Un árbol de 200 kg le sirve a la fábrica", es_peso_util(200))
print("Un árbol de 900 kg le sirve a la fábrica", es_peso_util(900))
print("Un árbol de 1200 kg le sirve a la fábrica", es_peso_util(1200))
  
# 3) # 4)
def sirve_pino ( altura : float ) -> bool :
    peso : float = peso_pino(altura)
    return es_peso_util(peso)

print("Un árbol de 2 metros le sirve a la fábrica", sirve_pino(2))
print("Un árbol de 12 metros le sirve a la fábrica", sirve_pino(12))

# ------------------------------------------------------------------------------------------------------

# Ejercicio 5

# 1)
def devolver_el_doble_si_es_par ( numero : int ) -> int :
    if(es_par(numero)):
        return numero * 2
    return numero

print("Devolver el doble si es par de 22", devolver_el_doble_si_es_par(22))
print("Devolver el doble si es par de 23", devolver_el_doble_si_es_par(23))

# 2)
def devolver_valor_si_es_par_sino_el_que_sigue ( numero : int) -> int :
    if(es_par(numero)) :
        return numero 
    return numero + 1

print("Devuelvo el númeor par", devolver_valor_si_es_par_sino_el_que_sigue(22))
print("Devuelvo el siguiente numero porque es impar", devolver_valor_si_es_par_sino_el_que_sigue(23))

# 3)
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero : int) -> int :
    if (es_multiplo_de(numero, 3)) :
            return numero * 2
    if (es_multiplo_de(numero, 9)) :
            return numero * 3
    return numero

print("Devuelvo el doble porque es múltiplo de 3", devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(27))
print("Devuelvo el triple porque es múltiplo de 9", devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(81))
print("Devuelvo el mismo número porque no es múltiplo de 3 y 9", devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(22))

# 4)
def lindo_nombre ( nombre : str) -> None :
    largo : int = len(nombre)
    if (largo >= 5) :
        return print("Tu nombre tiene muchas letras")
    return print ("Tu nombre tiene menos de 5 letras")

lindo_nombre("Franco")
lindo_nombre("Alan")

# 5)
def elRango ( numero : float ) -> None :
    if (numero < 5 ) :
        return print("El número es menro a 5")
    if ( numero >= 10 and numero <= 20) :
        return print ("El número está entre 10 y 20")
    if ( numero > 20) :
        return print("El número es mayor a 20")
    return print ("No hay rango para ese número")

elRango(3)
elRango(9)
elRango(16)
elRango(161)

# 6)
def frase_segun_sexo_edad ( sexo : str , edad : int) :
    if (sexo == 'F') :
        if (edad >= 60 or edad <= 18) : return print("Andá de vacaciones")
        return print ("Te toca trabajar")
    if (sexo == 'M') :
        if (edad >= 65 or edad <= 18) : return print("Andá de vacaciones")
        return print ("Te toca trabajar")    
    
frase_segun_sexo_edad("M", 10)    
frase_segun_sexo_edad("M", 30)
frase_segun_sexo_edad("M", 70)
frase_segun_sexo_edad("F", 18)    
frase_segun_sexo_edad("F", 45)
frase_segun_sexo_edad("F", 62)

# ------------------------------------------------------------------------------------------------------

# Ejercicio 6

# 1)
def imprime_del_1_10() -> None :
    i : int = 1
    while i <= 10 :
        print(i)
        i += 1

imprime_del_1_10()

# 2) 
def imprime_numeros_pares_entre_10_40() -> None :
    i: int = 10
    while i<= 40 :
        print(i)
        i += 2

imprime_numeros_pares_entre_10_40()        

# 3)
def eco() -> None :
    i : int = 1
    while i <= 10 :
        print("Eco")
        i += 1

eco()        

# 4)
def cuenta_regresiva( inicio : int ) -> None :
    i : int = inicio
    while i > 0 :
        print(i)
        i -= 1
    print("Despegue")

cuenta_regresiva(20)    

# 5)
def monitoreo_en_el_tiempo (partida : int, llegada : int) -> None :
    i : int = partida
    print("Inicio viaje en el tiempo")
    while i > llegada :
        print("Estoy en el año", i)
        i -= 1
    print ("Llegue al año", llegada)    

monitoreo_en_el_tiempo(2024, 2001)    

# 6)
def monitoreo_en_el_tiempo_20 (partida : int) -> None :
    i : int = partida
    print("Inicio viaje en el tiempo")
    while i > -384 :
        print("Estoy en el año", i)
        i -= 20
    print ("Llegue a conocer a Aristóteles")    

monitoreo_en_el_tiempo_20(200)

# ------------------------------------------------------------------------------------------------------

# Ejercicio 7

# 1)
def for_imprime_del_1_10() -> None :
    for i in range(1,11):
        print(i)

for_imprime_del_1_10()

# 2) 
def for_imprime_numeros_pares_entre_10_40() -> None :
    for i in range(10, 41, 2):
        print(i)
    
for_imprime_numeros_pares_entre_10_40()

# 3)
def for_eco() -> None :
    for i in range(1, 11):
        print("Eco")

for_eco() 

# 4)
def for_cuenta_regresiva( inicio : int ) -> None :
    for i in range(inicio, 0, -1):
        print(i)
    print("Despegue")

for_cuenta_regresiva(12)   

# 5)
def for_monitoreo_en_el_tiempo (partida : int, llegada : int) -> None :
    print("Inicio viaje en el tiempo")
    for i in range(partida, llegada, -1):
        print("Año", i)
    print ("Llegue al año", llegada) 

for_monitoreo_en_el_tiempo(2024, 2001)  

# 6)
def for_monitoreo_en_el_tiempo_20 (partida : int) -> None :
    print("Inicio viaje en el tiempo")
    for i in range(partida, -384, -20):
        print("Estoy en el año", i)
    print ("Llegue a conocer a Aristóteles")    

for_monitoreo_en_el_tiempo_20(100)

# ------------------------------------------------------------------------------------------------------

# Ejercicio 8

# 1) x = 5 ;
#    y = 7 ;
#    x = x + y ;
# primero asigna 5 a la variable x
# segundo asigna 7 a la variable y
# finalmente asigna x + y = 12 a x, o sea x = 12 / y = 7

# 2) x = 5 ;
#    y = 7 ;
#    z = x + y ;
#    y = z * 2 ;
# primero asigna 5 a la variable x
# segundo asigna 7 a la variable y
# tercero asigna x + y = 12 a la variable z
# finalmente asigna z * 2 = 24 a la variable y / x = 5 / z = 12

# 3) x = 5 ;
#    y = 7 ;
#    x = "hora";
#    y = x * 2
# primero asigna 5 a la variable x
# segundo asigna 7 a la variable y
# tercero asigna "hora" a la variable x
# finalmente y = "hora" * 2 = "horahora"" / x = "hora"

# 4) x = False ;
#    res = not(x) ;
# primero asigna x = False
# segundo asigna res = True
# finalmente x = False / res = True

# 5) x = False ;
#    x = not(x) ;
# primero asigna x = False
# finalmente x = True

# 6) x = True ;
#    y = False ;
#    res = x and y ;
#    x = res and x ;
# primero asigna x = True
# segundo asigna y = False
# tercero asigna res = False
# finalmente x = False / y = False / res = False

# ------------------------------------------------------------------------------------------------------

# Ejercicio 9

def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

# ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?
# 2 3 4

# ¿Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
# 2 2 2

