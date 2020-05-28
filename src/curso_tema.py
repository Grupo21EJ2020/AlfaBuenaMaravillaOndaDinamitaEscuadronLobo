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
    
    def agregar_curso_tema():
        self.archivo = open("./archivos/curso_tema.txt", "a", enconding= "utf8")
       
        print("Cual es el id del tema del curso?")
        self.idcursoTema = input("es")
        
        print("Cual es el id del curso?")
        self.idcurso = input("es")
       
        print("Cual es el id del tema?")
        self.idTema = input("es")
        self.archivo.write(idcursotema + "|" + idcurso + "|" + idtema)
        self.archivo.close()

    
    def consultar_curso_tema(self):
        self.archivo = open("./archivos/curso_tema.txt", enconding = "utf8")
        print(archivo.read())
        self.archivo.close()
    
    def detalle_curso_tema(self):
        self.archivo = open("./archivos/curso_tema.txt",enconding = "utf8")
        
        print("Dime el id que buscas")
        self.id_buscar = input(">")

        for renglon in self.archivo:
            id = renglon.split("|") [0]
            if self.id_buscar == id:
                print(renglon)
                break

        self.archivo.close()
    
    def modificar_curso_tema(self):
        self.archivo = open("./archivos/curso_tema.txt", "r", enconding = "utf8")
        self.archivo_temp = open("./archivos/curso_tema_temp.txt", "w", enconding = "utf8")

        print("Que id quieres modificar?: ")
        self.id_mod = input("> ")
        print("Crea un nuevo id para el tema del curso: ")
        self.id_curso = input("> ")
        print("Crea un nuevo id para curso: ")
        self.idcursoTema = input("> ")
        print("Crea un nuevo id para el tema")
        self.idtema = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|") [0]
            if self.id_mod != id:
                self.archivo_temp.write(renglon)
            elif self.id_mod == id:
                self.archivo_temp.write(self.idcursotema + "|" + self.idcurso + "|" + self.idtema + "\n")
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivo/curso_tema.txt")
        os.rename("./archivos/curso_tema_temp.txt", "./archivos/curso_tema.txt")
    def borrar_curso_tema(self):
        self.archivo = open("./archivos/curso_tema.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/curso_tema_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres borrar")
        self.id_borrar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_borrar != id:
                self.archivo_temp.write(renglon)
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/curso_tema.txt")
        os.rename("./archivos/curso_tema_temp.txt","./archivos/curso_tema.txt")

Curso_Tema()







    

