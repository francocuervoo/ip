factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)


-- Ejercicio 2
-- Lo que pide es "truncar" un número: 1,27 -> 1 no es un redondeo.
parteEntera :: Float -> Integer
parteEntera n | 0 <= n && n < 1 = 0
              | otherwise = 1 + parteEntera (n - 1)

parteEnteraConNegativos :: Float -> Integer
parteEnteraConNegativos x | x >= 0 && x < 1 = 0
                          | x < 0 = parteEnteraConNegativos (x+1) - 1
                          | otherwise = 1 + parteEnteraConNegativos (x - 1)


-- Funciones auxiliares

sacarDigitoUnidades :: Integer -> Integer
sacarDigitoUnidades n | n < 0 = -sacarDigitoUnidades (-n)
                      | otherwise = div n 10

-- "Dígito más significativo" = primer dígito
digitoMasSignificativo :: Integer -> Integer
digitoMasSignificativo n | n < 0 = digitoMasSignificativo ( - n)
                         | n < 10 = n
                         | otherwise = digitoMasSignificativo ( sacarDigitoUnidades n)

-- Me quedo con el último dígito
digitoUnidades :: Integer -> Integer
digitoUnidades n | n < 0 = digitoUnidades (-n)
                 | n < 10 = n
                 | otherwise = mod n 10

cantidadDigitos :: Integer -> Integer
cantidadDigitos n | n < 10 = 1
                  | otherwise = 1 + cantidadDigitos ( sacarDigitoUnidades n)                 

sacarDigitoMasSignificativo :: Integer -> Integer
sacarDigitoMasSignificativo n | n < 0 = - sacarDigitoMasSignificativo (-n)
                              | otherwise = mod n (10 ^ ((cantidadDigitos n ) - 1))                  

sacarPrimeroYUltimo :: Integer -> Integer
sacarPrimeroYUltimo n = sacarDigitoUnidades (sacarDigitoMasSignificativo n)                               

-- Ejercicio 3


-- Ejercicio 4


-- Ejercicio 5


-- Ejercicio 6


-- Ejercicio 7
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantidadDigitos n == i = digitoUnidades n
                 | otherwise = iesimoDigito ( sacarDigitoUnidades n) i


-- Ejercicio 8


-- Ejercicio 9
{-
    problema esCapicua( n : Z) : Bool {
        requiere: { n >= 0 }
        asegura: { res = true <-> el número es capicúa }
    }
-}
esCapicua :: Integer -> Bool 
esCapicua n | n < 10 = True
            | digitoMasSignificativo n == digitoUnidades n = esCapicua (sacarPrimeroYUltimo n)
            | otherwise = False

-- Otra forma de implementarlo es utilizando la función auxiliar invertir
invertir :: Integer -> Integer
invertir n | n < 0 = - invertir (-n)
           | n < 10 = n
           | otherwise = (digitoUnidades n) * (10 ^ (cantidadDigitos n -1)) + invertir (sacarDigitoUnidades n)