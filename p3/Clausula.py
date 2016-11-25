from unittest import TestCase
import numpy as np 
from utils import generar_bits, entero_aleatorio


class Clausula ():
    predicados = np.array([])

    def __init__(self,param):
         if isinstance(param,np.ndarray):
             self.predicados = param
         else:
             self.predicados = generar_bits(param)
        
    def se_cumple (self, clausula):
        """Disyuncion de predicados . Se espera un numpy array"""
        for (p,q) in zip(self.predicados, clausula):
            if (p == q):
                return True
        return False
    def mutar ( self ):
        i = entero_aleatorio(0,len(self.predicados) - 1)
        self.predicados[i] = int( not self.predicados[i] )

class ClausulaTests(TestCase):
    clausula_1 = None 
    clausula_2 = None 
    clausula_3 = None
    clausula_4 = None
    def setUp(self):
        self.clausula_1 = Clausula(np.array([0,1,0,0]))
        self.clausula_2 = Clausula(np.array([1,1,1,1]))
        self.clausula_3 = Clausula(np.array([0,0,0,0]))
        self.clausula_4 = Clausula(np.array([0,1,0,0]))
    def se_cumple_test ( self ):
        """Probando la or entre dos clausulas"""

        self.assertTrue(self.clausula_1.se_cumple( self.clausula_2.predicados))
        self.assertFalse(self.clausula_2.se_cumple( self.clausula_3.predicados))
        self.assertTrue(self.clausula_4.se_cumple( self.clausula_2.predicados))
        self.assertTrue(self.clausula_1.se_cumple( self.clausula_4.predicados))
        self.assertTrue(self.clausula_3.se_cumple( self.clausula_4.predicados))
    def mutar_test (self):
        """Este metodo comprueba que una regla y su mutacion 
        directa sea de un alelo"""
        clausula_copia = Clausula(self.clausula_1.predicados.copy())
        clausula_copia.mutar()
        comp_alelos = map(lambda x,y: int(x == int(not y)),
                          clausula_copia.predicados,
                          self.clausula_1.predicados)

        self.assertEqual(sum(comp_alelos),1)
        

