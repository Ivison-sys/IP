def tratar_expressao(text):
  equacao = []
  text += "-"

  inicio = 0
  for i in range(len(text)):
    if (text[i] == "+" or text[i] == "-") and i > 0:
      equacao.append(text[inicio:i])
      inicio = i
  return equacao

def derivar(expressao, grau):
  test = [0] * len(expressao)
  if grau == 0:
    return expressao
  if expressao == test:
    return -1
  
  

  for i in range(len(expressao)):
    if expressao[i] == 0:
      continue
    if expressao[i] != 0:
      if "x" not in expressao[i]:
        expressao[i] = 0
      elif expressao[i][-1] == "x":
        termos = expressao[i].split("x")
        if termos[0] in ["", "+", "-"]:
          expressao[i] = 1
        else:
          expressao[i] = termos[0]
      else:
        termos = expressao[i].split("^")

        if termos[0] == "x":
          base = 1
        else:
          base = int(termos[0].replace("x", ""))

        expoente = int(termos[1])
        if expoente > 2:
          expressao[i] = f"{base*expoente}x^{expoente-1}"
        else: 
          expressao[i] = f"{base*expoente}x"

  return derivar(expressao, grau-1) 



inp = input()
grau = int(input())

equacao = tratar_expressao(inp)
equacao = derivar(equacao, grau)

print(f"A derivada de ordem {grau} da função {inp} é:")

exemplo = []
if equacao == -1:
  print("0")
else:
  for i in range(len(equacao)):
    if equacao != 0:
      termo = str(equacao[i])
      if i > 0 and termo[0] not in ["-", "+"]:
        termo = "+" + termo
      if termo == "+0" or termo == "-0":
        termo = ""
      if termo != 0:
        print(termo, end='')  


