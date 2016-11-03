import numpy as np 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from datos import Datos
import EstrategiaParticionado

def clasifica_sklearn(datos,clasificador):
    X_train, X_test, y_train, y_test = train_test_split(datos[:,:-1],
                                                        datos[:,-1],
                                                        test_size = 0.2,
                                                        random_state = 42)
    clasificador.fit(X_train,y_train)
    error = 1 - clasificador.score(X_test,y_test)
    print( "Tasa de error: ", error)
    return error



clasificadorNB = GaussianNB()
tic_tac_toe = Datos ("../ficheros/ConjuntosDatos/tic-tac-toe.data", True).datos
wine = Datos("../ficheros/ConjuntosDatos/wine_proc.data",True).datos
crx = Datos("../ficheros/ConjuntosDatos/crx.data",True).datos
digits = Datos("../ficheros/ConjuntosDatos/digits.data",True).datos

clasifica_sklearn(tic_tac_toe,clasificadorNB)
clasifica_sklearn(wine,clasificadorNB)
clasifica_sklearn(crx,clasificadorNB)
clasifica_sklearn(digits,clasificadorNB)

