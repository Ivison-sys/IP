def calcularConsumo(h,p,i):
  energiaInicial = h*p
  return energiaInicial + (energiaInicial * i /100)
def calcularGastos(consumo, g):
  return consumo * g

qMaquinas = int(input())
listaGastos = []

for x in range(qMaquinas):
  h = int(input())
  p = float(input())
  i = int(input())
  g = float(input())

  consumo = calcularConsumo(h,p,i)
  gasto = calcularGastos(consumo, g)
  listaGastos.append(gasto)
  if consumo == 0:
    print("Parece que essa coisa nem ao menos funciona")
  elif consumo <= 100:
    print(f"Temos aqui uma máquina formidável, seu consumo de energia é {consumo:.2f}")
  elif consumo <= 300:
    print(f"Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {consumo:.2f}")
  else:
    print("Você se importaria de jogar seus explosivos em qualquer outro lugar?")

print(f"Os gastos totais com as maquinas foi de {sum(listaGastos):.2f}")
print(f"A máquina mais cara gasta um total de {max(listaGastos):.2f} para os cofres de Piltover")