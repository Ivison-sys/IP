def separar_nos(text):
  text = text.replace('[', "")
  text = text.replace("], ", "+")
  text = text.replace("]", "")
  text = text.replace(", ", "!")
  text+= "+"
  nos = []
  no = []
  
  inicio = 0
  for i in range(len(text)):
    if text[i] == '!':
      no.append(int(text[inicio:i]))
      inicio = i+1

    elif text[i] == "+":
      no.append(int(text[inicio:i]))
      inicio = i+1
      nos.append(no)
      no = []
  return nos[0], nos[1]

def relacionar_indice(no1, no2, lista_nos):
  if no1 not in lista_nos:
    lista_nos.append(no1)
  if no2 not in lista_nos:
    lista_nos.append(no2)

  return lista_nos.index(no1), lista_nos.index(no2)

def gerar_caminhos(grafo, inicio, destino, flare1, flare2, anterior=-1,caminho_atual=[]):
  global caminhos
  caminho_atual.append(inicio)

  if inicio == destino:
    caminhos.append(caminho_atual[:])
    if flare1 in caminho_atual:
      pos = caminho_atual.index(flare1)
      if pos - 1 >= 0:
        if caminho_atual[pos-1] == flare2:
          caminhos_flares.append(caminho_atual[:])
      if pos +1 < len(caminho_atual):
        if caminho_atual[pos+1] == flare2:
          caminhos_flares.append(caminho_atual[:])
  else:
    for vizinho in grafo[inicio]:
      if vizinho not in caminho_atual:
        gerar_caminhos(grafo, vizinho, destino, flare1, flare2, inicio, caminho_atual)

  caminho_atual.pop()

def calcular_tempo(caminho, grafo, is_flare = False,ponto1=[], ponto2=[]):
  tempo = 0
  tempo_flare = 0
  ativo1 = False
  ativo2 = False
  for i in range(1, len(caminho)):
    no1 = grafo[caminho[i-1]]
    no2 = grafo[caminho[i]]
    tempo += eval(f"abs({no2[0] - no1[0]}) + abs({no2[1] - no1[1]}) + abs({no2[2] - no1[2]})")

    if no1 == ponto1 or no2 == ponto1:
      ativo1 = True
    if no1 == ponto2 or no2 == ponto2:
      ativo2 = True
    if ativo1 and ativo2:
      tempo_flare = tempo
      ativo1, ativo2 = False, False
  
  if is_flare:
    return tempo, tempo_flare
  else:
    return tempo

caminhos = []
caminhos_flares = []

inp = input().split(", ")
q_eglus = int(inp[0])
q_arestas = int(inp[1])
eglus = []
grafo = []

for i in range(q_eglus):
  grafo.append([])

for i in range(q_arestas):
  aresta = input()
  eglu1 , eglu2 = separar_nos(aresta)
  indice1, indice2 = relacionar_indice(eglu1, eglu2, eglus)
  grafo[indice1].append(indice2)
  grafo[indice2].append(indice1)

tempo_maximo = int(input())

inp = input()
eglu_origem, eglu_seguro = separar_nos(inp)
indice_origem, indice_seguro = relacionar_indice(eglu_origem, eglu_seguro, eglus)

inp = input()
flare1, flare2 = separar_nos(inp)
indice_flare1, indice_flare2 = relacionar_indice(flare1, flare2, eglus)

gerar_caminhos(grafo, indice_origem, indice_seguro, indice_flare1, indice_flare2)
print(caminhos)
print(caminhos_flares)

tempo_menor_caminho = float("inf")
menor_caminho = []
for i in range(len(caminhos)):
  tempo = calcular_tempo(caminhos[i], eglus)
  if tempo < tempo_menor_caminho:
    tempo_menor_caminho = tempo
    menor_caminho = caminhos[i]

tempo_menor_flare = float("inf")
menor_flare = []
menor_tempo_ate_flare = 0
for i in range(len(caminhos_flares)):
  tempo, tempo_ate_flare = calcular_tempo(caminhos_flares[i], eglus, True, flare1, flare2)
  if tempo < tempo_menor_flare:
    tempo_menor_flare = tempo
    menor_tempo_ate_flare = tempo_ate_flare
    menor_flare = caminhos_flares[i]

print(tempo_menor_caminho)
print(tempo_menor_flare)
print(tempo_ate_flare)

if caminhos:
  if caminhos_flares:
    isDerrotados = False
    primeiro = True
    print(f"Puffle Flare capturado no momento: {menor_tempo_ate_flare} unidades de tempo")
    if tempo_maximo >= tempo_menor_caminho and tempo_maximo >= menor_tempo_ate_flare and tempo_maximo >= tempo_menor_flare:
      print("Missão bem sucedida!! Todos os puffles se salvaram.")
    elif tempo_maximo < tempo_menor_caminho or tempo_maximo < menor_tempo_ate_flare:
      isDerrotados = True
      print("Fomos derrotados... não foi possível escapar da erupção do vulcão!")
    elif tempo_maximo >= menor_tempo_ate_flare and tempo_maximo < tempo_menor_flare:
      primeiro = False
      print("O primeiro puffle não conseguiu chegar lá...")
      
    
    if not isDerrotados:
      if((not primeiro) or menor_caminho == menor_flare):
        print("Caminho comum entre todos os puffles:")
        for i in menor_caminho:
          if eglus[i] == eglu_seguro:
            print(f"{eglus[i]}", end=" ")
          else:
            print(f"{eglus[i]} -> ", end="")
        print(f"({tempo_menor_caminho} unidades de tempo)")
  else:
    print("Não há como escapar...")
else:
  print("Não há como escapar...")