def explorar(trilha, indice= 0,energia= 4, mochila= [0,0]):
  if energia <= 0 or indice >= len(trilha):
    if energia <= 0:
      print("Ah, cansei. Vou descansar.")
    return mochila
  
  if isinstance(trilha[indice], int):
    mochila[0] += trilha[indice]
  elif trilha[indice] != "X":
    mochila[1] += 1
    print(f"Oba! Encontrei um {trilha[indice]} 🐧🎉")
    energia += 2

  energia -= 1

  return explorar(trilha, indice+1, energia, mochila)

inp = input().split(', ')
seq = []

for x in inp:
  if x.isnumeric():
    x = int(x)
  seq.append(x)

itens = explorar(seq)

if itens == [0,0]:
  print("Essa caminhada não foi nada produtiva. É melhor ir pescar.")
else:
  if itens[0] > 0 and itens[1] == 0:
    print(f"Estamos ricos!! Encontrei {itens[0]} moedas.")
  elif itens[0] == 0 and itens[1] > 0:
    print(f"Dinheiro? Não temos. Mas temos {itens[1]} itens raros.")
  else:
    print(f"Quem diria!! {itens[0]} moedas e {itens[1]} itens raros. Hoje eu mereço bolo, não aqueles puffitos de sempre.")