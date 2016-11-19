from Clasificador import Clasificador
from unittest import TestCase
import random
from datetime import datetime

def crear_esquema(diccionarios):
    """metodo que devuelve la longitud de cada alelo del cromosoma
    a partir de la lista de diccionarios"""
    esquema = []
    for dicc in diccionarios:
        num_alelos = len(dicc.keys())
        if num_alelos:
            esquema.append(num_alelos)
    return esquema

def mutar(individuo):
    """Metodo que modifica un alelo aleatorio del cromosoma"""
    individuo_mutado = individuo.copy()    
    random.seed(datetime.now())
    alelo = random.randint(0,len(individuo) - 1)
    individuo_mutado[alelo] = 0 if individuo[alelo] else 1
    return individuo_mutado


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

    def clasifica(self, datosTest, atributosDiscretos, diccionario, individuo=self.individuo_apto):
        pass



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
        
    def mutar_test( self ):
        """Este metodo comprueba que la diferencia entre un individuo y su mutacion 
        directa sea de un alelo"""
        individuo = [0,1,1,0]
        comp_alelos = map(lambda x,y: int(x != y), individuo, mutar(individuo))
        self.assertEqual(sum(comp_alelos),1)

    def cruce_test ( self ):
        """Probando el cruce uniforme con dos individuos de los cuales se espera 
        dos vastagos concretos"""
        progenitor_1 = [1,1,0,1,1]
        progenitor_2 = [0,1,1,0,1]
        vastago_1 = [1,1,0,0,1]
        vastago_2 = [0,1,1,1,1]

        resultado_1,resultado_2 = cruce(progenitor_1,progenitor_2)
        self.assertEqual(vastago_1,resultado_2)
        self.assertEqual(vastago_2,resultado_1)

    
