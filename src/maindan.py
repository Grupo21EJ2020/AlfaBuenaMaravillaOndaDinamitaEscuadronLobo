import os.path 
import sys  
while True:
    print("seleccione una opcion")
    print("A) Curso")
    print("B) Curso tema")
    print("C) Empleado")
    print("D) Tema")
    print("E) Video")          

    choice = input ('Opción a relizar: ')
    choice = choice.upper()

    if choice == "A":
        execfile(os.path.join( os.path.dirname(sys.argv[0]), 'curso.py'))
    elif choice == "B":
        execfile(os.path.join( os.path.dirname(sys.argv[0]), 'curso_tema.py'))
    elif choice == "C":
        execfile(os.path.join( os.path.dirname(sys.argv[0]), 'empleado.py'))
    elif choice == "D": 
        execfile(os.path.join( os.path.dirname(sys.argv[0]), 'tema.py'))
    elif choice == "E": 
        execfile(os.path.join( os.path.dirname(sys.argv[0]), 'video.py'))
    else:
        print("Opción no válida")

    menu()