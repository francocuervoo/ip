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

factorial :: Integer -> Integer
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


-- Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == 0 = True
                | x < 0 = False
                | otherwise = esDivisible (x - y )  y


-- Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = (2 * n - 1) + sumaImpares (n - 1)


-- Ejercicio 5
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n - 2)


-- Ejercicio 6
todosLosDigitosIguales :: Integer -> Bool
todosLosDigitosIguales n | cantidadDigitos n == 1 = True
                         | cantidadDigitos n == 2  = digitoMasSignificativo n == sacarDigitoMasSignificativo n
                         | otherwise = todosLosDigitosIguales (sacarDigitoMasSignificativo n)


-- Ejercicio 7
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantidadDigitos n == i = digitoUnidades n
                 | otherwise = iesimoDigito ( sacarDigitoUnidades n) i


-- Ejercicio 8
sumaDigitos :: Integer -> Integer
sumaDigitos n | cantidadDigitos n == 1 = n
              | otherwise = digitoMasSignificativo n + sumaDigitos (sacarDigitoMasSignificativo (n))


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



--  Ejercicio 10
-- a)
f1 :: Integer -> Integer
f1 n | n == 0 = 1
     | otherwise = 2^n + f1 (n-1)

-- b) 
f2 :: Integer -> Float -> Float
f2 n q | n == 1 = q
       | otherwise = q^n + f2 (n-1) q

f3 :: Integer -> Float -> Float
f3 n q | n == 1 = q + q^2
       | otherwise = q^(2*n) + q^(2*n-1) + f3 (n-1) q


f4 :: Integer -> Float -> Float
f4 n q = f3 n q - f2 (n-1) q


-- Ejercicio 11
-- a)
eAprox :: Integer -> Float
eAprox n | n < 0 = 0
         | n == 0 = 1
         | otherwise = 1 / fromIntegral(factorial n) + eAprox (n-1)

-- b)
e :: Float
e = eAprox 10


-- Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = 1 + 1 / sucesionAn (n-1)

sucesionAn :: Integer -> Float
sucesionAn 1 = 2
sucesionAn n = 2 + 1 / sucesionAn (n-1) 


-- Ejercicio 13
f :: Integer -> Integer -> Integer
f 1 m = m
f n m =  sumatoriaN n m + f (n-1) m

sumatoriaN :: Integer -> Integer -> Integer
sumatoriaN n 1 = n
sumatoriaN n m = n^m + sumatoriaN n (m-1)


--  Ejercicio 14
{-
    sumaPotencias (q: Z, n: Z, m: Z) : Z {
        requiere: { q > 0 ^ n > 0 ^ m > 0 }
        aegura: { res = a la suma de todas las potencias de la forma q^(a+b) con 1 <= a <= n y 1 <= b <= m } 
        o también
        asegura: { res = Σ a = 1 / n Σ b = 1 / m q^(a+b) }   
    }
-}

sumaPotencias ::  Int -> Int -> Int -> Int
sumaPotencias q n 1 = sumaPotenciasN q n 1
sumaPotencias q n m = sumaPotenciasN q n m + sumaPotencias q n (m-1)

sumaPotenciasN :: Int -> Int -> Int -> Int
sumaPotenciasN q 1 m = q ^ (1 + m)
sumaPotenciasN q n m = q ^ (n + m) +  sumaPotenciasN q (n-1) m


-- Ejercicio 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumaRacionalesN 1 m 
sumaRacionales n m = sumaRacionalesN n m + sumaRacionales (n-1) m
 
sumaRacionalesN :: Integer -> Integer -> Float
sumaRacionalesN n 1 = fromIntegral n
sumaRacionalesN n m = fromIntegral n / fromIntegral m + sumaRacionalesN n (m-1)


-- Ejercicio 16
-- a)
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2


menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n i | mod n i == 0 = i
                      | otherwise = menorDivisorDesde n (i+1)

-- b)            
esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n = menorDivisor n == n

-- c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m | m == 1 = False
                | esDivisible n m || esDivisible m n = True
                | otherwise = sonCoprimos n (div m (menorDivisor m))

-- d)
nEsimoPrimo :: Integer -> Integer 
nEsimoPrimo n | n == 1 = 2
              | otherwise = nEsimoPirmoAux n 1 2

nEsimoPirmoAux :: Integer -> Integer -> Integer -> Integer -- 3 1 2
nEsimoPirmoAux n i k | n == i = k 
                     | otherwise = nEsimoPirmoAux n (i+1) (siguientePrimo k 2)

siguientePrimo :: Integer -> Integer -> Integer
siguientePrimo n m | esPrimo n && esPrimo m && m > n = m
                   | esPrimo n && esPrimo m = siguientePrimo n (m+1)
                   | otherwise = siguientePrimo n (m+1)


-- Ejercicio 17
esFibonacci :: Integer -> Bool
esFibonacci n | n < 0 = False
              | otherwise = n == esFibonacciAux n 0 
              
              
esFibonacciAux :: Integer -> Integer -> Integer 
esFibonacciAux n k | n == fibonacci k || fibonacci k > n = fibonacci k
                   | otherwise = esFibonacciAux n (k+1)


-- Ejercicio 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | todosLosDigitosSonImpares n = -1
                 | n < 10 = n
                 | esImpar(digitoMasSignificativo n) = mayorDigitoPar(sacarDigitoMasSignificativo n)
                 | esImpar (digitoUnidades n) = mayorDigitoPar(sacarDigitoUnidades n)
                 | digitoMasSignificativo n > digitoUnidades n = mayorDigitoPar(sacarDigitoUnidades n)
                 | otherwise = mayorDigitoPar(sacarDigitoMasSignificativo n)


esPar :: Integer -> Bool
esPar n = mod n 2 == 0

esImpar :: Integer -> Bool
esImpar n = mod n 2 /= 0

segundoDigito :: Integer -> Integer
segundoDigito n | n < 10 = 0
                | n < 100 = sacarDigitoMasSignificativo n
                | otherwise = segundoDigito ( sacarDigitoUnidades n)        

todosLosDigitosSonImpares:: Integer -> Bool
todosLosDigitosSonImpares n | n < 0 = False
                            | n < 10 && esPar n = False
                            | n < 10 && not (esPar n) = True
                            | esPar (digitoMasSignificativo n ) = False
                            | otherwise = todosLosDigitosSonImpares (sacarDigitoMasSignificativo n)


-- Ejercicio 19
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaDePrimerosMPrimos n 2

esSumaDePrimerosMPrimos :: Integer -> Integer -> Bool
esSumaDePrimerosMPrimos n m | n == 0 = True
                            | m > n = False
                            | otherwise = esSumaDePrimerosMPrimos (n - m) (siguientePrimo m 2)


-- Ejercicio 20 -- PENDIENETE
tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n m = n



-- Ejercicio 21
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r | m == 0 = pitagorasMFijo 0 n r
                | otherwise = pitagorasMFijo m n r + pitagoras (m-1) n r


pitagorasMFijo :: Integer -> Integer -> Integer -> Integer
pitagorasMFijo m n r | n < 0 = 0
                     | esMenorPitagoras m n r = 1 + pitagorasMFijo m (n-1) r 
                     | otherwise = pitagorasMFijo m (n-1) r

esMenorPitagoras :: Integer -> Integer -> Integer -> Bool
esMenorPitagoras p q r = p^2 + q^2 <= r^2

-- pitagoras 3 4 5 ⇝ 20
-- pitagoras 3 4 2 ⇝ 6

