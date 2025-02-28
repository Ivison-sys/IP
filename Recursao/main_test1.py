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

# def gerar_combinacoes(grid,caminhos, n,indice=0):
#   resultado = []
#   if indice >= 3:
#     return caminhos
#   for i in range(len(caminhos)):
#     caminhos_gerados = []
#     caminho = caminhos[i]
#     print(caminho[-1][0], caminho[-1][1], n)
#     prox_coordenadas = gerar_prox_letras(caminho[-1][0], caminho[-1][1], n)
#     for prox_coordenada in prox_coordenadas:
#       new_caminho = caminho + [prox_coordenada]
#       caminhos_gerados.append(new_caminho)
#     resultado.append(caminhos_gerados)
  
#   return gerar_combinacoes(grid, resultado, n, indice+1)
  
# print(gerar_combinacoes(grad, [[[0,0]]], 3)
