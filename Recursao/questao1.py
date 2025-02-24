def verificar(num, fib, ant):
  # caso base
  if num == fib or num in [0,1]:
    return True, [fib, ant]
  elif num < fib:
    return False, [fib, ant]

  fib, ant = fib + ant, fib
    
  return verificar(num, fib, ant) 

q_numbers = int(input())
numbers = []
certos = []

for i in range(q_numbers):
  num = int(input())
  numbers.append(num)

numbers = sorted(numbers)
seq = [2,1]

for number in numbers:
  is_fib, seq = verificar(number, seq[0], seq[1])
  
  if is_fib:
    certos.append(str(number))
  
print(f"Contei um total de {len(certos)} números que estão na sequência de penguinacci!") 

if len(certos) == q_numbers:
  print(f"Boa, Paulo! Todos esses números fazem parte da sequência de penguinacci.")
elif (len(certos)):
  print(f"Eita, nem todos que você falou fazem parte da sequência de penguinacci. Os que fazem parte são:")
  print(", ".join(certos))
else:
  print("Acho que é melhor revisar a teoria um pouco...")