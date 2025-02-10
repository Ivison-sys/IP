def calcular_taxa(situacao_econimica, pop_zaun, pop_piltover):
  if situacao_econimica == "desastre":
    taxa_zaun = 0.9
    taxa_piltover = 1 - taxa_zaun
  elif situacao_econimica == "crise":
    taxa_zaun = 0.8
    taxa_piltover = 1 - taxa_zaun
  elif situacao_econimica == "critica":
    taxa_zaun = 0.7
    taxa_piltover = 1 - taxa_zaun
  elif situacao_econimica == "normal":
    taxa_zaun = 0.6
    taxa_piltover = 1 - taxa_zaun
  elif situacao_econimica == "tranquilo":
    taxa_zaun = 0.5
    taxa_piltover = 1 - taxa_zaun
  else:
    taxa_zaun = pop_zaun / (pop_zaun + pop_piltover)
    taxa_piltover = 1 - taxa_zaun
  
  return taxa_zaun, taxa_piltover

def distribuir_recursos(taxa_zuan, taxa_piltover)
total_recursos = int(input())
populacao_piltover = int(input())
populacao_zaun = int(input())
situacao_zaun = input()

taxa_zaun, taxa_piltover = calcular_taxa(situacao_zaun)

print(f"Foi decidido que será {recursos_piltover} para Piltover e {recursos_zaun} para Zaun!Foi decidido que será {(total_recursos * taxa_piltover):.2f} para Piltover e {(total_recursos * taxa_zaun):.2f} para Zaun!")

