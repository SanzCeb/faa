from sys import argv
from datos import Datos
from ClasificadorAPriori import ClasificadorAPriori
from ClasificadorNaiveBayes import ClasificadorNaiveBayes
from ClasificadorNaiveBayesLaplace import ClasificadorNaiveBayesLaplace
import EstrategiaParticionado
import numpy


nombre_script,nombre_fichero = argv


dataset = Datos ( nombre_fichero, True)
estrategia = EstrategiaParticionado.ValidacionCruzada(5)
clasificador = ClasificadorAPriori()
clasificador_bayes = ClasificadorNaiveBayes()
clasificador_laplace = ClasificadorNaiveBayesLaplace()




errores = clasificador.validacion(estrategia, dataset, clasificador)
errores_bayes  = clasificador.validacion(estrategia,dataset,clasificador_bayes)
errores_laplace = clasificador.validacion(estrategia,dataset,clasificador_laplace)


print ("Error del clasificador a priori es: ", numpy.mean(errores))
print ("Error del clasificador Naive-Bayes es: ", numpy.mean(errores_bayes))
print ("Error del clasificador Naive-Bayes-Laplace es: ", numpy.mean(errores_laplace))

