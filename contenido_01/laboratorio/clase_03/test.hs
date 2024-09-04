-- Así hago comentarios

doubleMe :: Int -> Int
doubleMe x = x + x

suma :: Int -> Int -> Int
suma x y = x + y 


-- Ejercicio 1

-- a)
f :: Int -> Int
f 1 = 8
f 4 = 131
f 16 = 16

-- b)
g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

-- c)
h :: Int -> Int
h x = f (g x)

k :: Int -> Int
k x = g (f x)


-- Ejercicio 2

-- c
{- Especificación
    problema maximo3 (x, y, z: Z) : Z {
        requiere: { True }
        asegura: { res es igual a x o a y o a z },
        asegura: { res es mayor igual a x y a y a z}
    }
-}

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z = maximo ( maximo x y) z

maximo :: Int -> Int -> Int
maximo x y | x > y = x  
           | otherwise = y               

-- Para pasarle un negativo, pasarlo con paréntesis. Ej: (-1)

-- g
{- Especificación
    problema sumaDistintos (x, y, z : Z) :Z {
        requiere: { True }
        asegura: { si x != y != z , res = x + y + z
                   si x = y = z  ,  res = x 
                   si x = y , res = x + z
                   si x = z , res = x + y }
                 }
    }            

    Otra manera:
    si los 3 parámetros son distintos entre si res = x + y + z
    ...
    si los 3 parámetros son iguales entre si res = x

-}

sudaDistintos :: Int -> Int -> Int -> Int
sudaDistintos x y z | x == y &&  y == z = x
                    | x == y = z + x
                    | x == z || y == z = x + y
                    | otherwise = x + y + z


-- i
{-
    Especificación
    problema digitoUnidades ( x : Z ) : Z {
    requiere : { True }
    asegura : { res es el dígito de las unidades de x} 
    }
-}                    

digitoUnidades :: Int -> Int
digitoUnidades x | x < 0 = (-x) `mod` 10
                 | otherwise = x `mod` 10

-- j
{-
    Espeficación
    problema digitoDecenas (x : Z ) : Z {
        requiere: { True }
        asegura: { result es el dígito de x correspondiente a las decenas }
    }
-}   

sacarUnidades :: Int -> Int
sacarUnidades x | x >= 0 = x `div` 10
                | otherwise = (-x) `div` 10

digitoDecenas :: Int -> Int
digitoDecenas x = digitoUnidades(sacarUnidades(x))


-- Ejercicio 4
--b 
{-
    Especificación
    problema todoMenor( t1, t2 : RxR ) : Bool {
        requiere: { True }
        asegura: { res = true <-> la componente de cada tupla es menor a la segunda}
    }
-}

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
--todoMenor t1 t2 = fst t1 < fst t2 && snd t1 < snd t2
todoMenor (a,b) (c,d) = a < c && b < d