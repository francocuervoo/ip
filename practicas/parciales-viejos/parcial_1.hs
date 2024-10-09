-- Ejercicio 1
generarStock :: [String] -> [(String, Int)]
generarStock [] = [("",0)]
generarStock [x] = [(x, 1)]
generarStock lista = (head lista, cantidadadProductoEnProductos (head lista) lista) : generarStock (eliminarProductoEnProductos (head lista) lista)


eliminarProductoEnProductos :: String -> [String] -> [String]
eliminarProductoEnProductos _ [] = []
eliminarProductoEnProductos producto [x] | producto == x = []
                                         | otherwise = [x]
eliminarProductoEnProductos producto productos | producto == head productos = eliminarProductoEnProductos producto (tail productos)
                                               | otherwise = head productos : eliminarProductoEnProductos producto (tail productos) 

cantidadadProductoEnProductos :: String -> [String]  -> Int
cantidadadProductoEnProductos producto [] = 0
cantidadadProductoEnProductos producto [x] | producto == x = 1
                              | otherwise = 0
cantidadadProductoEnProductos producto (x:xs) | producto == x = 1 + cantidadadProductoEnProductos producto xs
                                 | otherwise = cantidadadProductoEnProductos producto xs                              


-- Ejercicio 2
stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] producto = 0
stockDeProducto [(productoTupla, cantidad)] producto | producto == productoTupla = cantidad
                                                     | otherwise = 0
stockDeProducto productos producto = cantidadDeProductoEnStock producto productos

cantidadDeProductoEnStock :: String -> [(String, Int)] -> Int
cantidadDeProductoEnStock producto [(productoTupla, cantidad)] | producto == productoTupla = cantidad
                                                               | otherwise = 0
cantidadDeProductoEnStock producto ((productoTupla, cantidad):xs) | producto == productoTupla = cantidad
                                                                  | otherwise = cantidadDeProductoEnStock producto xs


-- Ejercicio 3
dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] [] = 0
dineroEnStock [(tuplaStockProducto, tuplaStockCantidad)] listaPrecios = fromIntegral tuplaStockCantidad * obtenerPrecioEnLista tuplaStockProducto listaPrecios
dineroEnStock ((tuplaStockProducto, tuplaStockCantidad):stockProductos) listaPrecios = fromIntegral tuplaStockCantidad * obtenerPrecioEnLista tuplaStockProducto listaPrecios + dineroEnStock stockProductos listaPrecios


obtenerPrecioEnLista :: String -> [(String, Float)] -> Float
obtenerPrecioEnLista _ [] = 0
obtenerPrecioEnLista producto [(productoTupla, precioTupla)] | producto == productoTupla = precioTupla
                                                             | otherwise = 0
obtenerPrecioEnLista producto ((productoTupla, precioTupla):lista) | producto == productoTupla = precioTupla
                                                                   | otherwise =  obtenerPrecioEnLista producto lista


-- Ejercicio 4
aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta [] [] = []
aplicarOferta [(tuplaStockProducto, tuplaStockCantidad)] listaPrecios | tuplaStockCantidad > 10 = (tuplaStockProducto, obtenerPrecioEnLista tuplaStockProducto listaPrecios  * 0.80) : elimiarProductoEnListaPrecios tuplaStockProducto listaPrecios
                                                                      | otherwise = listaPrecios 
aplicarOferta ((tuplaStockProducto, tuplaStockCantidad):xs) listaPrecios | tuplaStockCantidad > 10 = (tuplaStockProducto, obtenerPrecioEnLista tuplaStockProducto listaPrecios  * 0.80) : aplicarOferta xs (elimiarProductoEnListaPrecios tuplaStockProducto listaPrecios)
                                                                         | otherwise = (tuplaStockProducto, obtenerPrecioEnLista tuplaStockProducto listaPrecios) : aplicarOferta xs (elimiarProductoEnListaPrecios tuplaStockProducto listaPrecios)


elimiarProductoEnListaPrecios :: String -> [(String, Float)] -> [(String, Float)]
elimiarProductoEnListaPrecios producto [] = []
elimiarProductoEnListaPrecios producto ((productoLista, precioLista):xs) | producto == productoLista = elimiarProductoEnListaPrecios producto xs
                                                                         | otherwise = (productoLista, precioLista) : elimiarProductoEnListaPrecios producto xs


-- productos:
-- ["manzana", "pera", "banana", "carne", "pera", "manzana", "pera", "carne", "batata"]

-- stock cantidad:
-- [("manzana",2),("pera",3),("banana",1),("carne",2),("batata",1)]

-- lista precios:
-- [ ("manzana",1.5) , ("pera",2.0) , ("cerveza", 4.0) , ("banana",1.0) , ("carne",5.5) , ("batata",0.5) , ("agua", 3.0) ]

