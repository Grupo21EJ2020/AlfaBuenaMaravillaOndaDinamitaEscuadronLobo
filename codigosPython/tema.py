#########################
# Daniel Mendoza Perez  #
#   version 0.55        #
#########################

import json
temas=[]

n=int(input("cuantos temas son?"))
for i in range(n):
    tema=input("temas:")
    temas.append(tema)
print(temas) 

with open('archivos/temas.txt', 'w') as outfile: json.dump(temas, outfile)
