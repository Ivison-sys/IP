def relacionar_letras_palavrasAlvos(letra):
  if letra == "P":
    return ["PENGUINBAR", "PRAIAGELADA", "PENGUICUPSTADIUM"]
  elif letra == "D":
    return ["DELEGACIAPOLAR"]
  elif letra == "S":
    return ["SUBZEROWAY"]
  elif letra == "F":
    return ["FRIODEJANEIRO"]
  else:
    return []

def palavra_normal(palavra):
  if palavra == "PENGUINBAR": 
    return "Penguin Bar"
  elif palavra == "PRAIAGELADA":
      return "Praia Gelada" 
  elif palavra == "PENGUICUPSTADIUM":
    return "PenguiCup Stadium" 
  elif palavra == "SUBZEROWAY":
    return "SubzeroWay"


def gerar_prox_posicoes(pos, n):
  x, y = pos[0], pos[1]
  coordenadas = []
  d_x = [1, -1, 0, 0, 1, 1, -1, -1]
  d_y = [0, 0, 1, -1, 1, -1, 1, -1]

  for i in range(8):
    pos_x, pos_y = x + d_x[i], y + d_y[i]
    if pos_x < n and pos_x >= 0 and pos_y < n and pos_y >= 0:
      coordenadas.append([pos_x, pos_y])
  return coordenadas
 

isAchei = False
palavraAchada = ""

def gerar_combinacoes(grid, n, posicao, palavras_alvo, palavra_atual):
  global isAchei
  global palavraAchada
  
  original = grid[posicao[1]][posicao[0]]
  grid[posicao[1]][posicao[0]] = "1"

    
  if palavra_atual in palavras_alvo:
    palavraAchada = palavra_atual
    isAchei = True
  
  lista = gerar_prox_posicoes(posicao, n)
  if not isAchei:
    for p in lista:
      letra = grid[p[1]][p[0]]
      for palavra_alvo in palavras_alvo:
        if palavra_atual + letra in palavra_alvo:
          x = grid[p[1]][p[0]] 
          gerar_combinacoes(grid, n, p, palavras_alvo, palavra_atual + letra)
          grid[p[1]][p[0]] = x
  
  grid[posicao[1]][posicao[0]] = original

n = int(input())
matriz = []
inicios_busca = []

for y in range(n):
  inp = input()
  linha = inp.split(" ")
  matriz.append(linha)
  for x in range(n):
    if linha[x] in ["P", "D", "S", "F"]:
      inicios_busca.append([x,y])

for inicio in inicios_busca:
  copia = matriz.copy()
  letra = matriz[inicio[1]][inicio[0]]
  alvos = relacionar_letras_palavrasAlvos(letra)
  busca = gerar_combinacoes(matriz, n, inicio, alvos, letra)
  if isAchei:
    break

if (palavraAchada):
  if palavraAchada == "DELEGACIAPOLAR":
    print("Se formos até a Delegacia Polar, estaremos mexendo com um fora da lei. Vamos até lá investigar!")
  elif palavraAchada == "FRIODEJANEIRO":
    print("ARRGH! Todos sabem que o melhor carnaval é no bloco Pinguim da Madrugada. Vamos buscar nossa estátua no Frio de Janeiro")
  else:
    print(f"Temos que correr! O Pinguim da Madrugada pode estar no(a) {palavra_normal(palavraAchada)}. Vamos salvar nosso Carnaval de Inverno!") 
else:
  print("Nosso carnaval de inverno está perdido... NÃOOOOO")