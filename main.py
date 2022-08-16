# Al presente simulador le faltan funciones por implementar

acc = None #acumulador
uc = None #unit control
alu = None
pc = 0
mar = None
icr = None
mdr = None
memoria = [None]



#Función que almacena un valor en una dirección
def setFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria
  
  mar = int(instrucciones[0].replace("D",""))
  valor = int(instrucciones[1])
  mdr = int(valor)
  memoria[mar] = mdr

#Función que carga un valor que se encuentra en una dirección y lo almacena en el acc
def ldrFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria
  
  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  mar = posicionMemoria1
  print("MAR: ", mar, "\n")
  mdr = memoria[mar]
  print("MDRRRRR: ", mdr, "\n")
  acc = mdr
  
#Función que realiza una suma según la cantidad de direcciones que reciba.
def addFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  print("MDR SUMA: ", mdr, "\n")
  print("MAR SUMA: ", mar, "\n")
  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = instrucciones[1]
  posicionMemoria3 = instrucciones[2]
  if posicionMemoria2 == "NULL" and posicionMemoria3 == "NULL":
    mar = posicionMemoria1
    mdr = memoria[mar]
    alu = acc
    acc = mdr
    alu = alu + acc
    acc = alu
  elif posicionMemoria2 != "NULL" and posicionMemoria3 == "NULL":
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu + acc
    acc = alu
  else:
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu + acc
    acc = alu
    mar = int(posicionMemoria3.replace("D",""))
    mdr = acc
    memoria[mar] = mdr

#Función que realiza una resta según la cantidad de direcciones que reciba.
def subFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  print("MDR RESTA: ", mdr, "\n")
  print("MAR RESTA: ", mar, "\n")
  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = instrucciones[1]
  posicionMemoria3 = instrucciones[2]
  if posicionMemoria2 == "NULL" and posicionMemoria3 == "NULL":
    mar = posicionMemoria1
    mdr = memoria[mar]
    alu = acc
    acc = mdr
    alu = alu - acc
    acc = alu
  elif posicionMemoria2 != "NULL" and posicionMemoria3 == "NULL":
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu - acc
    acc = alu
  else:
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu - acc
    acc = alu
    mar = int(posicionMemoria3.replace("D",""))
    mdr = acc
    memoria[mar] = mdr

#Función que realiza una multiplicación según la cantidad de direcciones que reciba.
def mulFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  print("MDR MUL: ", mdr, "\n")
  print("MAR MUL: ", mar, "\n")
  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = instrucciones[1]
  posicionMemoria3 = instrucciones[2]
  if posicionMemoria2 == "NULL" and posicionMemoria3 == "NULL":
    mar = posicionMemoria1
    mdr = memoria[mar]
    alu = acc
    acc = mdr
    alu = alu * acc
    acc = alu
  elif posicionMemoria2 != "NULL" and posicionMemoria3 == "NULL":
    print("POSICIONMEMORIA1: ", posicionMemoria1)
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu * acc
    acc = alu
  else:
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu * acc
    acc = alu
    mar = int(posicionMemoria3.replace("D",""))
    print("PRINT MUL 3 PARAMS: ", mar, "\n" + "Tamaño: ", len(memoria))
    mdr = acc
    memoria[mar] = mdr

#Función que realiza una división según la cantidad de direcciones que reciba.
def divFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  print("MDR DIV: ", mdr, "\n")
  print("MAR DIV: ", mar, "\n")
  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = instrucciones[1]
  posicionMemoria3 = instrucciones[2]
  if posicionMemoria2 == "NULL" and posicionMemoria3 == "NULL":
    mar = posicionMemoria1
    mdr = memoria[mar]
    alu = acc
    acc = mdr
    alu = alu / acc
    acc = alu
  elif posicionMemoria2 != "NULL" and posicionMemoria3 == "NULL":
    print("POSICIONMEMORIA1: ", posicionMemoria1)
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu / acc
    acc = alu
  else:
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    alu = alu / acc
    acc = alu
    mar = int(posicionMemoria3.replace("D",""))
    print("PRINT DIV 3 PARAMS: ", mar, "\n" + "Tamaño: ", len(memoria))
    mdr = acc
    memoria[mar] = mdr
    
#Función que lee el valor del acc y lo coloca en la dirección que haya recibido
def storeFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  mar = int(instrucciones[0].replace("D",""))
  mdr = acc
  memoria[mar] = mdr

#Función que incrementa +1 a un valor almacenado en una dirección
def incFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  mar = int(instrucciones[0].replace("D",""))
  mdr = memoria[mar]
  acc = mdr
  alu = acc + 1
  acc = alu
  mdr = acc
  memoria[mar]=mdr

#Función que disminuye -1 a un valor almacenado en una dirección
def decFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  mar = int(instrucciones[0].replace("D",""))
  mdr = memoria[mar]
  acc = mdr
  alu = acc - 1
  acc = alu
  mdr = acc
  memoria[mar]=mdr

#Función que mueve un valor de una dirección a otra dirección
def movFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = instrucciones[1]
  mar = posicionMemoria1
  mdr = memoria[mar]
  mar = int(posicionMemoria2.replace("D",""))
  memoria[mar] = mdr

  mar = posicionMemoria1
  mdr = memoria[mar]
  memoria[mar] = None

#Función que muestra el valor almacenado en una dirección o en un registro como el MAR.
def showFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria
  print("ENTRÉ AL SHW")
  if instrucciones[0][0] == "D":
    posicionMemoria1 = int(instrucciones[0].replace("D",""))
    print(memoria[posicionMemoria1], " posicion:", instrucciones[0])
  elif instrucciones[0]=="ACC": 
    print(acc, " VALOR EN ACC")
  elif instrucciones[0]=="ICR": 
    print(icr, " VALOR EN ICR")
  elif instrucciones[0]=="MAR": 
    print(mar, " VALOR EN MAR")
  elif instrucciones[0]=="MDR": 
    print(mdr, " VALOR EN MDR")
  elif instrucciones[0]=="UC": 
    print(acc, " VALOR EN UC")

#Función BEQ
def beqFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria
  print("HACIENDO BEQ")
  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = instrucciones[1]
  posicionMemoria3 = instrucciones[2]
  if posicionMemoria2 == "NULL" and posicionMemoria3 == "NULL":
    mar = posicionMemoria1
    mdr = memoria[mar]
    if(mdr-acc == 0):
      acc=mdr
    
  elif posicionMemoria2 != "NULL" and posicionMemoria3 == "NULL":
    print("POSICIONMEMORIA1: ", posicionMemoria1)
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc=mdr
    alu=acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc=mdr
    if(alu - acc == 0):
      acc=alu
    
  else:
    mar = posicionMemoria1
    mdr = memoria[mar]
    acc = mdr
    alu = acc
    mar = int(posicionMemoria2.replace("D",""))
    mdr = memoria[mar]
    acc = mdr
    if(alu-acc == 0):
      valor = int(posicionMemoria3)
      mdr=acc + valor + pc
      memoria[mar] = mdr
      
  print(mdr," BEQ")

#Función AND
def andFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = int(instrucciones[1].replace("D",""))
  posicionMemoria3 = int(instrucciones[2].replace("D",""))
  mar=posicionMemoria1
  mdr=memoria[mar]
  acc=mdr
  alu=acc
  mar=posicionMemoria2
  mdr=memoria[mar]
  acc=mdr
  alu=acc & alu
  mar=posicionMemoria3
  mdr=memoria[mar]
  mdr= alu
  memoria[mar]=mdr
  print(mdr," AND")

#Función OR
def orFunction(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria

  posicionMemoria1 = int(instrucciones[0].replace("D",""))
  posicionMemoria2 = int(instrucciones[1].replace("D",""))
  posicionMemoria3 = int(instrucciones[2].replace("D",""))
  mar=posicionMemoria1
  mdr=memoria[mar]
  acc=mdr
  alu=acc
  mar=posicionMemoria2
  mdr=memoria[mar]
  acc=mdr
  alu=acc | alu
  mar=posicionMemoria3
  mdr=memoria[mar]
  mdr= alu
  memoria[mar]=mdr
  print(mdr," OR")
  
#Diccionario encargado de almacenar las funciones, es usado para reemplazar la estructura switch-case que no tiene el lenguaje.
diccionarioFuncs = {
  "SET":setFunction,
  "LDR":ldrFunction,
  "ADD":addFunction,
  "SUB":subFunction,
  "STR":storeFunction,
  "SHW":showFunction,
  "INC":incFunction,
  "DEC":decFunction,
  "MOV":movFunction,
  "MUL":mulFunction,
  "DIV":divFunction,
  "INC":incFunction,
  "DEC":decFunction,
  "BEQ":beqFunction,
  "AND":andFunction,
  "OR":orFunction
}

#Función que calcula la cantidad de espacios necesarios para el array memoria.
#Obtiene la dirección más alta y en base a ella hace el cálculo.
def calcularMemoriaTotal(instrucciones):
  global memoria
  direcciones = []
  archivo = open(instrucciones, "r")
  while(True): #Bucle para leer cada línea del .txt
    linea = archivo.readline() #Lee la línea según el bucle
    listadoLineas = linea.split() #Genera una  lista con cada palabra
    dirs = listadoLineas[1:4]
    direccion = listadoLineas[1].replace("D","")
    if direccion!="NULL" and direccion!="ACC" and direccion!="MDR" and direccion!="ICR" and direccion!="MAR" and direccion!="UC":
      for dir in dirs:
        if dir!="NULL":
          direcciones.append(int(dir.replace("D","")))
    if not linea or listadoLineas[0]=="END":
      break
  memoria = memoria*(max(direcciones)+1)

      
#Funcion que inicia el ciclo basico de instruccion
def cicloInstruccion(instrucciones):
  global acc
  global uc
  global alu
  global pc
  global mar
  global icr
  global mdr
  global memoria
  
  calcularMemoriaTotal(instrucciones)
  archivo = open(instrucciones, "r") #Abre el archivo .txt
  while(True): #Bucle para leer cada línea del .txt
    linea = archivo.readline() #Lee la línea según el bucle
    listadoLineas = linea.split() #Genera una  lista con cada palabra
    
    if not linea or listadoLineas[0]=="END":
      break
    
    if listadoLineas[0]!="SET": #set no aumenta el pc
      pc = pc + 1
    mar = pc
    mdr = listadoLineas[0]
    icr = mdr
    uc = icr
    print("PC: ", pc , "\n"
         "MAR: ", mar , "\n"
         "MDR: ", mdr , "\n"
         "ICR: ", icr , "\n"
         "Unidad Control: ", uc , "\n")
    diccionarioFuncs.get(uc)(listadoLineas[1:5])

cicloInstruccion("Instrucciones2.txt")