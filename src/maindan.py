
from tema import menu


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
        print("ya fue")
elif choice == "B":
        print("tango")
elif choice == "T":
        tema.menu()
elif choice == "S":
    print("Saliendo del sistema")
    sys.exit(0)
else:
    print("Opción no válida")

menu()            