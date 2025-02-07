print("QUE COMECEM AS BATALHAS")
inp = input().split(" ")

qAsh , qGary = int(inp[0]), int(inp[1])
pokemonsAsh = []
nomesAsh = []
pokemonsGary = []
nomesGary = []
vitoriasAsh = 0
vitoriasGary = 0
batalhas = [] 
if qAsh == qGary and qGary == 0:
  print("=============== ===============")
  print("Nenhuma batalha foi concluída.")
else:
  if qGary == 0:
    print("=============== ===============")
    print("Gary deixou seus pokemons descansando!")
    print("Ash é o grande vencedor!")
  elif qAsh == 0:
    print("=============== ===============")
    print("Ash deixou seus pokemons descansando!")
    print("Gary é o grande vencedor!")
  else:
    for x in range(int(qAsh)):
      pokemon = input().split(", ")
      pokemon[2], pokemon[3] = int(pokemon[2]), int(pokemon[3])
      pokemonsAsh.append(pokemon)   
      nomesAsh.append(pokemon[0])
    for x in range(int(qGary)):
      pokemon = input().split(", ")
      pokemon[2], pokemon[3] = int(pokemon[2]), int(pokemon[3])
      pokemonsGary.append(pokemon)
      nomesGary.append(pokemon[0])

    decisao = input()
    while decisao != "FIM DAS BATALHAS":
    
      inp = input().split(" ")
      sum = int(inp[0]) + int(inp[1])

      isFishtAsh = False

      if (sum % 2 == 0 and decisao == "par") or (sum % 2 == 1 and decisao == "ímpar"):
        isFishtAsh = True
    
      inp = input().split(" ")
      ativoAsh = inp[0]
      inp = input().split(" ")
      ativoGary = inp[0]

      indiceAsh = nomesAsh.index(ativoAsh)
      indiceGary = nomesGary.index(ativoGary)
    
      contador = 0
      while(pokemonsAsh[indiceAsh][2] > 0 and pokemonsGary[indiceGary][2] > 0):
        if isFishtAsh:
          if contador % 2 == 0:
            pokemonsGary[indiceGary][2] -= pokemonsAsh[indiceAsh][3] * 2
          else:
            pokemonsAsh[indiceAsh][2] -= pokemonsGary[indiceGary][3] * 2
        else:
          if contador % 2 == 1:
            pokemonsGary[indiceGary][2] -= pokemonsAsh[indiceAsh][3] * 2
          else:
            pokemonsAsh[indiceAsh][2] -= pokemonsGary[indiceGary][3] * 2
      
        contador+=1
      decisao = input()

      if pokemonsAsh[indiceAsh][2] < pokemonsGary[indiceGary][2]:    
        print(f"{pokemonsAsh[indiceAsh][0]} desmaiou e {pokemonsGary[indiceGary][0]} venceu esta luta") 
        p1, p2 = pokemonsAsh[indiceAsh][0], pokemonsGary[indiceGary][0].upper()
        batalhas.append([p1, p2])
        vitoriasGary+=1
        del pokemonsAsh[indiceAsh]
        del nomesAsh[indiceAsh]
      else:
        print(f"{pokemonsGary[indiceGary][0]} desmaiou e {pokemonsAsh[indiceAsh][0]} venceu esta luta")
        p1, p2 = pokemonsAsh[indiceAsh][0].upper(), pokemonsGary[indiceGary][0]
        batalhas.append([p1, p2])
        vitoriasAsh+=1
        del pokemonsGary[indiceGary]
        del nomesGary[indiceGary]

    print("=============== ===============")
    for i in range(len(batalhas)):
      print(f"{i+1}° Batalha: {batalhas[i][0]} vs {batalhas[i][1]}")

    if vitoriasAsh > vitoriasGary:
      print("Ash é o grande vencedor!")
    elif vitoriasGary > vitoriasAsh:
      print("Gary é o grande vencedor!")
    else:
      print("Depois de todas as batalhas, ainda terminou em empate!")