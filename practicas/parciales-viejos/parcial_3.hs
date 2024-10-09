module Parcial_3 where

-- Ejercicio 1
divisoresPropios :: Int -> [Int]
divisoresPropios 1 = [1]
divisoresPropios n = 1 : obtenerSiguientesDivisores n 2

obtenerSiguientesDivisores :: Int -> Int -> [Int]
obtenerSiguientesDivisores 1 k = [1]
obtenerSiguientesDivisores n k | n == k = [] 
                               | mod n k == 0 = k : obtenerSiguientesDivisores n (k+1) 
                               | otherwise = obtenerSiguientesDivisores n (k+1) 


-- Ejercicio 2
sumarNumeros :: [Int] -> Int
sumarNumeros [] = 0
sumarNumeros [n] = n
sumarNumeros (x:xs) = x + sumarNumeros xs

sonAmigos :: Int -> Int -> Bool
sonAmigos n m = sumarNumeros (divisoresPropios n) == m && sumarNumeros (divisoresPropios m) == n


-- Ejercicio 3
losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n = revertir (listaNumerosPerfectos n 2 [])



listaNumerosPerfectos :: Int -> Int -> [Int] -> [Int]
listaNumerosPerfectos 1 k list = [6]
listaNumerosPerfectos n k list | longitud list == n = list
                               | esNumeroPerfecto k = listaNumerosPerfectos n (k+1) (k:list)
                               | otherwise = listaNumerosPerfectos n (k+1) list     

siguienteNumeroPerfecto :: Int -> Int
siguienteNumeroPerfecto n | esNumeroPerfecto (n+1) = n+1
                          | otherwise = siguienteNumeroPerfecto (n+1)

esNumeroPerfecto :: Int -> Bool
esNumeroPerfecto n = sumarNumeros (divisoresPropios n) == n

revertir :: [Int] -> [Int]
revertir [] = []
revertir (x:xs) = revertir xs ++ [x]

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

