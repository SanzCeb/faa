from utils import entero_aleatorio
from Regla import Regla
from functools import reduce

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

    def clasifica(self, dato):
        for regla in self.reglas:
            if regla.se_cumple(dato):
                return regla.conclusion
        return self.reglas[0].conclusion
    
    def obtener_fitness (self, datos_train):
        """Metodo que calcula el ajuste de un individuo a partir 
        de un numpy array con los datos codificados"""
        def __acierta(dato_train):
            return not (self.clasifica(dato_train[:-1]) - dato_train[-1]).any()
        self.fitness = sum(map(__acierta, datos_train)) / len(datos_train)
        return self.fitness
        
            

    def mutar(self):
        i = entero_aleatorio(0, len(self.reglas) - 1)
        self.reglas[i].mutar()
        
    def cruce(self, progenitor):
        """Cruzar cada regla de este individuo con una aleatoria 
        del otro progenitor"""
        reglas_1 = []
        reglas_2 = []
        progenitor_num_reglas = len(progenitor.reglas)

        for regla in self.reglas:
            i = entero_aleatorio(0, progenitor_num_reglas - 1)
            punto = entero_aleatorio(0, progenitor_num_reglas - 1)
            regla_1, regla_2 = regla.cruce(progenitor.reglas[i],punto)
            reglas_1.append(regla_1)
            reglas_2.append(regla_2)

            
        individuo_1 = Individuo(self.esquema, self.num_reglas, reglas_1)
        individuo_2 = Individuo(self.esquema, self.num_reglas, reglas_2)
        return individuo_1, individuo_2
    
    def __str__(self):
        return reduce(lambda x,y: str(x) + "\n" + str(y), self.reglas)
    

    
