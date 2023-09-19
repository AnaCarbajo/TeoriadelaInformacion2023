from tkinter import Tk
from tkinter.filedialog import askopenfilename
import math


def readfile(archivo):
  byts = []
  with open(archivo, 'rb') as file:
    while True:
      byte = file.read(1)
      if not byte:
        break
      byts.append(
          int.from_bytes(byte, byteorder='big')
      )  #convertimos cada byte en un numero entero y lo almacenamos en la lista
  return byts


def calcular(byts):
  q = 256  #cantidad de simbolos ascii
  r = 2  #base de logaritmo
  longitud_archivo = len(byts)

  simbolos = []
  for ch in range(q):
    simbolos.append(
        ch)  #almacenamos en una lista todos los simbolos del codigo ascii

  probabilidades = []
  for ch in simbolos:
    probabilidades.append(
        float(byts.count(ch) / longitud_archivo)
    )  #almacenamos las probabilidades de aparicion de cada simbolo en el archivo

  entropia = 0
  cont = 0
  for prob in probabilidades:
    if prob > 0:
      cont += 1
      entropia += prob * math.log(1 / prob, r)
  print("Entropia: ", entropia)
  print("Cantidad de simbolos: ",cont)
  entropia_maxima = math.log(float(cont), r)

  rendimiento = entropia / entropia_maxima

  redundancia = (1 - rendimiento) * 100
  print("Redundancia: ", redundancia, "%")


if __name__ == '__main__':

  Tk().withdraw()
  archivo = askopenfilename()

  byts = readfile(archivo)
  calcular(byts)
