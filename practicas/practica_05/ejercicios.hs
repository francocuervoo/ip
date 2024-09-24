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
-- REVISAR
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos (x:xs) (y:ys) | pertenece x (y:ys) = mismosElementos (quitarTodos x (x:xs)) (y:ys)
                              | pertenece y (x:xs) = mismosElementos (quitarTodos y (y:ys)) (x:xs)
                              | otherwise = False 