class Empleado:
     def __init__(self, idEmpleado, nombre, direccion ):
        self.__idEmpleado= idEmpleado
        self.__nombre = nombre
        self.__direccion = direccion 

    @property  
    def idEmpleado(self):
        return self.__idEmpleado

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    @idEmpleado.setter
    def idEmpleado(self,valor):
        self.__idVideo = valor

    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor

    @direccion.setter
    def direccion(self,valor):
        self.__direccion = valor

    Menu=1
    while Menu != 6:
          print("MENU")
          print("1)Agregar Empleado")
          print("2)Eliminar Empleado")
          print("3)Modificar Empleado")
          print("4)Consultar Empleado")
          print("5)Ver detalles de Empleados")
          Menu=int(input("Seleción: "))

    if Menu == 1:
        print ("Registro de Empleado")
        archivo = open("./archivos/empleados.txt","a",encoding="utf8")

        print("Clave del Empleado ")
        idEmpleado = input("Id \n")
        print("Nombre del Empleado:\n")
        nombre = input("Nombre: \n")
        print("Direccion del Empleado")
        direccion = input("Direccion: \n ")

        archivo.write(idEmpleado + "|" + nombre + "|" + direccion)
        archivo.close()