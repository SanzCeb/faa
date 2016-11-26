from unittest import TestCase
from Individuo import Individuo
from utils import entero_aleatorio

import math 

class Poblacion:
    individuos = []
    vastagos = []
    poblacion = 0
    num_generaciones = 0.0
    num_reglas = 0
    esquema = []
    
    def __init__(self,poblacion, esquema):
        
        self.prob_cruce  = prob_cruce
        self.prob_mutacion = prob_mutacion
        self.prob_elitismo = prob_elitismo
        self.esquema = esquema 
        self.individuos = [ Individuo(esquema, entero_aleatorio(1,5))
                            for i in range(poblacion) ]
        

    def __ordenar_poblacion(self):
        poblacion = map(lambda x : (x,x.fitness()), individuos)
        return sorted(poblacion, key = lambda x : x[1])
    def __obtener_fitness_total( self, poblacion_ordenada):
        return sum(map(lambda x : x[1], poblacion_ordenada))
    def recombinacion (self,prob_cruce):
        num_cruces = math.floor(len(poblacion) * prob_cruce)
        poblacion_ordenada = self.__ordenar_poblacion()
        fitness_total = self.__obtener_fitness_total(poblacion_ordenada)

        def __escoger_individuo():
            for individuo in poblacion_ordenada:
                if numero_aleatorio(0, fitness_total) < individuo[1]:
                    return individuo

        for i in range(num_cruces):
            progenitor_1 = __escoger_individuo()
            progenitor_2 = __escoger_individuo()
            vastago_1, vastago_2 = progenitor_1[0].cruce(progenitor_2[0])
            vastago.append(vastago_1)
            vastago.append(vastago_2)
            
        
    def mutacion (self,prob_mutacion):
        for i in range(vastagos):
            if random.random() < prob_cruce:
                self.vastagos[i].mutar()
    def seleccion_natural(self):
        pass
