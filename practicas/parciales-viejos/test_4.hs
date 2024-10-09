module SolucionTest where
import Parcial_4
import Test.HUnit

run = runTestTT tests 
tests = test [
    "formulasValidas" ~: testFormulasValidas
    ]

testFormulasValidas = test [
    "Formula valida" ~: formulasValidas [("Juan Pérez","Susana García"), ("María Montero","Pablo Moreno")] ~?= True,
    "Formula invalida" ~: formulasValidas [("Juan Pérez","Susana García"), (" Montero","")] ~?= False,
    "Formula invalida" ~: formulasValidas [("Juan Pérez",""), (" Montero","Pablo Moreno")] ~?= False,
    "Formula invalida" ~: formulasValidas [("",""), ("","")] ~?= False
    ]    