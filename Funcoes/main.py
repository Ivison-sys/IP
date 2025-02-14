inimigo = input().split(' - ')
nome = inimigo[0]
vida = int(inimigo[1])
distancia = int(inimigo[2])
velocidade = int(inimigo[3])
defesa = inimigo[4] == "1"
ativo = False
lancar = True

print(f"Andando pelas ruas de Zaun, jinx dá de cara com um {nome} e agora vão lutar.")

def zap(vida):
  global ativo
  global defesa
  ativo = True
  if not defesa:
    vida -= 5
    print("Você foi zapeado hahaha.")
  else:
    print("Ele está com defesa e está muito perto!")
  return vida

def powPow(vida):
  print("Jinx vai encher esse cara de buracos agora.")
  return vida - 15

def fishBones(vida):
  global defesa
  if defesa:
    print("A defesa dele foi destruída com o poder da Fishbones!")
    defesa = False
    return vida
  print("Vamos derretê-lo com a Fishbones!") 
  return vida - 30
 
def lancaMissil(vida):
  global lancar
  if lancar:
    lancar = False
    print("Ele vai ser transformado em cinzas pelo SUPER MÍSSIL!")
    return vida - 100
 

def escolhaArma(vida, distancia, defe):
  if defe and distancia >= 30:
    vida = fishBones(vida)
  elif not defe:
    if distancia >= 50 and lancar:
      vida = lancaMissil(vida)  
    elif distancia >= 30:

      vida = fishBones(vida)
    elif distancia >= 15:
      vida = powPow(vida)
    else:
      vida = zap(vida)
  else:
    vida = zap(vida)
    
  return vida

while distancia > 0 and vida > 0:
  vida = escolhaArma(vida, distancia, defesa)
  if velocidade <= 1:
    ativo = False
  if ativo:
    velocidade -= 1
  distancia -= velocidade

if distancia > 0:
  print("Ninguem é capaz de derrotar a Jinx!!!")
else:
  print("Ah não, A Jinx foi PEGA!")