class Curso:
    def __init__(self,idCurso,descripcion,idEmpleado):
        self.__idCurso = idCurso
        self.__descripcion = descripcion
        self.__idEmpleado = idEmpleado

    @property
    def idCurso(self):
        return self.__idCurso

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idCurso.setter
    def idCurso(self,valor):
        self.__idCurso = valor

    @descripcion.setter
    def descripcion (self,valor):
        self.__descripcion = valor

    @idEmpleado.setter
    def idEmpleado (self,valor):
        self.__idEmpleado = valor

    def agregarCurso (self):
        origen = open("./archivos/curso.txt", "a", encoding = "utf8")
        origen.write(f"{self.__idCurso} | {self.__descripcion} | {self.__idEmpleado} \n")
         origen.close()

