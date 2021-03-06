from unittest import TestCase
from Regla import Regla
from Clausula import Clausula
from copy import deepcopy

import numpy as np 

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
        self.regla_1.conclusion = 1

        
        self.regla_2.clausulas.append(c_3)
        self.regla_2.clausulas.append(c_4)
        self.regla_2.conclusion = 0
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
