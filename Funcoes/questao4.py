def descriptografar(palavra, num):
  texto = ""
  for i in range(len(palavra)):
    indice = alfabeto.index(palavra[i])

    if indice - num < 0:
      letra = 26 + (indice - num)
    else:
      letra = indice - num
    
    texto += alfabeto[letra]
  return texto

def calcular_dano(precisao, poder_explosao, resistencia, palavra):
  if palavra == "ALTO":
    fator = 2
  elif palavra == "MEDIO":
    fator = 1.5
  else:
    fator = 1
  
  return round(precisao * (poder_explosao / resistencia) * fator)

def ordenarAtaques(lista_ataques, lista_danos):
  danos_ordenados = sorted(lista_danos, reverse=True)
  lista = []
  for dano in danos_ordenados:
    indice = lista_danos.index(dano)
    lista.append(lista_ataques[indice])
  return lista

n_ataques = int(input())
alfabeto = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if n_ataques == 0:
  print("Piltover em paz... por enquanto.")

else:
  ataques = []
  danos = []
  for i in range(n_ataques):
    ataque = input().split(', ')
    palavra = descriptografar(ataque[4], int(ataque[5]))
    dano = calcular_dano(int(ataque[1]), int(ataque[3]),int(ataque[2]), palavra)
    danos.append(dano)
    ataques.append([ataque[0], dano])
    
    ataques = ordenarAtaques(ataques, danos)

    print(f"Decifrando: {palavra}")
    print(f"{ataque[0]}: {dano} de dano calculado.")

    if dano >= 100:
      print(f"{ataque[0]} será destruído!")
    else:
      print(f"{ataque[0]} resistirá ao ataque.")
    print()
    
  print("Prioridade de ataques:")

  for at in ataques:
    print(f"{at[0]} - {at[1]} de dano")