module Parcial_2 where

type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

-- Ejercicio 1
maximo :: Tablero -> Int
maximo [[]] = 0
maximo [list] = maximoEnFila list
maximo (list:lists) | maximoEnFila list > maximoEnFila (head lists) = maximo (list : tail lists)
                    | otherwise = maximo lists  

maximoEnFila :: Fila -> Int
maximoEnFila [] = 0
maximoEnFila [x] = x
maximoEnFila (x:xs) | x > head xs = maximoEnFila (x : tail xs)
                    | otherwise = maximoEnFila xs

-- Ejercicio 2
masRepetido :: Tablero -> Int
masRepetido [[]] = 0
masRepetido (list:lists) = maximaRepeticionEnFilas list (list:lists)

maximaRepeticionEnFilas :: Fila -> Tablero -> Int
maximaRepeticionEnFilas [] [[]] = 0
maximaRepeticionEnFilas [x] tablero = masRepetidoEnFila [x] tablero
maximaRepeticionEnFilas (x:xs) tablero | cantidadDeRepeticionesEnFilas x tablero > cantidadDeRepeticionesEnFilas (head xs) tablero = maximaRepeticionEnFilas (x : tail xs) tablero
                                       | otherwise =  maximaRepeticionEnFilas xs tablero

masRepetidoEnFila :: Fila -> Tablero -> Int
masRepetidoEnFila [] [[]] = 0
masRepetidoEnFila [x] tablero | cantidadDeRepeticionesEnFilas x tablero == 0 = 0
                              | otherwise = x
masRepetidoEnFila (x:xs) tablero | cantidadDeRepeticionesEnFilas x tablero > cantidadDeRepeticionesEnFilas (head xs) tablero = masRepetidoEnFila (x : tail xs) tablero
                                 | otherwise = masRepetidoEnFila xs tablero
                              

cantidadDeRepeticionesEnFilas :: Int -> Tablero -> Int
cantidadDeRepeticionesEnFilas n [[]] = 0
cantidadDeRepeticionesEnFilas n [list] = cantidadDeRepeticionesEnFila n list
cantidadDeRepeticionesEnFilas n (list:lists) = cantidadDeRepeticionesEnFila n list + cantidadDeRepeticionesEnFilas n lists


cantidadDeRepeticionesEnFila :: Int -> Fila -> Int
cantidadDeRepeticionesEnFila n [] = 0
cantidadDeRepeticionesEnFila n list | n == head list = 1 + cantidadDeRepeticionesEnFila n (tail list)
                                    | otherwise = cantidadDeRepeticionesEnFila n (tail list)


-- [[13, 12, 6, 4] , [1, 1, 32, 25] , [9, 2, 14, 7] , [7, 3, 5, 16 ] , [27, 2, 8, 18]]

-- [13, 12, 6, 4] [[13, 12, 6, 4] , [1, 13, 12, 12]]


