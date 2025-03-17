# função secundário de calcular_sugestoes
def calcular_pontuacao(lista_palavras, palavra):
  pontuacao_total = 0
  for x in lista_palavras:
    t = min(len(x), len(palavra))

    for i in range(t):
      pontuacao_total += ord(x[i]) - ord(palavra[i])
  return pontuacao_total

def calcular_sugestoes(lista_palavras, dicionario):
  pontuacoes = [] 
  sugestoes = []
  lista_palavras = lista_palavras[-4:]
  for key in dicionario:
    pontuacao = calcular_pontuacao(lista_palavras, key)
    pontuacoes.append([key, pontuacao])
  
  pontuacoes = sorted(pontuacoes, key= lambda x: x[1])

  for x in pontuacoes:
    sugestoes.append(x[0])

  if len(sugestoes) > 4:
    return sugestoes[:4]
  return sugestoes

def add(lista, dicionario):
  dicionario[lista[0]] = lista[1]

def delete(chave, dicionario):
  dicionario.pop(chave)

def esc(lista_texto, lista_chaves, chave, dicionario):
  lista_texto.append(dicionario[chave])
  lista_chaves.append(chave)

def sel(lista_texto, lista_chaves, number, sugestoes, dicionario):
  lista_texto.append(dicionario[sugestoes[number-1]])
  lista_chaves.append(sugestoes[number-1])


inp = input()
traducoes = {}
texto = []
chaves = []
sugestoes = []
while inp != "*FIM":
  comando = inp[1:4]
  texto_passado = texto[:]
  sugestoes_passado = sugestoes[:]
  
  if comando == "ADD":
    lista = inp[5:].split(":")
    add(lista, traducoes)
  elif comando == "DEL":
    chave = inp[5:]
    delete(chave, traducoes)
  elif comando == "ESC":
    chave = inp[5:]
    esc(texto, chaves, chave, traducoes)
  else:
    n = int(inp[5:])
    sugestoes = calcular_sugestoes(chaves, traducoes)
    sel(texto, chaves, n, sugestoes, traducoes)

  sugestoes = calcular_sugestoes(chaves, traducoes)  
  if (texto_passado != texto or sugestoes_passado != sugestoes) and len(texto) > 0:
    frase1 = " ".join(texto)
    frase2 = f'({",".join(sugestoes)})'
    print(f"{frase1} {frase2}")
    print("------------------")
  
  inp = input()

print(" ".join(chaves))
print(" ". join(texto)) 