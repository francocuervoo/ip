module SolucionTest where
import Parcial_2
import Test.HUnit

run = runTestTT tests 
tests = test [
    "maximo" ~: testMaximo
 
    ]

testMaximo = test [
        "El maximo es" ~: maximo [[13, 12, 6, 4] , [1, 1, 32, 25] , [9, 2, 14, 7] , [7, 3, 5, 16 ] , [27, 2, 8, 18]] ~?= 32,
        "El maximo es" ~: maximo [[13, 12, 6, 4]] ~?= 13,
        "El maximo es" ~: maximo [[13, 12, 6, 4] , [11111, 1, 32, 25] , [9, 2, 14, 7] , [7, 3, 5, 16 ] , [27, 2, 8, 18]] ~?= 11111        
    ]     