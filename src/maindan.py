from curso import Curso


while True:
    print("seleccione una opcion")
    print("A) curso")
    print("B) curso tema")
    print("C) empleado")
    print("T) Tema")
    print("S) Salida")            

    choice = input ('Opción a relizar: ')
    choice = choice.upper()

    if choice == "A":
            Curso.menu
    elif choice == "B":
            print("tango")
    elif choice == "T": 
        execfile('tema.py')
    elif choice == "S":
        print("Saliendo del sistema")
        sys.exit(0)
    else:
        print("Opción no válida")

menu()            