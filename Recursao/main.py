grad = [["m","a","i"],["x","x","u"],["z","u","y"]]

def gerar_prox_letras(x , y, n):
  coordenadas = []
  d_x = [1, -1, 0, 0, 1, 1, -1, -1]
  d_y = [0, 0, 1, -1, 1, -1, 1, -1]

  for i in range(8):
    pos_x, pos_y = x + d_x[i], y + d_y[i]
    if pos_x < n and pos_x >= 0 and pos_y < n and pos_y >= 0:
      coordenadas.append([pos_x, pos_y])
  return coordenadas

def gerar_combinacoes(lista):
  pass