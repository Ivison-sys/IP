def escolher_combinacao(lista, k):
  maior = [[]]

  def backtrack(inicio, combinacao):
      
    if sum(combinacao[:]) == k and len(combinacao[:]) >= 4:  
      if len(combinacao[:]) > len(maior[0]):
        maior[0] = combinacao[:]
      
    for i in range(inicio, len(lista)):  
      combinacao.append(lista[i])  
      backtrack(i + 1, combinacao)
      combinacao.pop()

  backtrack(0, [])
  return maior[0]

def gerar_print(porta, seq):
  for i in range(len(seq)):
    seq[i] = str(seq[i])
  text = "".join(seq)
  text = text.replace("-", "")
  text = text.replace("0", "")
  print(f"A senha da porta {porta} é: {text}")

q_portas = int(input())

for i in range(q_portas):
  seq = input().split(", ")
  seq_tratado = []
  
  for num in seq:
    num = int(num)
    if num != 0:
      seq_tratado.append(num)
    
  k = int(input())
  melhor_seq = escolher_combinacao(seq_tratado, k)

  if(melhor_seq):
    gerar_print(i+1, melhor_seq)
  else:
    print("Não foi possível descobrir a senha dessa porta, Penguin Bond deve procurar outra entrada!")
    break