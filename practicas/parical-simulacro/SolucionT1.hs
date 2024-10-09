module SolucionT1 where
  
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = False
relacionesValidas relaciones = not (hayTuplasRepetidas relaciones) && not (hayTuplasConComponentesIguales relaciones)


personas :: [(String, String)] -> [String]
personas [] = []
personas ((primeraComponente, segundaComponente):xs) | estaIncluidaPrimeraTupla (primeraComponente, segundaComponente) xs && estaIncluidaSegundaTupla (primeraComponente, segundaComponente) xs = personas xs
                                                     | estaIncluidaPrimeraTupla (primeraComponente, segundaComponente) xs = [segundaComponente] ++ personas xs
                                                     | estaIncluidaSegundaTupla (primeraComponente, segundaComponente) xs = [primeraComponente] ++ personas xs
                                                     | otherwise = [primeraComponente, segundaComponente] ++ personas xs


amigosDe :: String -> [(String, String)] -> [String]
amigosDe nombre relaciones = quitarNombre nombre (personas (tuplaDeAmigos nombre relaciones))

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [(primeraComponente,segundaComponente)] = primeraComponente




-- Funciones auxiliares
cantidadDeAmigosDe :: String -> [(String, String)] -> Integer
cantidadDeAmigosDe nombre [] = 0
cantidadDeAmigosDe nombre relaciones = cantidadDeAmigos(amigosDe nombre relaciones)


cantidadDeAmigos :: [String] -> Integer
cantidadDeAmigos [] = 0
cantidadDeAmigos (x:xs) = 1 + cantidadDeAmigos xs


tuplaDeAmigos :: String -> [(String, String)] -> [(String, String)]
tuplaDeAmigos nombre [(primeraComponente, segundaComponente)] | nombre == primeraComponente || nombre == segundaComponente = [(primeraComponente, segundaComponente)]
                                                              | otherwise = []
tuplaDeAmigos nombre ((primeraComponente, segundaComponente):xs) | nombre == primeraComponente = (primeraComponente, segundaComponente) : tuplaDeAmigos nombre xs
                                                                 | nombre == segundaComponente = (primeraComponente, segundaComponente) : tuplaDeAmigos nombre xs
                                                                 | otherwise = tuplaDeAmigos nombre xs

quitarNombre :: String -> [String] -> [String]
quitarNombre nombre [] = []
quitarNombre nombre (x:xs) | nombre == x = quitarNombre nombre xs
                           | otherwise = x : quitarNombre nombre xs



estaIncluidaPrimeraTupla :: (String, String) -> [(String, String)] -> Bool
estaIncluidaPrimeraTupla (_,_) [] = False
estaIncluidaPrimeraTupla (primeraComponente, segundaComponente) relaciones | primeraComponente == primeraComponenteTupla (head relaciones) || primeraComponente == segundaComponenteTupla (head relaciones) = True
                                                                         | otherwise = estaIncluidaPrimeraTupla (primeraComponente, segundaComponente) (tail relaciones)

estaIncluidaSegundaTupla :: (String, String) -> [(String, String)] -> Bool
estaIncluidaSegundaTupla (_,_) [] = False
estaIncluidaSegundaTupla (primeraComponente, segundaComponente) relaciones | segundaComponente == primeraComponenteTupla (head relaciones) || segundaComponente == segundaComponenteTupla (head relaciones) = True
                                                                         | otherwise = estaIncluidaSegundaTupla (primeraComponente, segundaComponente) (tail relaciones)


hayTuplasRepetidas :: [(String, String)] -> Bool
hayTuplasRepetidas [] = False
hayTuplasRepetidas [(_,_)] = False
hayTuplasRepetidas ((primeraComponente, segundaComponente):xs) | primeraComponente == primeraComponenteTupla (head xs) && segundaComponente == segundaComponenteTupla (head xs) = True
                                                               | primeraComponente == segundaComponenteTupla (head xs) && segundaComponente == primeraComponenteTupla (head xs) = True
                                                               | otherwise = hayTuplasRepetidas xs

hayTuplasConComponentesIguales :: [(String, String)] -> Bool
hayTuplasConComponentesIguales [] = False
hayTuplasConComponentesIguales [(primeraComponente, segundaComponente)] = primeraComponente == segundaComponente
hayTuplasConComponentesIguales ((primeraComponente, segundaComponente): xs) | primeraComponente == primeraComponenteTupla (head xs) &&  segundaComponente == segundaComponenteTupla (head xs) = True
                                                                            | otherwise = hayTuplasConComponentesIguales xs

primeraComponenteTupla :: (String, String) -> String
primeraComponenteTupla (primeraComponenteTupla, segundaComponenteTupla) = primeraComponenteTupla

segundaComponenteTupla :: (String, String) -> String
segundaComponenteTupla (primeraComponenteTupla, segundaComponenteTupla) = segundaComponenteTupla

 

                                                    






-- [("Ana", "Juan"), ("Jorge", "Raul")]
-- [("Ana", "Juan"), ("Juan", "Cristina")]

