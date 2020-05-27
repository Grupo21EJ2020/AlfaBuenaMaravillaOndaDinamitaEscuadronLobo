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

    global lista
    lista=list()

    def agregarCurso (self):
        origen = open("./archivos/curso.txt", "a", encoding = "utf8")
        origen.write(f"{self.__idCurso}|{self.__descripcion}|{self.__idEmpleado} \n")
        origen.close()
        
    def modificarCurso(self,numero,id1,texto,id2):
        archivo_texto = open("./archivos/curso.txt", "r+")
        lista_texto = archivo_texto.readlines();
        numero -= 1
        lista_texto[numero] = f"{id1}|{texto}|{id2}" 
        archivo_texto.seek(0)
        archivo_texto.writelines(lista_texto)
        archivo_texto.close()


    def eliminarCurso(self):
        origen = open("./archivos/curso.txt","r",encoding="utf8")
        lines=archivo.readlines()
        origen.close()
        origen = open("./archivos/curso.txt","w",encoding="utf8")
        idCurso = input("Ingrese Id de empleado a eliminar: ")
        for line in lines:
            id = line.split("|")[0]
            if idCurso != id:
                origen.write(line)
        origen.close()

    def leerTodoCurso(self):
       origen = open("./archivos/curso.txt", encoding='utf8')
       print(origen.read())
       origen.close()


    def detallesEmpleado(self):
        archivo = open("./archivos/curso.txt","r",encoding="utf8")
        lines = archivo.readlines()
        id_detalles = input("Ingrese Id de empleado a para ver detalles: ")
    
        for line in lines:
            id = line.split("|")[0]
            if id_detalles == id:
                print(line)
        archivo.close()

    

primerID = int(input("Dime el primer id"))
textoPrincipal = input("Dime el texto que quieres")
segundoiD = int(input("Dime el segundo id"))
clase = Curso(primerID, textoPrincipal, segundoiD)
clase.agregarCurso()
clase.detallesEmpleado()
















