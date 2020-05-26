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