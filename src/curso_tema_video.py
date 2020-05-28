from io import open
import os
class Curso_Tema_Video:
     def __init__(self,idCursoTV,idCT,idVideo):
        self.__idCursoTV = idCursoTV
        self.__idCT = idCT
        self.__idVideo = idVideo

@property
def idCursoTV(self):
    return self.__idCursoTV

@property
def idCT(self):
    return self.__idCT
@property
def idVideo(self):
    return self.__idVideo

@idCursoTV.setter
def idCursoTV(self,valor):
    return self.__idCursoTV

@idCT.setter
def idCT(self,valor):
    return self.__idCT

@idVideo.setter
def idVideo(self,valor):
    return self.__idVideo

global lista
lista=list()

def agregar_idCursoTV():
    archivo = open("./archivos/Curso_Tema_Video.txt","a",encoding="utf8")
    idCursoTV=input("Ingrese id del Video del Tema de Curso: ")
    idCT=str(input("id Curso de Tema: "))
    idVideo=str(input("id Video:"))
    archivo.write(idCursoTV + "|" + idCT + "|" + idVideo + "\n")
    archivo.close()

def eliminar_idCursoTV():
    archivo = open("./archivos/Curso_Tema_Video.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/Curso_Tema_Video.txt","w",encoding="utf8")
    idCursoTV = input("Ingrese Id de Video del Tema de Curso a eliminar: ")
    
    for line in lines:
        id = line.split("|")[0]
        if idCursoTV!= id:
            archivo.write(line)
    archivo.close()
    

def modificar_idCursoTV(self):
    self.archivo = open("./archivos/Curso_Tema_Video.txt", "r", enconding = "utf8")
    self.archivo_temp = open("./archivos/Curso_Tema_Video_temp.txt", "w", enconding = "utf8")

    print("Que id quieres modificar?: ")
    self.id_mod = input("> ")
    print("Crea un nuevo id para el Video del Tema de Curso: ")
    self.id_mod = input("> ")
    print("Crea un nuevo id para Curso de Tema: ")
    self.idCT = input("> ")
    print("Crea un nuevo id para el Video")
    self.idVideo = input("> ")

    for renglon in self.archivo:
        id = renglon.split("|") [0]
        if self.id_mod != id:
            self.archivo_temp.write(renglon)
        elif self.id_mod == id:
            self.archivo_temp.write(self.idCursoTV + "|" + self.idCT + "|" + self.idVideo + "\n")
    self.archivo.close()
    self.archivo_temp.close()
    os.remove("./archivo/curso_tema_video.txt")
    os.rename("./archivos/curso_tema_video_temp.txt", "./archivos/curso_tema_video.txt")
    

def consultar_idCursoTV(self):
    self.archivo = open("./archivos/curso_tema_video.txt", enconding = "utf8")
    print(archivo.read())
    self.archivo.close()

 def detalle_idCursoTV(self):
     self.archivo = open("./archivos/curso_tema_video.txt",enconding = "utf8")
        
     print("Dime el id que buscas")
     self.id_buscar = input(">")

     for renglon in self.archivo:
        id = renglon.split("|") [0]
        if self.id_buscar == id:
           print(renglon)
           break

        self.archivo.close()

def menu():
    Menu=0
    while Menu!=6:

        print("MENU")
        print("1)Agregar Curso Tema Video")
        print("2)Eliminar Curso Tema Video")
        print("3)Modificar Curso Tema Video")
        print("4)Consultar Curso Tema Video")
        print("5)Ver detalles de Curso Tema Videos")
        Menu=int(input("Seleción: "))

        if Menu == 1:
            agregar_idCursoTV()
        elif Menu == 2:
            eliminar_idCursoTV()
        elif Menu == 3:
            modificar_idCursoTV()
        elif Menu == 4:
            consultar_idCursoTV()
        elif Menu == 5:
            detalle_idCursoTV()

menu()