import os

class Curso_Tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.__idCursoTema = idCursoTema
        self.__idCurso = idCurso
        self.__idTema = idTema
        
    @property
    def idCursoTema(self):
        return self.__idCurso

    @property
    def idCurso(self):
        return self.__idCurso
    
    @property 
    def idTema(self):
        return self.__idTema
    
    @idCursoTema.setter
    def idCursoTema(self,valor):
        self.__idCursoTema = valor

    @idCurso.setter
    def idCurso(self,valor):
        self.__idCurso = valor

    @idTema.setter
    def idTema(self,valor):
        self.__idTema = valor
    
   global lista
lista=list()

def agregar_curso_tema():
    archivo = open("./archivos/curso_tema.txt","a",encoding="utf8")
    idCursoTema=input("Ingrese el id del curso del tema: ")
    idCurso=input("Ingrese el id del Curso: "))
    idTema= input("Ingrese el id del tema: ")
    archivo.write(idCursoTema + "|" + idCurso + "|" + idTema + "\n")
    archivo.close()

def eliminar_curso_tema():
    archivo = open("./archivos/curso_tema.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/curso_tema.txt","w",encoding="utf8")
    idcursoTema = input("Ingrese Id del tema  a eliminar: ")
    
    for line in lines:
        id = line.split("|")[0]
        if idcursoTema!= id:
            archivo.write(line)
    archivo.close()
    

def modificar_curso_tema_():
    print("Modificacion de parametros: ")
    archivo = open("./archivos/curso_tema.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/curso_tema.txt","w",encoding="utf8")
    idcursoTema = input("Ingrese Id de : ")
    
    for line in lines:
        id = line.split("|")[0]
        if idcursoTema!= id:
            archivo.write(line)
        else:
            print("Ingrese nuevos datos sobre curso_tema: ")
            idCursoTema=input("Ingrese id: ")
            idCurso=(input("Ingrese id: "))
            idTema=(input("Ingrese id: "))
            archivo.writelines(idCursoTema + "|" + idCurso + "|" + idTema + "\n")

    archivo.close()

def consultar_curso_tema(): 
    archivo = open("./archivos/curso_tema.txt","r", encoding = "utf8")    
    print("Datos de curso_tema: ")
    print(archivo.read())
    archivo.close()

def detalles_curso_empleado():
    archivo = open("./archivos/curso_tema.txt","r",encoding="utf8")
    lines=archivo.readlines()
    id_detalles = input("Ingrese Id para ver detalles: ")
    
    for line in lines:
        id = line.split("|")[0]
        if id_detalles== id:
            print(line)
    archivo.close()

def menu():
    Menu=0
    while Menu!=6:

        print("MENU")
        print("1)Agregar id: ")
        print("2)Eliminar id: ")
        print("3)Modificar id: ")
        print("4)Consultar id: ")
        print("5)Ver detalles del id: ")
        Menu=int(input("Seleción: "))

        if Menu == 1:
            agregar_curso_tema()
        elif Menu == 2:
            eliminar_curso_tema()
        elif Menu == 3:
            modificar_curso_tema_()
        elif Menu == 4:
            consultar_curso_tema()
        elif Menu == 5:
            detalles_curso_empleado()

menu()










    

