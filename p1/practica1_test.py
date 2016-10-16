from sys import argv
from datos import Datos
from ClasificadorAPriori import ClasificadorAPriori
from ClasificadorNaiveBayes import ClasificadorNaiveBayes
from ClasificadorNaiveBayesLaplace import ClasificadorNaiveBayesLaplace
import EstrategiaParticionado
import numpy

estrategia = EstrategiaParticionado.ValidacionCruzada(5)
clasificador = ClasificadorAPriori()
clasificador_bayes = ClasificadorNaiveBayes()
clasificador_laplace = ClasificadorNaiveBayesLaplace()

def clasificar (dataset):
    errores_bayes  = clasificador.validacion(estrategia,dataset,clasificador_bayes)
    errores_laplace = clasificador.validacion(estrategia,dataset,clasificador_laplace)
    print ("Error del clasificador Naive-Bayes es: ", numpy.mean(errores_bayes),numpy.std(errores_bayes))
    print ("Error del clasificador Naive-Bayes-Laplace es: ", numpy.mean(errores_laplace),numpy.std(errores_laplace))
    print ()

    

tic_tac_toe = Datos ("../ficheros/ConjuntosDatos/tic-tac-toe.data", True)
wine = Datos ( "../ficheros/ConjuntosDatos/wine_proc.data", True)
crx = Datos ( "../ficheros/ConjuntosDatos/crx.data", True)
digits = Datos ( "../ficheros/ConjuntosDatos/digits.data",True)

clasificar(tic_tac_toe)
clasificar(wine)
clasificar(crx)
clasificar(digits)
