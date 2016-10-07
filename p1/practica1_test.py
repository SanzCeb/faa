from sys import argv
from datos import Datos

import EstrategiaParticionado
import numpy
from ClasificadorAPriori import ClasificadorAPriori
from ClasificadorNaiveBayes import ClasificadorNaiveBayes

nombre_script,nombre_fichero = argv

dataset = Datos ( nombre_fichero, True)
estrategia = EstrategiaParticionado.ValidacionCruzada(5)
clasificador = ClasificadorAPriori()
clasificador_bayes = ClasificadorNaiveBayes()
errores = clasificador.validacion(estrategia, dataset, clasificador)
errores_bayes  = clasificador_bayes.validacion(estrategia,dataset,clasificador_bayes)

print ("Error del clasificador a priori es: ", numpy.mean(errores))
print ("Error del clasificador Naive-Bayes: ", numpy.mean(errores_bayes))
