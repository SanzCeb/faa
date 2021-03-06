import numpy as np

def leer_dato(fichero):
  """Lee una linea del fichero y divide la linea en tantos trozos como comas"""
  return fichero.readline().split('\n')[0].split(',')

def leer_metadatos(fichero):
  """Funcion que lee el fichero y devuelve el numero de datos, 
  la cabecera de los datos y el tipo de cada atributo"""
  return int(fichero.readline()),leer_dato(fichero),leer_dato(fichero)

def leer_datos(fichero,numDatos):
  """Funcion para leer los numDatos disponibles"""
  return [leer_dato(fichero) for x in range(numDatos)]

def leer_fichero(fichero):
  """Funcion para leer los ficheros .data"""
  numDatos, atributos, tipoAtributos = leer_metadatos(fichero)
  datos = leer_datos(fichero,numDatos)
  return atributos,tipoAtributos,datos

def es_nominal(tipo):
  return True if tipo == 'Nominal' else False

def encontrar_nominales(tipoAtributos):
  """Funcion para averiguar que atributos son nominales"""
  return list(map(es_nominal, tipoAtributos)) 

def crear_diccionario(seq):
  """Funcion que asigna un codigo a cada valor unico de seq 
  y devuelve un diccionario"""
  conjunto = list(set(seq))
  return dict(zip(conjunto,range(len(conjunto))))

def crear_diccionarios(datos):
  """Funcion que crea un diccionario por cada atributo 
  que posea el conjunto de datos"""
  datosTraspuestos = np.transpose(np.array(datos))
  return list(map(crear_diccionario, datosTraspuestos))

def codificar_atributo(diccionario, valores):
  """Funcion que transforma cada valor en su clave correspondiente en el 
  diccionario"""
  return [diccionario[i] for i in valores]


def codificar_datos(diccionarios, matriz_datos):
  """Funcion que codifica el conjunto de datos leidos del fichero"""
  return np.array(
    list(
      map (codificar_atributo,
           diccionarios,
           np.transpose (matriz_datos)))).transpose()
         

class Datos(object):
  
  supervisado=True
  TiposDeAtributos=('Continuo','Nominal')
  tipoAtributos=[]
  nombreAtributos=[]
  nominalAtributos=[]
  datos=np.array(())
  diccionarios=[]
 

  def __init__(self, nombreFichero,sup):
    self.supervisado = sup
    fichero = open(nombreFichero,'r')
    self.nombreAtributos, self.tipoAtributos, datos_raw = leer_fichero(fichero)
    self.nominalAtributos = encontrar_nominales(self.tipoAtributos)
    self.diccionarios = crear_diccionarios(datos_raw)
    self.datos = codificar_datos(self.diccionarios,datos_raw)
    fichero.close()
    
  # TODO: hacer en las proximas practicas
  def extraeDatosTrain(idx):
    pass
  
  def extraeDatosTest(idx):
    pass


dataset = Datos('ConjuntosDatos/tic-tac-toe.data',True)
print(dataset.datos)

