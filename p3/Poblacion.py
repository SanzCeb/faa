from unittest import TestCase
from Individuo import Individuo
from utils import entero_aleatorio, numero_aleatorio

import math 

class Poblacion:
    individuos = []
    vastagos = []
    tam_poblacion = 0
    num_generaciones = 0.0
    num_reglas = 0
    esquema = []
    prob_mutacion = 0.0
    tasa_elitismo = 0.0
    prob_cruce = 0.0 

    
    def __init__(self, tam_poblacion,esquema,
                 prob_cruce, prob_mutacion, tasa_elitismo):

        self.tam_poblacion = tam_poblacion 
        self.prob_cruce  = prob_cruce
        self.prob_mutacion = prob_mutacion
        self.tasa_elitismo = tasa_elitismo
        self.esquema = esquema 
        self.individuos = self.generar_poblacion(tam_poblacion)

    def generar_poblacion(self, tam_poblacion):
        return [ Individuo(self.esquema, entero_aleatorio(1,5))
                 for i in range(tam_poblacion)]
            

    def calcular_num_cruces(self):
        return math.floor(self.tam_poblacion * self.prob_cruce)

    def calcular_num_mutaciones(self):
        return round(len(self.vastagos) * self.prob_mutacion)

    def calcular_num_supervivientes(self):
        return round(self.tam_poblacion * self.tasa_elitismo)

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
        return sum(map(lambda x : x.fitness, poblacion_ordenada))

    def recombinacion (self):
        """Metodo que implementa el cruce entre individuos utilizando
        una seleccion proporcional al fitness si la poblacion se encuentra
        ordenada """
        num_cruces = self.calcular_num_cruces()
        fitness_total = self.__obtener_fitness_total(self.individuos)

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
            vastago_1, vastago_2 = progenitor_1.cruce(progenitor_2)
            self.vastagos.append(vastago_1)
            self.vastagos.append(vastago_2)
            
    def mutacion (self):
        """Metodo que provoca la mutacion entre los vastagos"""
        num_mutaciones = self.calcular_num_mutaciones()
        for i in range(num_mutaciones):
            num = entero_aleatorio(0, len(self.vastagos) - 1)
            self.vastagos[num].mutar()

    def seleccion_natural(self):
        """Funcion que genera una nueva poblacion escogiendo a los mejores 
        de la actual y a los vastagos de la nueva"""
        num_supervivientes = self.calcular_num_supervivientes()
        num_nuevos_individuos = self.tam_poblacion - num_supervivientes
        elite = self.individuos[:num_supervivientes]
        self.individuos =  elite + self.vastagos

    def mejor_individuo(self):
        """Devuelve el mejor individuo suponiendo que la lista de individuos
        esta ordenada en funcion del fitness"""
        return self.individuos[0]

    def nueva_generacion(self, datos_train):
        self.ordenar_poblacion(datos_train)
        self.recombinacion()
        self.mutacion()
        self.seleccion_natural()
