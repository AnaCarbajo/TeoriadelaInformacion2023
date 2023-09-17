from tkinter import *
import math

def createCharactersList(chain1,chain2, characters):
    cont = 0
    porc = 0
    if not characters:
        for i in chain1:
            for j in chain2:
                if i == j:
                    if j not in characters and j!= " ":
                        characters.append(j)
                        cont +=1
    else:
        characters.clear()
        for i in chain1:
            for j in chain2:
                if i == j:
                    if j not in characters and j!= " ":
                        characters.append(j)
                        cont +=1
    porc = round((cont/len(chain1))*100,ndigits=5)
    print(f"\nCaracteres que se repiten: \n {characters}")
    print(f"\nLas cadenas {chain1} y {chain2} tienen un parecido de: {porc}% \n")

if __name__ == "__main__" :
    characters = []
    score = int(0)
    chain1 = input("Ingrese la primera cadena: ")
    chain2 = input("Ingrese la segunda cadena: ")
    createCharactersList(chain1.upper(),chain2.upper(), characters)