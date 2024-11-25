from typing import TypeVar

T = TypeVar('T')

def leer_lineas_0 ( nombre_archivo : str) :
    archivo = open(nombre_archivo, 'r', encoding = 'utf-8')
    lineas:list[str] = archivo.readlines()
    
    for linea in lineas:
        print (linea)
    
    archivo.close() #siempre cerrar el archivo        

def escribir ( nombre_archivo: str, txt: str) -> None:
    archivo = open(nombre_archivo, 'w')
    archivo.write(txt)
    archivo.close()
        
def escribir_agregando_al_final (nombre_archivo : str, frase: str) -> None:
    archivo = open(nombre_archivo, 'a')    
    archivo.write(frase)
    archivo.close()
    
    
    