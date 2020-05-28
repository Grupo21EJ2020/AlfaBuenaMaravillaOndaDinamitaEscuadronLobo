from io import open
import os
import json
class Video:
    def __init__(self,idVideo,nombre,url,fechaPublicacion):
        self.__idVideo = idVideo
        self.__nombre = nombre
        self.__url = url
        self.__fechaPublucacion = fechaPublicacion


@property
def idVideo(self):
    return self.__idVideo

@property
def nombre(self):
    return self.__nombre

@property
def url(self):
    return self.__url

@property
def fechaPublicacion(self):
    return self.__fechaPublicacion

@idVideo.setter
def idVideo(self,valor):
    self.__idVideo = valor
    
@nombre.setter
def nombre(self,valor):
    self.__nombre = valor

@url.setter
def url(self,valor):
    self.__url = valor

@fechaPublicacion.setter
def fechaPublicacion(self,valor):
    self.__fechaPublicacion = valor

global lista
lista=list()



def agregarVideo():
    archivo = open("./archivos/videos.txt","a",encoding="utf8")
    idVideo=input("Ingrese id: ")
    Nombre=str(input("Nombre: "))
    url=str(input("Url:"))
    fecha=str(input("Fecha:"))
    archivo.write(idVideo + "|" + Nombre + "|" + url + "|" + fecha + "\n")
    archivo.close()

def eliminarVideo():
    archivo = open("./archivos/videos.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/videos.txt","w",encoding="utf8")
    idVideo = input("Ingrese Id del video a eliminar: ")
    for line in lines:
        id = line.split("|")[0]
        if idVideo!= id:
            archivo.write(line)
    archivo.close()
    

def modificarVideo():
    print("Modificacion de Video: ")
    archivo = open("./archivos/videos.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/videos.txt","w",encoding="utf8")
    idVideo = input("Ingrese Id del video a modificar: ")
    
    for line in lines:
        id = line.split("|")[0]
        if idVideo!= id:
            archivo.write(line)
        else:
            print("Ingrese nuevos datos de empleado: ")
            idVideo=input("Ingrese id: ")
            Nombre=str(input("Nombre: "))
            url=str(input("Url: "))
            fecha=str(input("Fecha: "))
            archivo.writelines(idVideo + "|" + Nombre + "|" + url+ "|" + fecha + "\n")

    archivo.close()

def consultarVideo(): 
    archivo = open("./archivos/videos.txt","r", encoding = "utf8")    
    print("Datos de Videos: ")
    print(archivo.read())
    archivo.close()

def detallesVideos():
    archivo = open("archivos/videos.txt")
    print(archivo.read())

def menu():
    Menu=0
    while Menu!=6:

        print("MENU")
        print("1)Agregar Video")
        print("2)Eliminar Video")
        print("3)Modificar Video")
        print("4)Consultar Video")
        print("5)Ver detalles de Videos")
        print("6)Salir del menu de videos")
        Menu=int(input("Seleción: "))

        if Menu == 1:
            agregarVideo()
        elif Menu == 2:
            eliminarVideo()
        elif Menu == 3:
            modificarVideo()
        elif Menu == 4:
            consultarVideo()
        elif Menu == 5:
            detallesVideos()
        elif Menu ==6:
            break

menu()