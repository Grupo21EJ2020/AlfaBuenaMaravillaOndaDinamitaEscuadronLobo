from io import open
import json
class Video:
    def __init__(self,idVideo,nombre,url,fechaPublicacion):
        self.__idVideo = idVideo
        self.__nombre = nombre
        self.__url = url
        self.__fechaPublicacion = fechaPublicacion

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

    def detallesVideo(self):
        print(f"idVideo: {self.__idVideo}\nNombre: {self.__nombre}\nUrl: {self.__url}\nFecha de Publicacion: {self.__fechaPublicacion}")
    
    def guardarVideo(self):
        info = (f"{self.__idVideo}|{self.__nombre}|{self.__url}|{self.__fechaPublicacion}\n")
        archivo = open("archivos/videos.txt","a")
        archivo.write(info)
        archivo = open("archivos/videos.txt")
        print(archivo.read())
        archivo.close
    
    def eliminarVideo(self):
        lista = []
        info = (f"{self.__idVideo}|{self.__nombre}|{self.__url}|{self.__fechaPublicacion}\n")
        archivo = open("archivos/videos.txt","r")
        for i in archivo:
            if i not in info:
                lista.append(i)
        archivo = open("archivos/videos.txt","w")
        nl = "\n".join(lista)
        archivo.write(nl)
        archivo = open("archivos/videos.txt")
        print(archivo.read())
        archivo.close
    
    def modificarVideo(self,nombreObjeto):
        #el nombre del objeto que desean modificar debe ser el mismo nombre que se usara en la funcion ejemplo
        # nombreobjeto.("nombreobjeto") dentro de los parentesis debe llevar comillas para que la use como un string
        lista = []
        info = (f"{self.__idVideo}|{self.__nombre}|{self.__url}|{self.__fechaPublicacion}\n")
        archivo = open("archivos/videos.txt","r")
        for i in archivo:
            if i not in info:
                lista.append(i)
            else:
                id = input("Ingresa el nuevo id del video: ")
                nombre = input("Ingresa el nuevo nombre del video: ")
                url = input("Ingresa el nuevo url del video: ")
                fecha = input("Ingresa la nueva fecha del video: ")
                videonuevo = (f"{id}|{nombre}|{url}|{fecha}")
                lista.append(videonuevo)
                    
        archivo = open("archivos/videos.txt","w")
        nl = "\n".join(lista)
        archivo.write(nl)
        archivo = open("archivos/videos.txt")
        print(archivo.read())
        archivo.close
        
def DetallesTodosVideos():
    archivo = open("archivos/videos.txt")
    print(archivo.read())