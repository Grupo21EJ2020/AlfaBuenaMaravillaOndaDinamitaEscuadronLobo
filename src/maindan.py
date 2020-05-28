import os.path 
import sys  

rutacode = os.path.dirname(sys.argv[0])
rutacurso = "python " + rutacode + "/curso.py"
rutacursotema = "python " + rutacode + "/curso_tema.py"
rutatema = "python " + rutacode + "/tema.py"
rutaempleado = "python " + rutacode + "/empleado.py"
rutavideo = "python " + rutacode + "/video.py"
rutactm = "python " + rutacode + "/curso_tema_video.py"

while True:
    print("seleccione una opcion")
    print("A) Curso")
    print("B) Curso tema")
    print("C) Empleado")
    print("D) Tema")
    print("E) Video")
    print("F) CursoTemaVideo")          

    choice = input ('Opción a relizar: ')
    choice = choice.upper()

    if choice == "A":
        os.system(rutacurso)
    elif choice == "B":
        os.system(rutacursotema)
    elif choice == "C":
        os.system(rutaempleado)
    elif choice == "D": 
        os.system(rutatema)
    elif choice == "E": 
        os.system(rutavideo)
    elif choice == "F":
        os.system(rutactm)
    else:
        print("Opción no válida")

menu()