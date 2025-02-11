def adicionar(nome):
  for i in range(len(lista)):
    if lista[i] == "":
      lista[i] = nome
      return

def remover(nome):
  pos = 0
  for i in range(len(lista)):
    if lista[i] == nome:
      lista[i] = ""
      for z in range(i+1,len(lista)):
        lista[z-1] = lista[z]
  

def vitoria():
  isVitoria = True

  for x in lista:
    if x not in ["Jinx", "Vi", "Heimerdinger", "Ekko", "Caitlyn", "Jayce", "Viktor", "Silco", "Claggor", "Vander", "Mylo"]:
      isVitoria = False
  
  return isVitoria

q = int(input())
lista = [""] * q



while("" in lista):
  comando = input()
  nome = input()
  if comando == "Adiciona":
    adicionar(nome)
    print(f"Personagem {nome} adicionado")
  else:
    remover(nome)
    print(f"Personagem {nome} removido")

print("Lista final de personagens:")
for x in lista:
  print(x)

if(vitoria()):
  print("Parabéns!! Você conseguiu acertar todos os nomes.")
  print("UAUUU! Acho que estamos preparados para ver a segunda temporada.")
else:
  print("Infelizmente você perdeu...")
  print("Eita... Vamos precisar assistir novamente.")