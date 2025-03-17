def calcular_pontuacao(lista_palavras, palavra):
  pontuacao_total = 0
  for x in lista_palavras:
    t = min(len(x), len(palavra))

    for i in range(t):
      pontuacao_total += ord(x[i]) - ord(palavra[i])
  return pontuacao_total

print(calcular_pontuacao(["nasz"], "população"))