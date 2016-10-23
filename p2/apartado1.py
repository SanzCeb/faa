import numpy as np 
from sklearn.naive_bayes import MultinomialNB
from datos import Datos
import EstrategiaParticionado

estrategia = EstrategiaParticionado.ValidacionCruzada(10)
clasificador_sklearn = MultinomialNB()

tic_tac_toe = Datos ("../ficheros/ConjuntosDatos/tic-tac-toe.data", True)
particiones = estrategia.creaParticiones(tic_tac_toe)

datos_train = tic_tac_toe.extraeDatosTrain(particiones[0])
datos_test = tic_tac_toe.extraeDatosTest(particiones[0])

clasificador_sklearn.fit(datos_train[:-1],
                         datos_train[-1])
print(clasificador_sklearn.predict(datos_test[:-1]))

