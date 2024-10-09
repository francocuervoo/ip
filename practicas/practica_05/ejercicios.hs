-- Ejercicio 1

-- 1.
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- 2.
ultimo :: [t] -> t
ultimo list | longitud list == 1 = head list
            | otherwise = ultimo (tail list)
{-
    problema ultimo (s: seq⟨T⟩) : T {
        requiere: { |s|> 0 } -- indica que la cantidad de elementos de s tiene que ser mayor a 0
        asegura: { resultado = s[|s|−1] } -- el resultado es el elemento de s que está ubicado en la posición cantidad de elementos de s-1
    }
-}

-- 3.
principio :: [t] -> [t]
principio (x:xs) | longitud xs == 0 = []
                 | otherwise = x : principio xs
{-
    problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
        requiere: { |s| > 0 }
        asegura: { resultado = subseq(s, 0, |s|−1) } resultado = una subsecuencia de s que comienza en la posición 0 y termina en la posición |s|−1. Básicamente, el resultado de la función debe ser todos los elementos de la lista excepto el último.
    }
-}

-- 4.
reverso :: [t] -> [t]
reverso list | longitud list == 0 = []
             | otherwise = ultimo list : reverso ( principio list)


-- Ejercicio 2

-- 1.
pertenece :: (Eq t) => t -> [t] -> Bool
-- (Eq t) => es una restricción de tipo. Indica que el tipo t debe pertenecer a la clase de tipos Eq.
-- Los tipos que pertenecen a la clase Eq son aquellos para los cuales se pueden definir comparaciones de igualdad.
-- Ejemplos de tipos que implementan Eq son Int, Char, String, etc.
pertenece _ [] = False
pertenece t (x:xs) | t == x = True
                   | otherwise = pertenece t xs

-- problema pertenece (e: T , s: seq⟨T⟩) : B {
--     requiere: { True }
--     asegura: { resultado = true ↔ e ∈ s }
-- }

-- 2.
todosIguales :: (Eq t) => [t] -> Bool
todosIguales list | longitud list == 0 = False
                  | longitud list == 1 = True
todosIguales (x:xs) | not (pertenece x xs) = False
                    | otherwise = todosIguales xs

-- 3.
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos list | longitud list == 0 = False
                    | longitud list == 1 = True
                    | todosIguales list = False
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs

-- 4.
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos []  = False
hayRepetidos [x] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs

-- 5.
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar t (x:xs) | t == x = xs
                | otherwise = x : quitar t xs

-- 6.
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos t (x:xs) | t == x = quitarTodos t (quitar t xs)
                     | otherwise = x : quitarTodos t xs

-- 7.
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = x : eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x : eliminarRepetidos xs

-- 8.
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos [_] [] = False
mismosElementos [] [_] = False
mismosElementos (x:xs) (y:ys) | pertenece x (y:ys) = mismosElementos (quitarTodos x (x:xs)) (quitarTodos x (y:ys))
                              | otherwise = False

-- 9
capicua :: (Eq t) => [t] -> Bool
capicua list = list == reverso list


-- Ejercicio 3

-- 1.
sumatoria :: [Integer] -> Integer
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

-- 2.
productoria :: [Integer] -> Integer
productoria [x] = x
productoria (x:xs) = x * productoria xs

-- 3.
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x > head xs = maximo (quitarTodos (head xs) (x:xs))
              | x == head xs = maximo (quitar x (x:xs))
              | otherwise = maximo (quitarTodos x xs)

-- 4.
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = [n]
sumarN n [x] = [x + n]
sumarN n (x:xs) = (x + n) : sumarN n xs


-- 5.
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [n] = [n + n]
sumarElPrimero (x:xs) = (x + x) : sumarN x xs

-- 6.
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [n] = [n + n]
sumarElUltimo list = reverso (sumarElPrimero (reverso list))

-- 7.
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | esPar x = x : pares xs
             | otherwise = pares xs

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

-- 8.
multiplosN :: Integer -> [Integer] -> [Integer]
multiplosN n [] = []
multiplosN n (x:xs) | esXMultiploNDe x n = x : multiplosN n xs
                    | otherwise = multiplosN n xs

esXMultiploNDe :: Integer -> Integer -> Bool
esXMultiploNDe x n = mod x n == 0

-- 9.
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [n] = [n]
ordenar list = maximo list : ordenar (quitar (maximo list) list)


-- Ejercicio 4
-- palabra = secuencia de caracteres sin blanco

-- a.
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:xs) | x == ' ' && x == head xs = sacarBlancosRepetidos xs
                             | otherwise = x : sacarBlancosRepetidos xs

-- b.
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs)
  | x == ' '  = contarPalabras (sacarBlancos xs)  -- Ignorar espacios consecutivos
  | otherwise = 1 + contarPalabras (sacarPalabra xs)  -- Contar una palabra y saltar a la siguiente

sacarBlancos :: [Char] -> [Char]
sacarBlancos [] = []
sacarBlancos (x:xs)
  | x == ' '  = sacarBlancos xs  -- Si es un espacio, seguimos ignorando
  | otherwise = x:xs  -- Si encontramos un carácter que no es un espacio, devolvemos el resto de la lista

sacarPalabra :: [Char] -> [Char]
sacarPalabra [] = []
sacarPalabra (x:xs)
  | x == ' '  = xs  -- Cuando encontramos un espacio, devolvemos el resto de la lista
  | otherwise = sacarPalabra xs  -- Si no es un espacio, seguimos avanzando

 -- c.
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga x = comparoPalabras (palabras x) (head (palabras x))

comparoPalabras :: [[Char]] -> [Char] -> [Char]
comparoPalabras (x:xs) l | xs == [] = if longitudPalabra l > longitudPalabra x then l else x
                         | longitudPalabra x > longitudPalabra l = comparoPalabras xs x
                         | otherwise = comparoPalabras xs l

longitudPalabra :: [Char] -> Int
longitudPalabra [] = 0
longitudPalabra (x:xs) | x == ' ' = 0
                       | otherwise = 1 + longitudPalabra xs

-- d.
palabras :: [Char] -> [[Char]]
palabras x = palabrasAux x x

palabrasAux :: [Char] -> [Char] -> [[Char]]
palabrasAux [] l = [palabra l]
palabrasAux (x:xs) l | x == ' ' = palabra l : palabrasAux xs xs 
                     | otherwise = palabrasAux xs l

palabra :: [Char] ->  [Char]
palabra [] = []
palabra (x:xs) | x == ' ' = []
                | otherwise = x : palabra xs

-- e.
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

-- f.
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) | xs == [] = x
                         | otherwise = x ++ [' '] ++ aplanar xs
-- g.
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos (x:xs) n | xs == [] = x
                            | otherwise = x ++ generaNBlancos n ++ aplanarConNBlancos xs n 

generaNBlancos :: Integer -> [Char]
generaNBlancos 0 = []
generaNBlancos n = ' ' : generaNBlancos (n-1)  


-- Ejercicio 5

-- 1.
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [t] = [t]
sumaAcumulada (x:xs) = x : sumaAcumulada (x + head xs : tail xs)

-- 2.
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = descomponerEnFactoresPrimosDesde 2 x  : descomponerEnPrimos xs

descomponerEnFactoresPrimosDesde :: Integer -> Integer -> [Integer]
descomponerEnFactoresPrimosDesde 2 1 = []
descomponerEnFactoresPrimosDesde n x | esDivisible x n = n : descomponerEnFactoresPrimosDesde 2 (div x n)
                                     | otherwise = descomponerEnFactoresPrimosDesde (siguientePrimo n) x

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n i | mod n i == 0 = i
                      | otherwise = menorDivisorDesde n (i+1)

esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n                      

siguientePrimo :: Integer -> Integer
siguientePrimo n | esPrimo(n+1) = n+1
                 | otherwise = siguientePrimo (n+1)

esDivisible :: Integer -> Integer -> Bool
esDivisible n m = mod n m == 0                 


-- Ejercicio 6

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

elNombre :: Contacto -> Texto
elNombre (nombre, _) = nombre

elTelefono :: Contacto -> Telefono
elTelefono (_, telefono) = telefono

-- a.
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos nombre [] = False
enLosContactos nombre (x:xs) | nombre == elNombre x = True
                             | otherwise = enLosContactos nombre xs

-- b.
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (nombre, telefono) [] = [(nombre ,telefono)]
agregarContacto (nombre, telefono) list | elContactoExiste (nombre, telefono) list = (nombre, telefono) : eliminarContactoExistente (nombre, telefono) list
                                        | otherwise = (nombre, telefono) : list

elContactoExiste :: Contacto -> ContactosTel -> Bool
elContactoExiste (_,_) [] = False
elContactoExiste (nombre, telefono) [x] = nombre == elNombre x 
elContactoExiste (nombre, telefono) (x:xs) | nombre == elNombre x = True
                                           | otherwise = elContactoExiste (nombre, telefono) xs

eliminarContactoExistente :: Contacto -> ContactosTel -> ContactosTel
eliminarContactoExistente (_,_) [] = []
eliminarContactoExistente (nombre,telefono) [x] | nombre == elNombre x = []
                                                | otherwise = [x]
eliminarContactoExistente (nombre, telefono) (x:xs) | nombre == elNombre x = eliminarContactoExistente (nombre,telefono) xs
                                                    | otherwise = x : eliminarContactoExistente (nombre,telefono) xs


-- c.
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto nombre [] = []
eliminarContacto nombre [x] | nombre == elNombre x = []
                            | otherwise = [x]
eliminarContacto nombre (x:xs) | nombre == elNombre x = eliminarContacto nombre xs 
                               | otherwise = x : eliminarContacto nombre xs


-- Ejercicio 7                                                          

