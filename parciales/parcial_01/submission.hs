module SolucionT1 where
--------------------------------------------------------------------------------------------------------------------------------------------------

-- Ejercicio 1
maxMovilN :: [Integer] -> Integer -> Integer
maxMovilN list n = obtenerMaximo (obtenerLosUltimosN list n)

obtenerLosUltimosN :: [Integer] -> Integer -> [Integer]
obtenerLosUltimosN [] _ = []
obtenerLosUltimosN [x] _ = [x]
obtenerLosUltimosN list n | longitud list == n = list
                          | otherwise = obtenerLosUltimosN (tail list) n

longitud :: [Integer] -> Integer
longitud [] = 0
longitud list = 1 + longitud (tail list) 
 
obtenerMaximo :: [Integer] -> Integer
obtenerMaximo [] = 0
obtenerMaximo [x] = x
obtenerMaximo (x:xs) | x > head xs = obtenerMaximo (x : tail xs)
                     | otherwise = obtenerMaximo xs

--------------------------------------------------------------------------------------------------------------------------------------------------

 -- Ejercicio 2
promedioPrimo :: Integer -> Float
promedioPrimo n = fromInteger (sumatoriaDeElementos (factoresPrimosDeN n 2)) / fromInteger (longitud (factoresPrimosDeN n 2))

sumatoriaDeElementos :: [Integer] -> Integer
sumatoriaDeElementos [] = 0
sumatoriaDeElementos [x] = x
sumatoriaDeElementos (x:xs) = x + sumatoriaDeElementos xs

factoresPrimosDeN :: Integer -> Integer -> [Integer]
factoresPrimosDeN n k | n == 1 = []
                      | esPrimo (menorDivisor n k) = menorDivisor n k : factoresPrimosDeN (div n (menorDivisor n k)) k
                      | otherwise = factoresPrimosDeN n k

esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo 2 = True
esPrimo n = menorDivisor n 2 == n

menorDivisor :: Integer -> Integer -> Integer
menorDivisor 1 _ = 1
menorDivisor n k | mod n k == 0 = k
                 | otherwise = menorDivisor n (k+1)

--------------------------------------------------------------------------------------------------------------------------------------------------

-- Ejercicio 3
letrasIguales :: String -> Integer
letrasIguales [] = 0
letrasIguales (x:xs) | x == ' ' = letrasIguales xs
                     | estaRepetidoCaracterX x (eliminarBlancos xs) = 1 + letrasIguales (eliminarCaracterX xs x)
                     | otherwise = letrasIguales xs

estaRepetidoCaracterX :: Char -> String -> Bool
estaRepetidoCaracterX _ [] = False
estaRepetidoCaracterX c (x:xs) | c == x = True
                               | otherwise = estaRepetidoCaracterX c xs

eliminarCaracterX :: String -> Char -> String
eliminarCaracterX [] _ = []
eliminarCaracterX (x:xs) c | x == c = eliminarCaracterX xs c
                           | otherwise = x : eliminarCaracterX xs c 

eliminarBlancos :: String -> String
eliminarBlancos [] = []
eliminarBlancos (x:xs) | x == ' ' = eliminarBlancos xs
                       | otherwise = x : eliminarBlancos xs

--------------------------------------------------------------------------------------------------------------------------------------------------

-- Ejercicio 4
cuantosIguales :: String -> String -> Integer
cuantosIguales [] [] = 0
cuantosIguales _ [] = 0
cuantosIguales [] _ = 0
cuantosIguales palabra1 palabra2 | head palabra1 == ' ' = cuantosIguales (eliminarBlancos palabra1) (eliminarBlancos palabra2)
                                 | head palabra2 == ' ' = cuantosIguales (eliminarBlancos palabra1) (eliminarBlancos palabra2)
                                 | estaRepetidoCaracterX (head palabra1) palabra2 = 1 + cuantosIguales (eliminarCaracterX palabra1 (head palabra1)) (eliminarCaracterX palabra2 (head palabra1))  
                                 | otherwise = cuantosIguales (tail palabra1) palabra2

