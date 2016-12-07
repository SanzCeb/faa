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
        for (p,q) in zip (self.predicados, clausula):
            if (p == q):
                return True
        return False 

    def mutar ( self ):
        i = entero_aleatorio(0,len(self.predicados) - 1)
        self.predicados[i] = int( not self.predicados[i] )

    def __repr__(self):
        return str(self.predicados)

    


