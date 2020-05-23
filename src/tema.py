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

def IngresoTema(self):
    #para hacer lista
    import json
    temas=[]

    n=int(input("cuantos temas son?"))
    for i in range(n):
       tema=input("temas:")
       temas.append(tema)
    print(temas) 

    #para guardar en el archivo
    with open('archivos/temas.txt', 'w') as outfile: json.dump(temas, outfile)
