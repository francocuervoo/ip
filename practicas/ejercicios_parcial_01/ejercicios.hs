
type Producto = Char
type Cantidad = Int
type Valor = Float

type Productos = [Producto]
type Stock = [(Producto, Cantidad)]
type Precio = [(Producto, Valor)]

-- función elem te dice si un elemento pertence o no a una lista
-- función ++ concatena dos listas, o sea las une

generarStock :: Productos -> Stock
generarStock [] = []
generarStock (x:xs) = (x, cant) : generarStock (eliminarElemento x xs)
    where cant = 1 + cantidadApariciones x xs

eliminarElemento :: (Eq t) => t -> [t] -> [t]
eliminarElemento _ [] = []
eliminarElemento x (y:ys) | x == y = eliminarElemento x ys
                  | otherwise = y : eliminarElemento x ys

cantidadApariciones :: (Eq t) => t -> [t] -> Int
cantidadApariciones _ [] = 0
cantidadApariciones x (y:ys) | x == y = 1 + cantidadApariciones x ys
                             | otherwise = cantidadApariciones x ys                  

             