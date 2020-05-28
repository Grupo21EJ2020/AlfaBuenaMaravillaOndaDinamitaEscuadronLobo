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
    archivo = open("./archivos/curso_tema_video.txt","a",encoding="utf8")
    idCursoTV=input("Ingrese id del Video del Tema de Curso: ")
    idCT=str(input("id Curso de Tema: "))
    idVideo=str(input("id Video:"))
    archivo.write(idCursoTV + "|" + idCT + "|" + idVideo + "\n")
    archivo.close()

def eliminar_idCursoTV():
    archivo = open("./archivos/curso_tema_video.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/curso_tema_video.txt","w",encoding="utf8")
    idCursoTV = input("Ingrese Id de Video del Tema de Curso a eliminar: ")
    
    for line in lines:
        id = line.split("|")[0]
        if idCursoTV!= id:
            archivo.write(line)
    archivo.close()
    

def modificar_idCursoTV():
    print("Modificacion de parametros: ")
    archivo = open("./archivos/curso_tema_video.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/curso_tema_video.txt","w",encoding="utf8")
    idCursoTV = input("Ingrese Id de Video del Tema de Curso a modificar: ")
    
    for line in lines:
        id = line.split("|")[0]
        if idCursoTV!= id:
            archivo.write(line)
        else:
            print("Ingrese nuevos datos de Video del Tema de Curso: ")
            idCursoTV=input("Ingrese id: ")
            idCT=int(input("ID Curso del Tema: "))
            idVideo=int(input("ID Video:"))
            archivo.writelines(idCursoTV + "|" + idCT + "|" + idVideo + "\n")

    archivo.close()
    

def consultar_idCursoTV():
    archivo = open("./archivos/curso_tema_video.txt", encoding = "utf8")
    print(archivo.read())
    archivo.close()

def detalle_idCursoTV():
    archivo = open("./archivos/curso_tema_video.txt",encoding = "utf8")
    lines=archivo.readlines()
    id_detalles = input("Ingrese Id de Video del Curso de Tema a para ver detalles: ")
    
    for line in lines:
        id = line.split("|")[0]
        if id_detalles== id:
            print(line)
    archivo.close()

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