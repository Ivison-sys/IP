def processar_cadeia(text):
  if text == "ε":
    return text
  
  lista = []
  for i in range(len(text)):
    if text[i] == "1" or text[i] == "0":
      char = int(text[i])
      lista.append(char)
    else:
      return lista
  return lista

def imprimir_conexoes(matriz):
  for z in range(len(matriz)):
    print(f"q{z+1}: {{0 -> {matriz[z][0]}, 1 -> {matriz[z][1]}}}")

def realizar_transicoes(conexoes, cadeia, estado_inicial):
  caminho = []
  estado_atual = estado_inicial
  indice_atual = int(estado_atual[1:]) - 1
  caminho.append(estado_atual)
  for bit in cadeia:
    estado_passado = estado_atual
    estado_atual = conexoes[indice_atual][bit]
    indice_atual = int(estado_atual[1]) - 1
    if estado_passado != estado_atual:
      caminho.append(estado_atual)
  estado_final = estado_atual

  return estado_final, caminho

def mensagem(aceitos, total):
  taxa = aceitos/total

  if taxa == 1:
    print("Sensacional :)! Com certeza vamos voltar pra casa com esse autômato, até Alan Turing teria inveja!")
  elif taxa >= 0.75:
    print("Show de bola! Se fizermos alguns ajustes nesse autômato, temos muitas chances de voltar pra casa!")
  elif taxa >= 0.5:
    print("Até que esse autômato da pro gasto, mas vamos precisar de uns bons ajustes…")
  elif taxa >= 25:
    print("Nossa, que situação horrível, não faço a mínima ideia de como concertar esse autômato")
  else:
    print("Nossas expectativas já eram baixas, mas não sabia que seria tão catastrófico assim :/")
  

n = int(input())
if n == 1:
  print("É… acho que não tem muito o que fazer com apenas uma dimensão, vou ter que me contentar com minha triste realidade :(")
else:
  cadeias_aceitas = 0
  estado_aceitacao = input()
  conexoes = [[]] * n
  for i in range(n):
    r = input()
    r = r.split(",")
    indice_q1 = r[0].index('q')
    indice_q2 = r[1].index('q') 
    conexoes[i] = [r[0][indice_q1:], r[1][indice_q2:]]
  q_cadeia = int(input())

  imprimir_conexoes(conexoes)

  for i in range(q_cadeia):
    cadeia = input()
    nova_cadeia = processar_cadeia(cadeia)
    is_valid = True
    estado_inicial = input()
    indice_inicial = int(estado_inicial[-1]) - 1

    if cadeia == "ε":
      if estado_aceitacao == estado_inicial:
        print("Caramba, essa cadeia é abençoada! Nem precisei trabalhar!")
        cadeias_aceitas += 1
      else:
        print("Nossa, que maldição! Nem começou e já deu errado…")
      print(f"{{{estado_inicial}}}")
      is_valid = False
    else:
      for z in range(len(cadeia)):
        transicao = cadeia[z]
        if transicao != '0' and transicao != "1":
          print(f"Só pode estar de brincadeira comigo! Como vou lidar com {transicao} dentro da máquina?")
          estado_final, caminho = realizar_transicoes(conexoes, nova_cadeia, estado_inicial)
          caminho.append("ERROR")
          caminho = " -> ".join(caminho)
          print(f"{{{caminho}}}")
          is_valid = False
          break
        
    if(is_valid):  
      
      estado_final, caminho = realizar_transicoes(conexoes, nova_cadeia, estado_inicial)

      if(estado_aceitacao == estado_final):
        print("Beleza! Após suar muito a cadeia foi aceita, o esforço ta sendo compensado!")
        cadeias_aceitas += 1
      else:
        print("Que tristeza, todo esse arrudeio pra nada…")
      caminho = " -> ".join(caminho)
      print(f"{{{caminho}}}")
      
  mensagem(cadeias_aceitas, q_cadeia)