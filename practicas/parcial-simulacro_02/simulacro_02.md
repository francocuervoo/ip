## Enunciado
Resolver los siguientes ejercicios cuyas especificaciones figuran a continuación. Deben ser implementadas en Python utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).

## 1) Gestión de notas de estudiantes [2 puntos]
En una escuela llamada "Academia Futura", se desea desarrollar un programa para gestionar las notas de los estudiantes por materia. El programa debe procesar una lista de tuplas donde cada tupla contiene el nombre de un estudiante, el nombre de una materia y la nota final obtenida por el estudiante en esa materia.

Se pide implementar una función en python, que respete la siguiente especificación:

problema gestion_notas (in notas_estudiante_materia: seq⟨(String x String x Z)) : dict⟨String, seq⟨(String x Z)⟩⟩ {
  requiere: { Las primeras componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las segundas componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las terceras componentes de notas_estudiante_materia están entre 1 y 10, ambos inclusive }
  requiere: { No hay 2 tuplas en notas_estudiante_materia que tengan la primera y segunda componente iguales (mismo estudiante y misma materia) }
  asegura: {res tiene como claves solo los primeros elementos de las tuplas de notas_estudiante_materia (o sea, un estudiante)}
  asegura: {El valor en res de un estudiante es una lista de tuplas donde cada tupla contiene como primera componente el nombre de la materia y como segunda componente la nota obtenida por el estudiante en esa materia según notas_estudiante_materia}
  asegura: { Para toda clave (estudiante) en res, en su valor (lista de tuplas) no hay 2 tuplas que tengan la misma primera componente (materia) }
}

## 2) Cantidad dígitos pares [2 puntos]
Se pide implementar una función en Python llamada cantidad_digitos_pares que respete la siguiente especificación:

problema cantidad_digitos_pares (in numeros: seq⟨Z⟩) : Z {
  requiere:{Todos los elementos de numeros son mayores iguales a 0}
  asegura: {res es la cantidad total de digitos pares que aparecen en cada uno de los elementos de numeros}
}

Por ejemplo, si la lista de números es [5434, 42, 811, 3139], entonces el resultado esperado sería 5 (los dígitos pares son 4, 4, 4, 2, y 8).

## 3) Priorizar cola de paquetes [2 puntos]
En una empresa de logística, se manejan paquetes que llegan a una bodega y deben ser procesados para su posterior distribución. Cada paquete está representado por una tupla (id_paquete, peso), donde id_paquete es un identificador único del paquete y peso representa el peso del paquete en kilogramos.

Se pide implementar una función en Python llamada reordenar_cola_primero_pesados que respete la siguiente especificación:

problema reordenar_cola_primero_pesados(in paquetes: Cola⟨(String x Z)⟩, in umbral:Z): Cola⟨(String x Z)⟩{
  requiere: {no hay repetidos en las primeras componentes (Ids) de paquetes}
  requiere: {todos las segundas componentes (pesos) de paquetes son mayores estricto a cero}
  requiere: {umbral es mayor o igual a cero}
  asegura: {los elementos de res son exactamente los mismos que los elementos de paquetes}
  asegura: {|res| = |paquetes|}
  asegura: {no hay un elemento en res, cuyo peso sea menor o igual que el umbral, que aparezca primero que otro elemento en res cuyo peso sea mayor que el umbral)}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son menores o iguales que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en paquetes entonces p1 aparece primero que p2 en res}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son mayores que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en paquetes entonces p1 aparece primero que p2 en res}
}

## 4) Matriz pseudo ordenada [2 puntos]
Se desea verificar si una matriz está pseudo ordenada por columnas. Esto es que el mínimo de cada columna sea menor estricto que el mínimo de la columna siguiente

Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:

matriz_pseudo_ordenada (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {todos los elementos de matriz tienen la misma longitud}
  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el mínimo de la columna i de matriz < el mínimo de la columna i + 1 de matriz }
}