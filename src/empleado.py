class Empleado:
<<<<<<< HEAD
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
    print("empleado")

def eliminarEmpleado():
    print("eliminar")

def modificarEmpleado():
    print("modificar")

def consultarEmpleado():
    print("consulta")

def detallesEmpleado():
    print("detalles")


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

<<<<<<< HEAD
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

