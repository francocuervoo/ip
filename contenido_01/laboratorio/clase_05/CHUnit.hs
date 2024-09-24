-- Primer letra del archivo en mayúscula siempre para CHUnit

module CHUnit where

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-1)
