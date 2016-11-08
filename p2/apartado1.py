import numpy as np 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from ClasificadorNaiveBayes import ClasificadorNaiveBayes
from ClasificadorNaiveBayesLaplace import ClasificadorNaiveBayesLaplace
from datos import Datos
from EstrategiaParticionado import ValidacionCruzada

clasificador_NB = ClasificadorNaiveBayes()
clasificador_laplace = ClasificadorNaiveBayesLaplace()
clasificador_sk = GaussianNB()

def clasificar(datos):
    X_train, X_test, y_train, y_test = train_test_split(datos.datos[:,:-1],
                                                        datos.datos[:,-1],
                                                        test_size = 0.2,
                                                        random_state = 42)
    clasificador_sk.fit(X_train,y_train)
    print( "Tasa de aciertos sklearn: ", clasificador_sk.score(X_test,y_test) )
    
    particionado = ValidacionCruzada(10)                       
    error = clasificador_NB.validacion(particionado, datos, clasificador_NB)
    print( "Tasa de aciertos Naive-Bayes: ", 1 - np.mean(error))
    
    particionado = ValidacionCruzada(10)                       
    error = clasificador_NB.validacion(particionado, datos, clasificador_NB)
    print( "Tasa de aciertos Laplace: ", 1 - np.mean(error))
    return error




tic_tac_toe = Datos ("../ficheros/ConjuntosDatos/tic-tac-toe.data", True)
wine = Datos("../ficheros/ConjuntosDatos/wine_proc.data",True)
crx = Datos("../ficheros/ConjuntosDatos/crx.data",True)
digits = Datos("../ficheros/ConjuntosDatos/digits.data",True)

clasificar(tic_tac_toe)
clasificar(wine)
clasificar(crx)
clasificar(digits)

