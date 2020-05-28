#ESTE SERA EL MAIN DEL PROGRAMA
from curso import Curso
from curso_tema import Curso_Tema
from empleado import Empleado
from video import Video
while opcion == 1 and opcion == 2 and opcion == 3 and opcion == 4 and opcion == 5 and opcion ==6 and opcion ==7:
    print("*** Bienvenido al programa para Empezar alamcenar tu informacion, acorde a lo que nos indiques")
    print(" *** MENU DEL CURSO ***") 
    print("1.- Menu del Curso")
    print("2.- Menu del empleado")
    print("3.- Menu del video")
    print("4.- Menu del Tema")
    print("5.- Menu del Curso_Tema")
    print("6.- Menu del Curso_Tema_Video")
    print("7.- Salir")
    opcion = int(input("> "))
    if opcion == 1:
        Curso.Menu()
