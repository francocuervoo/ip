# Usar siempre python3
# quit() para salir de python
# import FILE_NAME para importar el archivo
# FILE_NAME.FUNCTION_NAME ejecuta la función

import math 

# Ejercicio 1.1
def imprimir_hola_mundo():
    print("Hola mundo")

imprimir_hola_mundo()


# Ejericio 1.5
def perimetro() -> float :
    return 2 * math.pi # Llamo al número pi

print(perimetro())


# Ejercicio 2.5
def es_multiplo_de(n : int , m : int) -> bool :
    res : bool = n % m == 0
    return res

print("Es multiplo 9,3", es_multiplo_de(9,3)) # True
print("Es multiplo 5,3", es_multiplo_de(5,3)) # False


# Ejercicio 3
def es_nombre_largo(nombre: str) -> bool :
    largo : int = len(nombre)
    return largo >= 3 and largo <= 8

print("Es nombre largo Franco", es_nombre_largo("Franco"))
print("Es nombre largo Al", es_nombre_largo("Al"))


# Ejercicio 5.1
def devolver_el_doble_si_es_par(n : int) -> int :
    esPar : bool = es_multiplo_de(n,2)

    if(esPar) :
        return 2 * n
    
    else :
        return n

print("Devolver el doble si es par de 3", devolver_el_doble_si_es_par(3))
print("Devolver el doble si es par de 6", devolver_el_doble_si_es_par(6))


# Ejercicio 6.2
def imprime_pares_10_40() -> None : # función que no retorna nada se tipa none
    i : int = 10
    while i <= 40:
        print(i)
        i += 2

print("Imprimo los pares desde 10 a 40")
imprime_pares_10_40()

def cuenta_regresiva(n : int) -> None :
    while n > 0:
        print (n)
        n -= 1

    print("Despegue 🚀")


print("Inicio despegue")
cuenta_regresiva(10)    


# Ejercicio 7
# range(4,9,1) -> empieza del 4, le va sumando 1 y termina en 9 (pero el 9 no lo incluye)
#              -> el último parámetro, no es obligatorio. range(4,9) desvuelve 4,5,6,7,8
#              -> y el primero tampoco es obligatorio. range(9) devuelve 0,1,2,3,4,5,6,7,8

def imprime_pares_10_40_for():
    for i in range(10,41,2):
        print(i)

print("Imprimo los pares desde 10 a 40 utlizando for")
imprime_pares_10_40_for()        


def cuenta_regresiva_for(n :int):
    for i in range(n,0, -1):
        print(i)

    print("Despegue 🚀")

print("Iniciando despegue for")
cuenta_regresiva_for(10)            


## Ejercicio SIMILAR 9
def ejemploArgumento(xArgumento : int):
    print("En ejemploArgumento: ", xArgumento)
    xArgumento = xArgumento + 40

def ejemploVarGlobal() :
    global xGlobal # Corrobora la existencia de xGlobal
    print("En ejemploVarGlobal ", xGlobal)
    xGlobal = xGlobal + 30   

xGlobal : int = 1

ejemploArgumento(xGlobal)
print("En codigo libre ", xGlobal)

ejemploVarGlobal()
print("En codigo libre ", xGlobal)

ejemploArgumento(xGlobal)
print("En codigo libre: ", xGlobal)

ejemploVarGlobal()
print("En codigo libre:", xGlobal)