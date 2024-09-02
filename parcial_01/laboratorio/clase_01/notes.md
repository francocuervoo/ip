Profesor: Juan Pablo Benedetti
Ayudantes: Fausto y Alejo
Comisión: D
Aula: 1104

TP
- tienen que ser compañeros de la misma comisión
- en Haskell

Exactas -> Estudiantes (ver actividades para estudiante)

Lunes / miércoles -> diferentes docentes

---

Ejercicio 10
f = "es fin de semana"
e = "Juan estudia"
m = "Juan escucha música"

a) Escribir usando lógica proposicional las siguientes oraciones
- "Si es un fin de semana, Juan estudia o escucha música, pero no ambas"
  f -> (eVm) ^ -(e^m)

- "Si no es fin de semana entonces Juan no estudia"
  -f -> -e

- "Cuando Juan estudia los fines de semana, lo hace escuchando música"
  ( e ^ f ) -> m

---

Lógica ternaria o trivalente
^L VL ->L depende de lo que pase a la izquierda.

True V undefined = undefined
False ^ undefined = undefined
True VL undefined = True
False ^L undefined = False


Ejercicio 17
x y -> undefined
b c -> true
a -> false

a) (-x VL b)
   como x es undefined ya es undefined

c) -(c VL y)
   -(true VL undefined)
   -(true) es false

e) ((c VL y) ^L (a VL b))
   ((true) ^L (true))
   true

g) (-c ^L -y)
   (false ^L -y) 
   false