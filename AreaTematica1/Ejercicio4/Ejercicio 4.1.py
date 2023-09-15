import scipy.optimize as spo
import math

if __name__ == '__main__':
  prob_matrix = []
  type_canal = int(input("Ingrese el valor de R (2, 3 o 4): "))
  #Cargo probabilidades en matriz
  for i in range(type_canal):
    row = []
    for j in range(type_canal):
      probability = float(
          input(f"Ingrese la probabilidad de la fila {i+1}, columna{j+1}:"))
      row.append(probability)
    prob_matrix.append(row)

# Funcion objetivo

  def informationMutua(AB):
    conditional_entropy = 0  #H(B/A)
    for j in range(type_canal):  #Itera sobre posibles salidas B
      conditional_entropy_contrib = 0  #Contribución de cada posible valor de B a la entropía condicional
      for i in range(
          type_canal
      ):  #itera sobre todas las posibles entradas de la variable aleatoria A
        conditional_entropy_contrib += AB[i] * prob_matrix[i][
            j]  #Se calcula la contribución a la entropía condicional y se suma a conditional_entropy_contrib multiplicando AB[i] por prob_matrix[i][j].
      if conditional_entropy_contrib != 0:
        conditional_entropy += conditional_entropy_contrib * math.log(
            1 / conditional_entropy_contrib, 2
        )  #Se acumula la entropía condicional total H(B|A) sobre todos los posibles valores de B dado A
    IM = 0
    for i in range(type_canal):
      x = 0
      for j in range(type_canal):
        if prob_matrix[i][j] != 0:
          x += prob_matrix[i][j] * math.log(1 / prob_matrix[i][j],
                                            2)  #Calcula la entropia
      IM += AB[i] * x
    conditional_entropy = conditional_entropy - IM
    return -conditional_entropy

# Aproximación inicial

  initial_AB = []
  for i in range(type_canal):
    initial_AB.append(1 / type_canal)

# Límites y restricciones
  if type_canal == 2:
    boundss = ((0, 1), (0, 1))
    constraints = ({'type': 'eq', 'fun': lambda AB: AB[0] + AB[1] - 1})
  if type_canal == 3:
    boundss = ((0, 1), (0, 1), (0, 1))
    constraints = ({'type': 'eq', 'fun': lambda AB: AB[0] + AB[1] + AB[2] - 1})
  if type_canal == 4:
    boundss = ((0, 1), (0, 1), (0, 1), (0, 1))
    constraints = ({
        'type': 'eq',
        'fun': lambda AB: AB[0] + AB[1] + AB[2] + AB[3] - 1
    })

    # Optimización
  result = spo.minimize(informationMutua,
                        initial_AB,
                        options={"disp": True},
                        constraints=constraints,
                        bounds=boundss)

  if result.success:
    AB = result.x
    print("Informacion mutua máxima:", result.fun * -1)
    i = 0
    for item in AB:
      print(f'P(a{i+1}) = {AB[i]}')
      i += 1
  else:
    print('Falló')
