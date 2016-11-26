import numpy as np
from utils import entero_aleatorio
from Clausula import Clausula
from functools import reduce
import operator as op 

class Regla:
    clausulas = None
    conclusion = None
    def __init__(self,esquema=None):
        if esquema != None:
            self.clausulas = [ Clausula(longitud) for longitud in esquema[:-1]]
            self.conclusion = np.array(esquema[-1])
        else:
            self.clausulas = []
            conclusion = np.array([])
            
    def se_cumple (self, dato):
        """Conjuncion de clausulas, se espera una lista de numpy array"""
        clausulas_comp = map(lambda x, y : x.se_cumple(y),self.clausulas, dato)
        return reduce(op.and_, clausulas_comp)

    def cruce (self, regla, punto):
        """Implementacion del cruce en un punto """
        vastago_1 = Regla()
        vastago_2 = Regla()

        vastago_1.clausulas = self.clausulas[:punto] + regla.clausulas[punto:]
        vastago_2.clausulas = regla.clausulas[:punto] + self.clausulas[punto:]
        vastago_1.conclusion = regla.conclusion
        vastago_2.conclusion = self.conclusion
        return vastago_1,vastago_2

    def mutar ( self ):
        """Invertimos un bit aleatoria de una clausula elegida de forma 
        tambien aleatoria"""
        i = entero_aleatorio(0, len(self.clausulas) - 1)
        self.clausulas[i].mutar()

