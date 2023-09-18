from ctypes import sizeof
from tkinter import *
import math
from turtle import bgcolor 

def cuit_validator(cuit):
    #Corrobora si el cuit/cuil cumple con el formato
    if cuit[2] != "-" or cuit[11] != "-" or len(cuit) != 13:
        return 2

    #Serie numérica que se necesita para multiplicar cada uno de los dígitos del cuil/cuit
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    cuit = cuit.replace("-", "")

    #Calcula el dígito verificador
    verification_digit= 0

    for i in range(10):
        verification_digit += int(cuit[i]) * base[i]

    resto = int(verification_digit / 11)
    verification_digit = 11 - (verification_digit - ( resto * 11))

    if verification_digit == 11:
        verification_digit = 0
    elif verification_digit == 10:
        verification_digit = 9
    elif verification_digit == int(cuit[10]):
        return 0
    else: return 1


def validations():
    cuit_result= cuit_validator(cuit)

    if cuit_result == 0:
        print(f"\n Número de CUIL/CUIT válido.")
    elif cuit_result == 1:
        print(f"\n Número de CUIL/CUIT inválido.")
    elif cuit_result == 2:
        print(f"\n Número de CUIL/CUIT incorrecto.")



if __name__ == "__main__" :
    cuit = input("Ingrese el CUIL/CUIT a validar: ")
    validations()

