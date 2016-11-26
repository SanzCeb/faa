from utils import entero_aleatorio
from Regla import Regla

import random
import numpy as np


class Individuo:
    reglas = []
    esquema = []
    num_reglas = 0
    fitness = 0.0
    def __init__(self,esquema, num_reglas, reglas = None):
        self.esquema = esquema
        self.num_reglas = num_reglas
        if reglas == None:
            self.reglas = [ Regla(esquema) for i in range(num_reglas) ]
        else:
            self.reglas = reglas 
        
    
    def obtener_fitness (self, datos_train):
        """Metodo que calcula el ajuste de un individuo a partir 
        de un numpy array con los datos codificados"""
        def __acierta(dato_train):
            for regla in self.reglas:
                if regla.se_cumple(dato_train[:-1]):
                    return not (regla.conclusion - dato_train[-1]).any()
            return False
        self.fitness = sum(map(__acierta, datos_train)) / len(datos_train)
        return self.fitness
        
            

    def mutar(self):
        i = entero_aleatorio(0, len(self.reglas) - 1)
        reglas[i].mutar()
        
    def cruce(self, progenitor):
        """Cruzar cada regla de este individuo con una aleatoria 
        del otro progenitor"""
        reglas_1 = []
        reglas_2 = []
        progenitor_num_reglas = len(progenitor.reglas)

        for regla in reglas:
            i = entero_aleatorio(0, progenitor_num_reglas - 1)
            regla_1, regla_2 = regla.cruce(progenitor.reglas[i])
            reglas_1.append(regla_1)
            reglas_2.append(regla_2)

            
        individuo_1 = Individuo(self.esquema, self.num_reglas, reglas_1)
        individuo_2 = Individuo(self.esquema, self.num_reglas, reglas_2)
        return individuo_1, individuo_2
    

    

    
