from tkinter import Tk 
from tkinter.filedialog import askopenfilename
import math

def readfile(archivo):
    byts = []
    with open(archivo,'rb') as file:
        while True:
            byte = file.read(1)
            if not byte:
                break
            byts.append(int.from_bytes(byte, byteorder='big'))
    return byts


def calcular(byts):
    q = 256 #cantidad de simbolos ascii
    r = 2 #base de logaritmo
    lenarchivo = len(byts)


    simbolos = []
    for ch in range(q):
        simbolos.append(ch) #almacenamos en una lista todos los simbolos del codigo ascii

    probabilidades = []
    for ch in simbolos:
        probabilidades.append(float(byts.count(ch)/lenarchivo))  #almacenamos las probabilidades de aparicion de cada simbolo en el archivo
    
    Entropia = 0
    for prob in probabilidades:
        if prob > 0:
            Entropia += prob * math.log(1/prob,r)
    print("Entropia: ", Entropia)

    EntropiaMaxima = math.log(float(q), r)

    Rendimiento = Entropia/EntropiaMaxima

    Redundancia = (1 - Rendimiento)*100
    print("Redundancia: ", Redundancia)

if __name__ == '__main__':
    
    Tk().withdraw()
    archivo = askopenfilename()

    byts = readfile(archivo)
    calcular(byts)