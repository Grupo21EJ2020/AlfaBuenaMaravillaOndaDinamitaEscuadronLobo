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
        lines = origen.readlines()
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


    def leeDetallesCurso(self):
        archivo = open("./archivos/curso.txt","r",encoding="utf8")
        lines = archivo.readlines()
        id_detalles = input("Ingrese iD del curso a para ver ese en especifico: ")
    
        for line in lines:
            id = line.split("|")[0]
            if id_detalles == id:
                print(line)
        archivo.close()

    def Menu():
        while True:
            print(" *** MENU DEL CURSO *** ")
            print("1.- Agregar Curso")
            print("2.- Eliminar Curso")
            print("3.- Modificar Curso")
            print("4.- Ver todos los cursos")
            print("5.- Ver algun curso")
            print("6.- Salir")
            Menu=int(input("Seleción: "))
            primerID = 0
            textoPrincipal = ""
            segundoiD = 0 
            clase = Curso(primerID,textoPrincipal,segundoiD)
            
            if Menu == 1:
                primerID = int(input("Dime el primer id"))
                textoPrincipal = input("Dime el texto que quieres")
                segundoiD = int(input("Dime el segundo id"))
                clase = Curso(primerID, textoPrincipal, segundoiD)
                clase.agregarCurso()
            
            elif Menu == 2:
                clase.eliminarCurso()
            
            elif Menu == 3:
                numero = int(input("Dime el id del que quieres modificar: "))
                idAModificar = int(input("Dime el id que quieres poner: "))
                textoAModificar = input("Dime el nombre del curso: ")
                idAModificarEmpleado = int(input("Dime el id del Empleado: "))
                clase.modificarCurso(numero,idAModificar,textoAModificar, idAModificarEmpleado)
                
            elif Menu == 4:
                Curso.leerTodoCurso()
            
            elif Menu == 5:
                Curso.leeDetallesCurso()

            elif Menu == 6:
                break

            else:
                print("Ha escogido un numero erroneo")

Curso.Menu()















