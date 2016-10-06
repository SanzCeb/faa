from sys import argv
import Datos
import EstrategiaParticionado
import numpy
import ClasificadorAPriori

nombre_fichero = argv

dataset = Datos ( nombre_fichero, True)
estrategia = EstrategiaParticionado.ValidacionCruzada()
clasificador = Clasificador.ClasificadorAPriori()
errores = clasificador.validacion(estrategia, dataset, clasificador)

print ("Error del clasificador a priori es: ", numpy.mean(errores))
