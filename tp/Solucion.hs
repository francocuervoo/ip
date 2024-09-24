-- divididos.3
-- Franco Monterubbianesi / 37989929
-- José Ignacio Nieva / 40226694
-- Jeremías Fernández / 43173917

module Solucion where

type Ciudad = String
type Duracion = Float
type Vuelo = (Ciudad, Ciudad, Duracion)

type AgenciaDeViajes = [Vuelo]

-- EJERCICIO 1
vuelosValidos :: AgenciaDeViajes -> Bool
vuelosValidos vuelos = not (vuelosRepetidos vuelos) && cuidadesRepetidasDistintaDuracion vuelos && todosLosVuelosSonValidos vuelos

vueloValido :: Vuelo -> Bool
vueloValido (c1, c2, d) | d > 0 && c1 /= c2 = True
                         | otherwise = False

todosLosVuelosSonValidos :: AgenciaDeViajes -> Bool
todosLosVuelosSonValidos [] = False
todosLosVuelosSonValidos [x] = vueloValido x
todosLosVuelosSonValidos (x:xs) | not (vueloValido x) = False
                                | otherwise = todosLosVuelosSonValidos xs

vuelosRepetidos :: AgenciaDeViajes -> Bool
vuelosRepetidos [] = False
vuelosRepetidos [_] = False
vuelosRepetidos (x:xs) = vueloRepetido x (head xs) || vuelosRepetidos xs

vueloRepetido :: Vuelo -> Vuelo -> Bool
vueloRepetido (c11, c12, d1) (c21, c22, d2) = c11 == c21 && c12 == c22  && d1 == d2

cuidadesRepetidasDistintaDuracion :: AgenciaDeViajes -> Bool
cuidadesRepetidasDistintaDuracion [] = False
cuidadesRepetidasDistintaDuracion [_] = False
cuidadesRepetidasDistintaDuracion (x:xs) = cuidadRepetidaDistintaDuracion x (head xs) || cuidadesRepetidasDistintaDuracion xs

cuidadRepetidaDistintaDuracion :: Vuelo -> Vuelo -> Bool
cuidadRepetidaDistintaDuracion (c11, c12, d1) (c21, c22, d2) = c11 == c21 && c12 == c22 && d1 /= d2










-- EJERCICIO 2
ciudadesConectadas :: AgenciaDeViajes -> Ciudad -> [Ciudad]
ciudadesConectadas _ _ = ["BsAs"] -- Borrar y escribir el código correcto

-- EJERCICIO 3
modernizarFlota :: AgenciaDeViajes -> AgenciaDeViajes
modernizarFlota _ = [("BsAs","Rosario",9.0)] -- Borrar y escribir el código correcto


-- EJERCICIO 4
ciudadMasConectada :: AgenciaDeViajes -> Ciudad
ciudadMasConectada _ = "Rosario" -- Borrar y escribir el código correcto


-- EJERCICIO 5
sePuedeLlegar :: AgenciaDeViajes -> Ciudad -> Ciudad -> Bool
sePuedeLlegar vuelos origen destino = True -- Borrar y escribir el código correcto


-- EJERCICIO 6
duracionDelCaminoMasRapido :: AgenciaDeViajes -> Ciudad -> Ciudad -> Duracion
duracionDelCaminoMasRapido _ _ _ = 10.0 -- Borrar y escribir el código correcto



-- EJERCICIO 7
puedoVolverAOrigen :: AgenciaDeViajes -> Ciudad ->  Bool
puedoVolverAOrigen vuelos origen = True -- Borrar y escribir el código correcto