## Teórica 03
- (Diapo clase 02)
Si específico de mas -> sobre especificación
En el ejemplo de sobre-espeficación, en el primer ejemplo satisface que es distinto pero sobre-especificando.

Si específico de menos -> sub especificación
en este este ejemplo, en el primero, estoy subespecificando solo para los positivos y está mal

No hay que pedir de mas y ni pedir de menos.

el T es un tipo paramétrico

en el ejemplo de esPermutaciones -> es un caso de Top / Down

- (Diapo clase 03)
Extensión de archivos haskell .hs
Algoritmo: conjunto de pasos para resolver un problema.
En Haskell el lado izquierdo es la expresión a definir y el lado derecho la definición.
El reemplazo es de izquierda a derecha pero no de derecha a izquierda.

La función suc(x) = x+1 
Suc de sucesor

La función div es la división entera div 12 5 = 2

mod nos da el resto de la división entera
ord el número que tiene en la tabla ASCII
y chr es la inversa, les dás un número de la tabla ASCII y me da el número

Variables de tipos
identidad:: t -> t
es una variable de tipo t, lo cual permite que sea de diferentes tipos

ahora si tengo
primero:: t -> t -> t
siempre será de tipo t

primero:: t -> s -> t
diferentes tipos

contanste5 x y z = 5
podría ser:
constante5:: t -> r -> s -> Int

La diferencia entre el tipo Int / Integer, es Integer te permite números más grandes
Lo mismo para Float / Double, Double permite un decimal más preciso que Float.

Abs -> valor absoluto

Eq permite saber si dos elementos son iguales

El comando ghci ejecuta Haskell
Comando para irse   ::q

triple:: (Num t) -> t -> t
(Num t) le pide a t que sea un Num

cantidadDeSoluciones:: (Num t, Ord t) -> t -> t -> Int
(Num t, Ord t) le pide a t que sea Nom y Ord

:type + la función me da el tipado que tiene una función

Diferencia entre tupla / secuencia
- secuencia no puede tener diferentes tipos y puede cambiar su tamaño
- tuplas si puede tener diferentes tipos pero su tamaño no cambia

La programación funcional nos permite aplicar funciones parciales
por ejemplo:
suma :: int -> int -> int
suma x y = x + y

sumaCinco :: int -> int
sumaCinco = suma 5 -> es una nueva función que está esperando el segundo parámetro para devolver int