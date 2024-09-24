identidad :: t -> t
identidad x = x

primero :: tx -> ty -> tx
primero x y = x

segundo :: tx -> ty -> ty
segundo x y = y

constante5 :: tx -> ty -> tz -> Int
constante5 x y z = 5

mismoTipo :: t -> t -> Bool
mismoTipo x y = True

longitud :: [Int] -> Int
longitud [] = 0
longitud list = 1 + longitud (tail list)

sumatoria :: [Int]-> Int
sumatoria [] = 0
sumatoria list = head list + sumatoria(tail list)

pertenece :: Int-> [Int]-> Bool
pertenece n list | longitud list == 0 = False
                 | n == head list = True
                 | otherwise = pertenece n (tail list)


 