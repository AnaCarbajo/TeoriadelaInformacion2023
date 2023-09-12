import math
A = []  # Probabilidades dadas
P = []  # Probabilidades Independientes de la entrada
PBj = []  # Probabilidades Independientes de la Salida
Pab = []  # Prababilidades Condicionales Hacia Atras
HA = 0  # Entropia del Emisor
HAb = []  # Condicionales de la fuente
HAB = 0  # Condicional de Entropia
IM = 0

def CalcularInformacionMutua(R, HA, PBj, HAb):
    res = 0
    for i in range(R):
        res += PBj[i] * HAb[i]
    HAB = res
    return (HA - HAB)

def CondicionalesFuente(R):
    count = 0
    res = 0
    for i in range(R):
        for j in range(R):
            res += (Pab[count] * math.log((1/Pab[count]),2))
            count += 1
        HAb.append(float(round(res,ndigits=5)))
        res = 0

def CalcularCondicionalesHaciaAtras(R):
    res= 0
    count = 0
    for i in range(R):
        for j in range(R):
          res += ((P[j] * A[count]) / PBj[i])
          count += 1
          Pab.append((float(round(res,ndigits=2))))
          res = 0 

def calcularEntropiaEntrada(R):
    res = 0
    for i in range(R):
        res += P[i] * math.log((1/P[i]), 2)
    return res

def calcularProbabilidad(R):
    count = 0
    resultado = 0
    for i in range(R):
        for j in range(R):
            resultado += (P[j] * A[count])
            count +=1
        PBj.append(round(resultado,ndigits=3))
        resultado = 0

def main():
    R = int(input("Ingrese el valor de R (2, 3 o 4): "))

    for i in range(R*R):
        Ai = float(input(f"Ingrese el valor de A{i + 1}: "))
        A.append(Ai)
 #Se puede ingresar por teclado o dividir 1 en cantidad de filas y tener las probabilidades
    for i in range(R):
        Pi = float(input(f"Ingrese el valor de P{i + 1}: "))
        P.append(Pi)

    calcularProbabilidad(R)
    HA = calcularEntropiaEntrada(R)
    CalcularCondicionalesHaciaAtras(R)
    CondicionalesFuente(R)
    IM = CalcularInformacionMutua(R, HA, PBj, HAb)

    print("Probabilidad Independientes de Salida:", PBj)
    print(f"Entropía del Emisor: {HA:.5f}")
    print(f"Informacion Mutua: {IM:.5f}")

if __name__ == "__main__":
    main()
