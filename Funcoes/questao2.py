def calcular_taxa(situacao_econimica, pop_zaun, pop_piltover):
  if situacao_econimica == "desastre":
    taxa_zaun = 0.9
  elif situacao_econimica == "crise":
    taxa_zaun = 0.8
  elif situacao_econimica == "critica":
    taxa_zaun = 0.7
  elif situacao_econimica == "normal":
    taxa_zaun = 0.6
  elif situacao_econimica == "tranquilo":
    taxa_zaun = 0.5
  else:
    taxa_zaun = pop_zaun / (pop_zaun + pop_piltover)
  
  taxa_piltover = 1 - taxa_zaun
  
  return taxa_zaun, taxa_piltover

def distribuir_recursos(taxa1, taxa2, total):
  recursos1 = total * taxa1
  recursos2 = total * taxa2

  return recursos1, recursos2

def mensagem(recursos1, recursos2):
  razao = recursos1/recursos2

  if razao >= 0.9:
    print("Zaun receberá uma bolada!!!")
  elif razao >= 0.8:
    print("Quase que Piltover ficava sem nada, pobrezinhos...")
  elif razao >= 0.7:
    print("O negócio vai ficar bom para Zaun hein.")
  elif razao >= 0.6:
    print("Parece que Zaun ainda precisa de ajuda.")
  elif razao >= 0.5:
    print("As coisas estão meio apertadas para Zaun.")
  else:
    print("A situação não está muito favorável para Zaun...")

  
total_recursos = int(input())
populacao_piltover = int(input())
populacao_zaun = int(input())
situacao_zaun = input()

taxa_zaun, taxa_piltover = calcular_taxa(situacao_zaun, populacao_zaun, populacao_piltover)
recursos_zaun, recursos_piltover = distribuir_recursos(taxa_zaun, taxa_piltover, total_recursos)
print(f"Foi decidido que será {(recursos_piltover):.1f} para Piltover e {(recursos_zaun):.1f} para Zaun!")

mensagem(recursos_zaun, recursos_piltover)