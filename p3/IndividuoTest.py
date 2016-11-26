from unittest import TestCase

from Regla import Regla
from Clausula import Clausula
from Individuo import Individuo

import numpy as np 
from copy import deepcopy

class IndividuoTest (TestCase):

    i_1 = None 

    def setUp(self):
        c_1 = Clausula( np.array([1,1]))
        c_2 = Clausula( np.array([1,0]))
        
        c_4 = Clausula( np.array([1,1]))
        c_5 = Clausula( np.array([1,1]))


        regla_1 = Regla()
        regla_2 = Regla()

        regla_1.clausulas.append(c_1)
        regla_1.clausulas.append(c_2)
        regla_1.conclusion = np.array([1])

        
        regla_2.clausulas.append(c_4)
        regla_2.clausulas.append(c_5)
        regla_2.conclusion = np.array([0])

        self.i_1 = Individuo( [2,2,1], 2, [regla_1, regla_2])
        pass

    def obtener_fitness_test (self):
        datos_train = np.empty((3,3), dtype=np.ndarray)

        datos_train[0] = np.array([np.array([1,0]), np.array([1,0]), np.array([1])])
        datos_train[1] = np.array([np.array([0,1]), np.array([0,1]), np.array([0])])
        datos_train[2] = np.array([np.array([1,0]), np.array([0,1]), np.array([1])])

        self.assertEqual(self.i_1.obtener_fitness(datos_train), 2/3)
        pass

    def mutar_test(self):
        pass

    def cruce_test(self):
        pass 
    
