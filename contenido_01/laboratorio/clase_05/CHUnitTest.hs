import Test.HUnit -- import HUnit
import CHUnit -- importo el archivo

run = runTestTT tests

tests = test [
    "Caso base 1" ~: ( fib 0 ) ~?= 0,
    "Caso base 2" ~: ( fib 1) ~?= 1,
    "Caso recursivo" ~: (fib 2) ~?= 1]