import numpy as np
from unittest import TestCase
from utils import entero_aleatorio
from Clausula import Clausula
from copy import deepcopy

class Regla:
    clausulas = [] #La clase es la ultima clausula

    def __init__(self,esquema=None):
        if esquema != None:
            self.clausulas = [ Clausula(longitud) for longitud in esquema]

    def se_cumple (self, dato):
        """Conjuncion de clausulas, se espera una lista de numpy array"""
        for (p, q) in zip(self.clausulas, dato):
            if not (p.se_cumple(q)):
                return False 
        return True
    def cruce (self, regla, punto):
        """Implementacion del cruce en un punto """
        vastago_1 = Regla()
        vastago_2 = Regla()

        vastago_1.clausulas = self.clausulas[:punto] + regla.clausulas[punto:]
        vastago_2.clausulas = regla.clausulas[:punto] + self.clausulas[punto:]
        return vastago_1,vastago_2
    def mutar ( self ):
        """Invertimos un bit aleatoria de una clausula elegida de forma 
        tambien aleatoria"""
        i = entero_aleatorio(0, len(self.clausulas) - 1)
        self.clausulas[i].mutar()

class ReglaTest (TestCase):
    regla_1 = None
    regla_2 = None
    c_1 = None
    c_2 = None
    def setUp(self):

        self.c_1 = Clausula( np.array([1,1]) )
        self.c_2 = Clausula( np.array([0,1]) )

        c_3 = Clausula( np.array([0,0]))
        c_4 = Clausula( np.array([1,1]))
        
        self.regla_1 = Regla()
        self.regla_2 = Regla()
        
        self.regla_1.clausulas.append(self.c_1)
        self.regla_1.clausulas.append(self.c_2)


        
        self.regla_2.clausulas.append(c_3)
        self.regla_2.clausulas.append(c_4)
        self.regla_2.conclusion = np.array([1,0])
    def se_cumple_test(self):

        self.assertTrue(self.regla_1.se_cumple([np.array([1,0]), np.array([1,1])]))
        self.assertFalse(self.regla_1.se_cumple([np.array([1,0]), np.array([1,0])]))
        self.assertFalse(self.regla_1.se_cumple([np.array([0,0]), np.array([0,1])]))
        pass

    def cruce_test(self):
        vastago_1, vastago_2 = self.regla_1.cruce(self.regla_2,1)

        self.assertEqual(vastago_1.clausulas[0], self.regla_1.clausulas[0])
        self.assertEqual(vastago_2.clausulas[0], self.regla_2.clausulas[0])
        self.assertEqual(vastago_1.clausulas[1], self.regla_2.clausulas[1])
        self.assertEqual(vastago_2.clausulas[1], self.regla_1.clausulas[1])
        
    def mutar_test(self):
        """El test comprueba que la diferencia entre una regla mutada 
        y la regla original es de una sola clausula"""
        def __comparador (c_1, c_2):
            return int ( (c_1.predicados - c_2.predicados).any())

        regla_3 = Regla()
        regla_3.clausulas = deepcopy(self.regla_2.clausulas)
        regla_3.mutar()

        comp_clausulas = map(__comparador,
                             regla_3.clausulas,
                             self.regla_2.clausulas)
        self.assertEqual( sum(comp_clausulas), 1)
