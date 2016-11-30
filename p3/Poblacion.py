from unittest import TestCase
from Individuo import Individuo
from utils import entero_aleatorio

import math 

class Poblacion:
    individuos = None
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
        

    def generar_poblacion(self, tam_poblacion):
        return [ Individuo(self.esquema, entero_aleatorio(1,5))
                 for i in range(tam_poblacion)]
            

    def calcular_num_cruces(self):
        return math.floor(self.tam_poblacion * self.prob_cruce)

    def calcular_num_mutaciones(self):
        return round(len(self.vastagos) * self.prob_mutacion)

    def calcular_num_supervivientes(self):
        return round(self.tam_poblacion * self.prob_elitismo)

    def ordenar_poblacion(self, datos_train):
        """Este metodo realiza una ordenacion de los individuos
        en funcion del fitness para posteriormente realizar
        una seleccion proporcional al mismo"""
        poblacion = zip(self.individuos, map( lambda x : x.obtener_fitness(datos_train),
                                                                           self.individuos))
        poblacion_ordenada = sorted(poblacion,
                                    key = lambda x : x[1],
                                    reverse=True)
        self.individuos = [individuo[0] for individuo in  poblacion_ordenada]
        return poblacion_ordenada

    def __obtener_fitness_total( self, poblacion_ordenada):
        return sum(map(lambda x : x[1], poblacion_ordenada))
    def recombinacion (self,prob_cruce):
        num_cruces = math.floor(len(poblacion) * prob_cruce)
        poblacion_ordenada = self.__ordenar_poblacion()
        fitness_total = self.__obtener_fitness_total(poblacion_ordenada)

        def __escoger_individuo():
            extremo_inferior = 0
            valor = numero_aleatorio(0, fitness_total)
            for individuo in self.individuos:
                extremo_superior = extremo_inferior + individuo.fitness
                if valor <= extremo_superior:
                    return individuo
                extremo_inferior = extremo_superior

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
