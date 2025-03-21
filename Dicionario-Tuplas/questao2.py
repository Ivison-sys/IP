def calcular_pontuacao(dicionario):
  pontos = 0

  if dicionario["aprovacao"] == "APROVA":
    pontos += 5
  elif dicionario["aprovacao"] == "TANTO FAZ":
    pontos += 2

  if dicionario["orcamento"] > 1000000:
    pontos += 3
  elif dicionario["orcamento"] >= 500000:
    pontos += 4
  else:
    pontos += 5
  
  if dicionario["categoria"] == "Defesa":
    pontos += 5
  elif dicionario["categoria"] == "Ciencia":
    pontos += 4
  elif dicionario["categoria"] == "Lazer":
    pontos += 3

  return pontos
  
locais = []
print()
for x in range(3):
  estabelecimento = {}
  estabelecimento["nome"] = input()
  estabelecimento["aprovacao"] = input()
  estabelecimento["orcamento"] = int(input())
  estabelecimento["categoria"] = input()
  estabelecimento["pontuacao"] = calcular_pontuacao(estabelecimento)
  locais.append(estabelecimento)

locais = sorted(locais, key= lambda x: [-x["pontuacao"], x["orcamento"]])
posicoes = ("primeiro", "segundo", "terceiro")

for i in range(3):
  print(f"O {posicoes[i]} estabelecimento construído deve ser {locais[i]['nome']}, com um orçamento de {locais[i]['orcamento']} e com a funcionalidade de {locais[i]['categoria']}.")

for i in range(3):
  categoria = locais[i]['categoria']

  if categoria == "Defesa":
    print("Oba, agora a cidade estará mais segura.")
  elif categoria == "Ciencia":
    print("Agora sim vou poder ter uma vida intelectual.")
  elif categoria == "Lazer":
    print("Vamooo, agora posso curtir meu final de semana descansando na bela cidade do Recife.")