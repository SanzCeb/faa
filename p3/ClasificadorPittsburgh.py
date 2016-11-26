from Clasificador import Clasificador
from unittest import TestCase
import random
import numpy as np 
from datetime import datetime
from utils import entero_aleatorio, num_aleatorio,crear_esquema

 

def crear_esquema(diccionarios):
    """metodo que devuelve la longitud de cada alelo del cromosoma
    a partir de la lista de diccionarios"""
    esquema = []
    for dicc in diccionarios:
        num_alelos = len(dicc.keys())
        if num_alelos:
            esquema.append(num_alelos)
    return esquema

def cruce (progenitor_1, progenitor_2):
    """Metodo que realiza un cruce uniforme y devuelve dos vastagos. 
    Los progenitores deben tener exactamente la misma estructura. En caso 
    contrario, se devolvera None"""
    vastago_1 = []
    vastago_2 = []
    num_alelos = len(progenitor_1)

    if num_alelos != len(progenitor_2):
        return None
    for i in range(num_alelos):
        if i % 2:
            vastago_1.append(progenitor_1[i])
            vastago_2.append(progenitor_2[i])
        else:
            vastago_1.append(progenitor_2[i])
            vastago_2.append(progenitor_1[i])

    return vastago_1,vastago_2

def crear_regla(esquema):
    """Iniciamos una regla a partir de un esquema dado
    con ceros o unos elegidos de forma aleatoria"""
    num_conjunciones = len(esquema)

    for i in range(num_conjunciones):
        regla[i] = generar_bits(esquema[i])
    return regla






class Regla:
    clausulas = []
    conclusion = np.array([])

    def __init__(self,esquema=None):
        if esquema != None:
            self.clausulas = [ Clausula(longitud) for longitud in esquema[:-1] ]
            self.conclusion = esquema[-1]

    def se_cumple (self, dato):
        """Conjuncion de clausulas, se espera una lista de numpy array"""
        for (p, q) in zip(self.clausulas, dato):
            if not (p.se_cumple(q)):
                return False 
        return True
    def cruce (self, regla, punto):
        """Implementacion del cruce por en un punto. Se basa en la idea de que
        elegir una clausula es equivalente a establecer dos puntos de cruce"""
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
        clausulas[i].mutar()
        
class Individuo:
    reglas = []
    esquema = []
    num_reglas = 0
    def __init__(self,esquema, num_reglas, reglas = None):
        self.esquema = esquema
        self.num_reglas = num_reglas
        if reglas == None:
            self.reglas = [ Regla(esquema) for i in range(num_reglas) ]
        else:
            self.reglas = reglas 
        
    
    def fitness (self, datos_train):
        pass
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
    

class ClasificadorPittsburgh (Clasificador):

    prob_cruce = 0.0
    prob_mutacion = 0.0
    prob_elitismo = 0.0
    poblacion = 0
    num_generaciones = 0
    esquema = []
    individuo_apto = []
    datos_train = np.array([])
    diccionario = []
    atributosDiscretos = []
    def __init__(prob_cruce, prob_mutacion, prob_elitismo,
                 poblacion, num_generaciones):
        super(ClasificadorPittsburgh, self).__init__()
        self.prob_cruce = prob_cruce
        self.prob_mutacion = prob_mutacion
        self.prob_elitismo = prob_elitismo
        self.poblacion = poblacion
        self.num_generaciones = num_generaciones

    
    def __fitness(self, individuo):
        """Nuestra funcion de fitness devuelve el porcentaje de acierto
        sobre los datos de entrenamiento del individuo propuesto"""
        prediccion = self.clasifica (self.datos_train,
                                     self.atributosDiscretos,
                                     self.diccionario,
                                     individuo)
        return 1 - self.__error(self.datos_train[:,-1], prediccion)

    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):
        self.esquema = crear_esquema(diccionario)
        pass

#    def clasifica(self, datosTest, atributosDiscretos, diccionario, individuo=self.individuo_apto):
 #       pass



class Tests (TestCase):
#    def setUp(self):
 #       self.clf = ClasificadorPittsburgh(0.6, 0.001, 0.05, 10, 100)

    def crear_esquema_test(self):
        diccionarios = [{'a':0,'b':3,'c':1},{'z':2, 'w':5, 'r': 10,'o':8}, {'x': 0, 'y': '1'}]
        self.assertEqual(crear_esquema(diccionarios), [3,4,2])
        diccionarios = [{}]
        self.assertEqual(crear_esquema(diccionarios), [])
        diccionarios = [{'hola':1, 'adios':0},{'haciendo':2,'un test': 2}]
        self.assertEqual(crear_esquema(diccionarios), [2,2])

    def se_cumple_regla_test (self ):
        codigo_regla = [np.array([1,1]),np.array([0,1]),np.zeros((1,1))]
        codigo_regla_2 = [np.array([1,0]),np.array([0,1])] 
        codigo_regla_3 = [np.array([0,0]),np.array([0,1])]
        codigo_regla_4 = [np.array([0,1]),np.array([1,0])]
        
        regla = Regla(codigo_regla)

        self.assertTrue(regla.se_cumple(codigo_regla[:-1]))
        self.assertTrue(regla.se_cumple(codigo_regla_2))
        self.assertFalse(regla.se_cumple(codigo_regla_3))
        self.assertFalse(regla.se_cumple(codigo_regla_4))


