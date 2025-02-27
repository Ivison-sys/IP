def gerar_combinacoes(lista, k):
    resultado = []


   
    def backtrack(inicio, combinacao, maior=[]):
        
        if sum(combinacao[:]) == k and len(combinacao[:]) >= 4:
            resultado.append(combinacao[:])  # Anota a combinação atual
            if len(combinacao[:]) > len(maior):
               maior = combinacao[:]
        
        for i in range(inicio, len(lista)):  
            combinacao.append(lista[i])  # Pega um brinquedo
            backtrack(i + 1, combinacao)  # Chama a brincadeira de novo
            combinacao.pop()  # Devolve o brinquedo para tentar outras combinações

    backtrack(0, [])  # Começa com a sacola vazia
    return resultado

q_portas = int(input())

for i in range(q_portas):
  seq = input().split(", ")
  seq_tratado = []
  
  for num in seq:
    num = int(num)
    if num != 0:
      seq_tratado.append(num)
    
  k = int(input())
  print(gerar_combinacoes(seq_tratado, k))
  

