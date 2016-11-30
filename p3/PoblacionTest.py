from unittest import TestCase
from Individuo import Individuo
from Poblacion import Poblacion
import numpy as np 


TAM_POBLACION = 100
esquema = [2,2,1]
PROB_CRUCE = 0.6
PROB_MUTACION = 0.01
TASA_ELITISMO = 0.05
TAM_VASTAGOS = int(TAM_POBLACION * PROB_CRUCE * 2)

class PoblacionTest(TestCase):

    poblacion = None
    def setUp(self):
        self.poblacion = Poblacion(TAM_POBLACION,
                                   esquema,
                                   PROB_CRUCE,
                                   PROB_MUTACION,
                                   TASA_ELITISMO)


    def generar_poblacion_test(self):
        individuos = self.poblacion.generar_poblacion(TAM_POBLACION)
        num_individuos = 0
        for individuo in individuos:
            self.assertTrue(len(individuo.reglas) <= 5)
            num_individuos += 1
        self.assertEqual(num_individuos, TAM_POBLACION)

    def calcular_num_cruces_test(self):
        num_cruces = self.poblacion.calcular_num_cruces()
        self.assertEqual(num_cruces, int(TAM_POBLACION * PROB_CRUCE))

    def recombinacion_test(self):
        datos_train = np.empty((3,3), dtype=np.ndarray)
        datos_train[0] = np.array([np.array([1,0]), np.array([1,0]), np.array([1])])
        datos_train[1] = np.array([np.array([0,1]), np.array([0,1]), np.array([0])])
        datos_train[2] = np.array([np.array([1,0]), np.array([0,1]), np.array([1])])

        poblacion_ordenada = self.poblacion.ordenar_poblacion(datos_train)
        self.poblacion.recombinacion()
        num_cruces = self.poblacion.calcular_num_cruces()
        self.assertEqual(len(self.poblacion.vastagos), TAM_VASTAGOS)
        self.assertEqual(num_cruces, TAM_VASTAGOS // 2)

    def ordenar_poblacion_test(self):
        datos_train = np.empty((3,3), dtype=np.ndarray)
        datos_train[0] = np.array([np.array([1,0]), np.array([1,0]), np.array([1])])
        datos_train[1] = np.array([np.array([0,1]), np.array([0,1]), np.array([0])])
        datos_train[2] = np.array([np.array([1,0]), np.array([0,1]), np.array([1])])


        poblacion_ordenada = self.poblacion.ordenar_poblacion(datos_train)

        fitness_previo = poblacion_ordenada[0][1]
        for fitness in map(lambda x :  x[1], poblacion_ordenada[1:]):
            self.assertTrue(fitness_previo >= fitness)
            fitness_previo = fitness

