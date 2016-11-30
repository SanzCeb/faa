import numpy as np 
from Poblacion import Poblacion 
from Clasificador import Clasificador
from utils import crear_esquema
class ClasificadorPittsburgh (Clasificador):

    prob_cruce = 0.0
    prob_mutacion = 0.0
    tasa_elitismo = 0.0
    tam_poblacion = 0
    num_generaciones = 0
    individuo_apto = None
    poblacion = None
    datos_train = np.array([])
    diccionario = []
    atributosDiscretos = []
    def __init__(self,prob_cruce, prob_mutacion, tasa_elitismo,
                 tam_poblacion, num_generaciones):
        super(ClasificadorPittsburgh, self).__init__()
        self.prob_cruce = prob_cruce
        self.prob_mutacion = prob_mutacion
        self.tasa_elitismo = tasa_elitismo
        self.tam_poblacion = tam_poblacion
        self.num_generaciones = num_generaciones

    
    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):
        self.poblacion = Poblacion(self.tam_poblacion,
                                   crear_esquema(diccionario),
                                   self.prob_cruce,
                                   self.prob_mutacion,
                                   self.tasa_elitismo)
        for i in range(self.num_generaciones):
            self.poblacion.nueva_generacion(datosTrain)
            self.individuo_apto = self.poblacion.mejor_individuo()
            if (self.individuo_apto.fitness == 1):
                return
            
        pass

    def clasifica(self, datosTest, atributosDiscretos, diccionario):
        return map(lambda x : self.individuo_apto.clasifica(x),
                   datosTest[:,:-1]) 
