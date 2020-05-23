class Tema:
     def __init__(self,idTema,Nombre,):
        self.__idTema = idTema
        self.__Nombre = Nombre

@property
def idTema(self):
    return self.__idTema

@property
def Nombre(self):
    return self.__Nombre

@idTema.setter
def idTema(self,valor):
    return self.__idTema

@Nombre.setter
def Nombre(self,valor):
    return self.__Nombre

def IngresoCant(self):
    #para hacer lista
    import json
    self.__idTemas=[]

    n=int(input("Cuales son los ID? "))
    for i in range(n):
       ident=input("ID: ")
       self.__idTemas.append(ident)
    print(self.__idTemas) 

    #para guardar en el archivo
    with open('archivos/IDtemas.txt', 'w') as outfile: json.dump(self.__idTemas, outfile)

def IngresoNom(self):
        #para hacer lista
    import json
    self.__Nombre=[]

    n=int(input("cuantos Nombres Ingresaras? "))
    for i in range(n):
       tema=input("Ingresa el Nombre segun como ingresaste los ID: ")
       self.__Nombre.append(tema)
    print(self.__Nombre) 

    #para guardar en el archivo
    with open('archivos/Temas.txt', 'w') as outfile: json.dump(self.__Nombre, outfile)


    
#combino id con nombre
#with open('archivo1.txt') as f1, open('archivo2.txt') as f2, open('archivounion.txt', 'w') as of:
    #line_1 = f1.readlines()[0].strip()
    #line_2 = f2.readlines()[5].strip()
    #out_line = "{}, {}".format(line_1[:-1], line_2[1:])
    #of.write(out_line)