#########################
# Daniel Mendoza Perez  #
#   version 0.55        #
#########################

import sys
import os
import json


temas=[]
ruta='arch/data.txt'


def addTema():
    if os.path.isfile(ruta):  # ya hay temas registrados
        tema=input('Tema a agregar? ')
        with open(ruta) as json_file: temas = json.load(json_file)
        if tema not in temas:
            temas.append(tema)
            with open(ruta, 'w') as outfile: json.dump(temas, outfile)
        qryTemas()   
    else:
        addTemas()
        qryTemas()   

def addTemas():
    n=int(input('cuantos temas vas a agregar? '))
    for i in range(n):
        tema=input('tema {0:02d}: '.format(i+1))
        temas.append(tema)
    with open(ruta, 'w') as outfile: json.dump(temas, outfile)

def qryTemas():
    try:
        with open(ruta) as json_file: temas = json.load(json_file)
        i=1
        for t in temas:
            print('tema {0:02d}: {1}'.format(i,t))
            i = i + 1
    except:
        print('Aún no existen temas registrados')

def rmvTema():
    qryTemas()
    tema=input('Tema a eliminar? ')
    with open(ruta) as json_file: temas = json.load(json_file)
    try:
        temas.remove(tema)
    except:
        print('El tema {} no está en la lista'.format(tema))
        rmvTema()
    with open(ruta, 'w') as outfile: json.dump(temas, outfile)
    qryTemas()

def updTema():
    qryTemas()
    tema=input('Tema a modificar? ')
    nvotema=input('Nuevo tema? ')
    with open(ruta) as json_file: temas = json.load(json_file)
    if tema not in temas:
        print('El tema {} no está en la lista'.format(tema))
    else:
        i=0
        for t in temas:
            if t.upper()==tema.upper():
                temas[i]=nvotema
                with open(ruta, 'w') as outfile: json.dump(temas, outfile)     
            i = i + 1
    qryTemas()  

def menu():
    while True:
        print('Elija una opción: (A, B, C ...)')
        print('A) Altas')
        print('B) Bajas')
        print('C) Consultas') 
        print('M) Modificaciones')            
        print('S) Salir')

        choice = input ('Opción a relizar: ')
        choice = choice.upper()

        if choice == "A":
            addTema()
        elif choice == "B":
            rmvTema()
        elif choice == "C":
            qryTemas()
        elif choice == "M":
            updTema()
        elif choice == "S":
            print("Saliendo del sistema")
            sys.exit(0)
        else:
            print("Opción no válida")

menu()       