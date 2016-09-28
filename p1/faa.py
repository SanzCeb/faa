from datos import Datos
from EstrategiaParticionado import ValidacionSimple

dataset = Datos('ConjuntosDatos/wine_proc.data',True)
print("Imprimiendo datos codificados")
print(dataset.datos)

validacion_simple_obj = ValidacionSimple(5,0.2) 

validacion_simple_obj.nombreEstrategia
validacion_simple_obj.numeroParticiones
particiones = validacion_simple_obj.creaParticiones(dataset)
for i in range(len(validacion_simple_obj.particiones)):
   print ("Particion ",i)
   print ("Test:")
   print (validacion_simple_obj.particiones[i].indicesTest)
   print ("Train:")
   print (validacion_simple_obj.particiones[i].indicesTrain)
   print ("\n")

