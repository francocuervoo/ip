esPar :: Int -> Bool
esPar n | n == 0 = True
        | n == 1 = False
        | otherwise = esPar(n-2)
        
esPar2 :: Int -> Bool
esPar2 n | n == 0 = True
        | otherwise = not(esPar2(n-1))