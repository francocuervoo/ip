def ultima_aparicion (s : list[int], e : int) -> int:
    
    aparicion : int = 0
    
    for i in range(len(s)):
        if s[i] == e:
            aparicion = i
            
    return aparicion

#print(ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1], 0))

# ------------------------------------------------------------------------------------

def elementos_exclsuivos ( s: list[int], t: list[int]) -> list[int]:
    lista_exclusiva : list[int] = []
    
    for elemS in s:
        if not pertenece_int(elemS, t) and not pertenece_int(elemS, lista_exclusiva):
            lista_exclusiva.append(elemS)
            
    for elemT in t:
        if not pertenece_int(elemT, s) and not pertenece_int(elemT, lista_exclusiva):
            lista_exclusiva.append(elemT)            
    
    return lista_exclusiva

def pertenece_int (elemento : int, conjunto : list[int]) -> bool:
    for elem in conjunto:
        if elemento == elem:
            return True
        
    return False
        
s = [-1,4,0,4,3,0,100,0,-1,-1]
t = [0,100,5,0,100,-1,5]    

#print (elementos_exclsuivos(s,t))

# ------------------------------------------------------------------------------------

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales ( ing : dict[str, str], ale : dict[str,str]) -> int:
    
    contador : int = 0
    
    for palabra in ing:
        if tiene_mimso_key_value(palabra, ing[palabra], ale):
            contador += 1
            
    return contador

def tiene_mimso_key_value ( key : str, value: str, diccionario : dict[str, str]) -> bool:
    
    diccionarioKeys = diccionario.keys()
        
    for elem in diccionario:
        if pertenece_str(key, diccionarioKeys):
            if diccionario[key] == value:
                return True
    return False

def pertenece_str ( elemento : str, conjunto : list[str]) -> bool:
    for elem in conjunto:
        if elem == elemento:
            return True
    return False        


    
    
aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}    

# FALTA REVISAR
    
print(contar_traducciones_iguales(aleman, inglés))