module SolucionTest where
import Parcial_3 
import Test.HUnit

run = runTestTT tests 
tests = test [
    "divisoresPropios" ~: testDivisoresPropios,
    "sonAmigos" ~: testSonAmigos,
    "losPrimerosNPerfectos"  ~: testLosPrimerosNPerfectos
    ]

testDivisoresPropios = test [
    "Divisores propios correctos" ~: divisoresPropios 1 ~?= [1],
    "Divisores propios correctos" ~: divisoresPropios 2 ~?= [1],
    "Divisores propios correctos" ~: divisoresPropios 6 ~?= [1,2,3],
    "Divisores propios correctos" ~: divisoresPropios 12 ~?= [1,2,3,4,6],
    "Divisores propios correctos" ~: divisoresPropios 28 ~?= [1,2,4,7,14]    
    ]

testSonAmigos = test [
    "Son amigos" ~: sonAmigos 220 284 ~?= True,
    "Son amigos" ~: sonAmigos 284 220 ~?= True,
    "Son amigos" ~: sonAmigos 1184 1210 ~?= True,
    "Son amigos" ~: sonAmigos 2 1210 ~?= False
    ]

testLosPrimerosNPerfectos = test [
    "LosPrimerosNPerfectos"  ~: losPrimerosNPerfectos 1 ~?= [6],        "LosPrimerosNPerfectos"  ~: losPrimerosNPerfectos 2 ~?= [6, 28],
    "LosPrimerosNPerfectos"  ~: losPrimerosNPerfectos 3 ~?= [6, 28, 496],
    "LosPrimerosNPerfectos"  ~: losPrimerosNPerfectos 4 ~?= [6, 28, 496, 8128]
    ]    