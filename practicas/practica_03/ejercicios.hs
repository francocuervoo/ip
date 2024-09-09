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
absoluto :: Int -> Int
absoluto n
  | n < 0 = n * (-1)
  | otherwise = n

-- b)
maximoAbsoluto :: Int -> Int -> Int
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


-- Ejercicio 3
estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b  | a == 0 || b == 0 = False
                       | (-a) `mod` b == 0 = True
                       | otherwise = False


-- Ejercicio 4

-- a) 
prodInt :: (Float , Float ) -> (Float, Float) -> Float
prodInt v w = fst v * fst w + snd v * snd w

-- b)
{-
  problema todoMenor ( t1: R x R, t2: R x R) : Bool {
    requiere: { True }
    asegura { res = True <-> la primera componente de t1 es menor que la primera componente de 52 y la segunda componente de t1 es menor que la segunda componente de t2 }
  }
-}

todoMenor :: (Float , Float) -> (Float, Float) -> Bool
todoMenor v w = fst v < fst w && snd v < snd w

-- c)
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos v w = sqrt((snd v - fst v)^2 + (snd w - fst w)^2)

-- d)
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x, y, z) = x + y + z

-- e)
multiploOCero :: Int -> Int -> Int
multiploOCero x n | n <= 0 || x `mod` n /= 0 = 0
                  | otherwise = x

sumarSoloMultiplos :: (Int , Int , Int) -> Int -> Int
sumarSoloMultiplos (x, y, z) n = multiploOCero x n + multiploOCero y n + multiploOCero z n

--f)
{-
  problema posPrimerPar (t1: Z x Z x Z) : Z {
    requiere: { True }
    asegura: { res = 4 <-> los número de la terna son todos impares }
    asegura: { res = 1 <-> si el primero número de la terna es par }
    asegura: { res = 2 <-> si el segundo número de la terna es par }
    asegura: { res = 3 <-> si el tercero número de la terna es par }
  }
-}
esPar :: Int -> Bool
esPar x = (x `mod` 2) == 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z) | esPar x = 1
                       | esPar y = 2
                       | esPar z = 3
                       | otherwise = 4

-- g)
crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

-- g)
invertir :: a -> b -> (b, a)
invertir x y = (y, x)

-- i)
type Punto2D = (Float, Float)
typeProdInt :: Punto2D -> Punto2D -> Float
typeProdInt v w = fst v * fst w + snd v * snd w

typeTodoMenor :: Punto2D -> Punto2D -> Bool
typeTodoMenor v w = fst v < fst w && snd v < snd w

typeDistanciaPuntos :: Punto2D -> Punto2D -> Float
typeDistanciaPuntos v w = sqrt((snd v - fst v)^2 + (snd w - fst w)^2)


-- Ejercicio 5
{-
  problema todosMenores (t : Z × Z × Z) : Bool {
    requiere: { True }
    asegura: { (res = true) <-> ((f5(t0) > g5(t0)) ∧(f5(t1) > g5(t1)) ∧(f5(t2) > g5(t2))) }
  }
  problema f5 (n: Z) : Z {
    requiere: {True}
    asegura: { (n<=7 -> res = n∧2) ∧ (n > 7 -> res = 2n−1) }
  }
  problema g5 (n: Z) : Z {
    requiere: { True }
    asegura: { Si n es un número par, entonces res = n/2, en caso contrario, res = 3n + 1 }
  }  
-}
f5 :: Int -> Int
f5 n | n <= 7 = n*n
     | otherwise = 2*n - 1

g5 :: Int -> Int
g5 n | esPar n = n `div` 2
     | otherwise = 3 * n + 1     

todosMenores :: (Int , Int , Int ) -> Bool
todosMenores (x, y, z) = (f5 x > g5 x) && (f5 y > g5 y) && (f5 z > g5 z)


-- Ejercicio 6
{-
  problema esBisiesto (año : Z) : Bool {
    requiere: { True }
    asegura : { res = false <-> año no es múltiplo de 4 o año es múltiplo de 100 pero no de 400 }
  }
-}

esBisiesto :: Int -> Bool
esBisiesto año = not(año `mod` 4 /= 0 || (año `mod` 100 == 0 && año `mod` 400 /= 0))



-- Ejercicio 7
{-
  probelma distanciaManhattan( p : R x R x R, q : R x R x R) : R {
    requiere: { True }
    asegura: { res = sumatoria de i = 0 a 2 del módulo de | pi - qi| }
  }
-}
absolutoFloat :: Float -> Float
absolutoFloat x
  | x < 0 = x * (-1)
  | otherwise = x

distanciaManhattan :: ( Float, Float , Float ) -> (Float , Float , Float ) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = absolutoFloat(x1 - y1) + absolutoFloat(x2 - y2) + absolutoFloat (x3 - y3)

type Coordenada3d = (Float, Float, Float)
floatDistanciaManhattan :: Coordenada3d -> Coordenada3d -> Float
floatDistanciaManhattan (x1, x2, x3) (y1, y2, y3) = absolutoFloat(x1 - y1) + absolutoFloat(x2 - y2) + absolutoFloat (x3 - y3)


-- Ejercicio 8
sumaUltimosDosDigitos :: Int -> Int 
sumaUltimosDosDigitos x =  absoluto x `mod` 10 + ( absoluto x `div` 10 ) `mod` 10

comparar :: (Int, Int) -> Int
comparar (a, b) | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
                | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
                | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0