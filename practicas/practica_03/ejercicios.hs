-- Ejercicio 1

-- a)
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

-- b)
g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- c)
h :: Integer -> Integer
h x = f (g x)

k :: Integer -> Integer
k x = g (f x)

-- Ejercicio 2

-- a)
absoluto :: Integer -> Integer
absoluto n
  | n < 0 = n * (-1)
  | otherwise = n

-- b)
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m
  | absoluto n >= absoluto m = absoluto n
  | otherwise = absoluto m

-- c)
maximo :: Int -> Int -> Int
maximo x y
  | x > y = x
  | otherwise = y

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z = maximo (maximo x y) z

-- d)
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y | x == 0 = True
              | y == 0 = True
              | otherwise = False

algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM 0 _ = True  
algunoEs0PM _ 0 = True
algunoEs0PM _ _ = False          

-- e)
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | (x == 0) && (y == 0) = True
              | otherwise = False

ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM _ _ = False              

-- f)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | (x <= 3) && (y <= 3) = True
                   | (x > 3) && (x <= 7) && (y > 3) && (y <= 7) = True
                   | (x > 7) && (y > 7) = True
                   | otherwise = False

-- g)
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x /= y) && (x /= z) && (y /= z) = x + y + z
                    | (x == y) && (x == z) && (y == z) = x
                    | x == y = x + z
                    | x == z = x + y
                    | y == z = x + y

-- h)
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | (x <= 0) || (y <= 0) = False
                 | (x `mod` y) == 0 = True
                 | otherwise = False

-- i)
digitoUnidades :: Int -> Int
digitoUnidades x | x < 0 = (-x) `mod` 10
                 | otherwise = x `mod` 10

-- j)
sacarUnidades :: Int -> Int
sacarUnidades x | x >= 0 = x `div` 10
                | otherwise = (-x) `div` 10

digitoDecenas :: Int -> Int
digitoDecenas x = digitoUnidades(sacarUnidades x)                 