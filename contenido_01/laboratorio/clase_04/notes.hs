-- Una manera de tipar un tipo propio
type Punto2D = (Float, Float)

todoMenorBis :: Punto2D -> Punto2D -> Bool
todoMenorBis (x1, y1) (x2, y2) = x1 < y1 && x2 < y2