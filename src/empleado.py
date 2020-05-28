from io import open
import os
class Empleado:
     def __init__(self,idEmpleado,Nombre,direccion):
        self.__idEmpleado = idEmpleado
        self.__Nombre = Nombre
        self.__direccion = direccion

@property
def idEmpleado(self):
    return self.__idEmpleado

@property
def Nombre(self):
    return self.__Nombre
@property
def direccion(self):
    return self.__direccion

@idEmpleado.setter
def idEmpleado(self,valor):
    return self.__idEmpleado

@Nombre.setter
def Nombre(self,valor):
    return self.__Nombre

@direccion.setter
def direccion(self,valor):
    return self.__direccion

global lista
lista=list()

def agregarEmpleado():
    archivo = open("./archivos/empleado.txt","a",encoding="utf8")
    idEmpleado=input("Ingrese id: ")
    Nombre=str(input("Nombre: "))
    direccion=str(input("Direccion:"))
    archivo.write(idEmpleado + "|" + Nombre + "|" + direccion + "\n")
    archivo.close()

def eliminarEmpleado():
    archivo = open("./archivos/empleado.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/empleado.txt","w",encoding="utf8")
    idEmpleado = input("Ingrese Id de empleado a eliminar: ")
    
    for line in lines:
        id = line.split("|")[0]
        if idEmpleado!= id:
            archivo.write(line)
    archivo.close()
    

def modificarEmpleado():
    print("Modificacion de parametros: ")
    archivo = open("./archivos/empleado.txt","r",encoding="utf8")
    lines=archivo.readlines()
    archivo.close()
    archivo=open("./archivos/empleado.txt","w",encoding="utf8")
    idEmpleado = input("Ingrese Id de empleado a modificar: ")
    
    for line in lines:
        id = line.split("|")[0]
        if idEmpleado!= id:
            archivo.write(line)
        else:
            print("Ingrese nuevos datos de empleado: ")
            idEmpleado=input("Ingrese id: ")
            Nombre=str(input("Nombre: "))
            direccion=str(input("Direccion:"))
            archivo.writelines(idEmpleado + "|" + Nombre + "|" + direccion + "\n")

    archivo.close()

def consultarEmpleado(): 
    archivo = open("./archivos/empleado.txt","r", encoding = "utf8")    
    print("Datos de Empleados: ")
    print(archivo.read())
    archivo.close()

def detallesEmpleado():
    archivo = open("./archivos/empleado.txt","r",encoding="utf8")
    lines=archivo.readlines()
    id_detalles = input("Ingrese Id de empleado a para ver detalles: ")
    
    for line in lines:
        id = line.split("|")[0]
        if id_detalles== id:
            print(line)
    archivo.close()

def menu():
    Menu=0
    while Menu!=6:

        print("MENU")
        print("1)Agregar Empleado")
        print("2)Eliminar Empleado")
        print("3)Modificar Empleado")
        print("4)Consultar Empleado")
        print("5)Ver detalles de Empleados")
        Menu=int(input("Seleción: "))

        if Menu == 1:
            agregarEmpleado()
        elif Menu == 2:
            eliminarEmpleado()
        elif Menu == 3:
            modificarEmpleado()
        elif Menu == 4:
            consultarEmpleado()
        elif Menu == 5:
            detallesEmpleado()

menu()