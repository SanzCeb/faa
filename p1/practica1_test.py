from sys import argv
from datos import Datos

import EstrategiaParticionado
import numpy
from ClasificadorAPriori import ClasificadorAPriori


nombre_script,nombre_fichero = argv

dataset = Datos ( nombre_fichero, True)
estrategia = EstrategiaParticionado.ValidacionSimple(1,0.3)
clasificador = ClasificadorAPriori()
errores = clasificador.validacion(estrategia, dataset, clasificador)

print ("Error del clasificador a priori es: ", numpy.mean(errores))
