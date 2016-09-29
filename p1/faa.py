from datos import Datos
import EstrategiaParticionado as ep


def print_particiones (validacion):
   print (validacion.nombreEstrategia)
   for i in range(len(validacion.particiones)):
      print ("Particion,i")
      print ("Test: ", len(validacion.particiones[i].indicesTest), " elementos")
      print (validacion.particiones[i].indicesTest)
      print ("Train: ", len(validacion.particiones[i].indicesTrain), " elementos")
      print (validacion.particiones[i].indicesTrain)
      print ("\n")


dataset = Datos('ConjuntosDatos/wine_proc.data',True)
print("Imprimiendo datos codificados")
print(dataset.datos)

validacion_simple_obj = ep.ValidacionSimple(5,0.2) 
validacion_cruzada_obj = ep.ValidacionCruzada(5) 

particiones_simple = validacion_simple_obj.creaParticiones(dataset)
particiones_cruzada = validacion_cruzada_obj.creaParticiones(dataset)

#print_particiones(validacion_simple_obj)
print_particiones(validacion_cruzada_obj)

   
