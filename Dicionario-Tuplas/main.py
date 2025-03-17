def adicao_letalidade(letalidade, recursos_ataque, recursos_defesa):
    arma1_atq, arma2_atq, arma3_atq = recursos_ataque['arma1'], recursos_ataque['arma2'], recursos_ataque['arma3']
   
    if arma1_atq in letalidade:
        letalidade_arma1_atq = letalidade[arma1_atq]
    else:
        letalidade_arma1_atq = 0

    if arma2_atq in letalidade:
        letalidade_arma2_atq = letalidade[arma2_atq]
    else:
        letalidade_arma2_atq = 0

    if arma3_atq in letalidade:
        letalidade_arma3_atq = letalidade[arma3_atq]
    else:
        letalidade_arma3_atq = 0

    letalidade_ataque = letalidade_arma1_atq + letalidade_arma2_atq + letalidade_arma3_atq

    arma1_def, arma2_def, arma3_def = recursos_defesa['arma1'], recursos_defesa['arma2'], recursos_defesa['arma3']
   
    if arma1_def in letalidade:
        letalidade_arma1_def = letalidade[arma1_def]
    else:
        letalidade_arma1_def = 0

    if arma2_def in letalidade:
        letalidade_arma2_def = letalidade[arma2_def]
    else:
        letalidade_arma2_def = 0

    if arma3_def in letalidade:
        letalidade_arma3_def = letalidade[arma3_def]
    else:
        letalidade_arma3_def = 0

    letalidade_defesa = letalidade_arma1_def + letalidade_arma2_def + letalidade_arma3_def

    return letalidade_ataque, letalidade_defesa

def batalha(recursos_ataque, recursos_defesa, recurso_coroa, alianca, alianca_forte, letalidade_ataque, letalidade_defesa, estado_ataque, estado_defesa):

    if estado_ataque in alianca_forte:
        forca_ataque = ((recursos_ataque[estado_ataque]['dinheiro'] * 2) + (recursos_ataque[estado_ataque]['soldados'] * 4) + (letalidade_ataque * 4)) / 10
        forca_ataque += (forca_ataque * 10) / 100  
    else:
        forca_ataque = ((recursos_ataque[estado_ataque]['dinheiro'] * 2) + (recursos_ataque[estado_ataque]['soldados'] * 4) + (letalidade_ataque * 4)) / 10

    forca_defesa = ((recursos_defesa[estado_defesa]['dinheiro'] * 2) + (recursos_defesa[estado_defesa]['soldados'] * 4) + (letalidade_defesa * 4)) / 10
   
    if forca_ataque > forca_defesa:
        vencedor = estado_ataque
        perdedor = estado_defesa
        porcentagem = (forca_ataque / forca_defesa)

    elif forca_defesa > forca_ataque:
        vencedor = estado_defesa
        perdedor = estado_ataque
        porcentagem = (forca_defesa / forca_ataque)
    else:
        vencedor = None
        perdedor = None
        porcentagem = 0

    if vencedor in recurso_alianca['estados']:
        recurso_alianca['vitorias'] += 1
        recurso_coroa['derrotas'] += 1  # Adiciona derrota ao oponente
    elif vencedor in recurso_coroa['estados']:
        recurso_coroa['vitorias'] += 1
        recurso_alianca['derrotas'] += 1
    if estado_ataque in alianca:
        recurso_alianca['qtd_soldados'] -= recursos_ataque[estado_ataque]['soldados']
    else:
        recurso_coroa['qtd_soldados'] -= recursos_ataque[estado_ataque]['soldados']
   
    if estado_ataque in alianca:
        recurso_alianca['qtd_dinheiro'] -= recursos_ataque[estado_ataque]['dinheiro']
    else:
        recurso_coroa['qtd_dinheiro'] -= recursos_ataque[estado_ataque]['dinheiro']
   
    if estado_defesa in alianca:
        recurso_alianca['qtd_soldados'] -= recursos_defesa[estado_defesa]['soldados']
    else:
        recurso_coroa['qtd_soldados'] -= recursos_defesa[estado_defesa]['soldados']
   
    if estado_defesa in alianca:
        recurso_alianca['qtd_dinheiro'] -= recursos_defesa[estado_defesa]['dinheiro']
    else:
        recurso_coroa['qtd_dinheiro'] -= recursos_defesa[estado_defesa]['dinheiro']    
       
    return vencedor, perdedor, porcentagem

def anexar_estado(bloco_perdedor, estado_perdedor, estados_perdidos):
    if estado_perdedor in bloco_perdedor['estados']:
        bloco_perdedor['estados'].remove(estado_perdedor)
        estados_perdidos.append((estado_perdedor, bloco_perdedor))  
   

def armazenar_estados(estados_perdidos, vencedor, recurso_alianca, recurso_coroa):
    if estados_perdidos:
        estado_perdido, bloco_original = estados_perdidos[-1]  
        bloco_vencedor = recurso_alianca if vencedor in recurso_alianca['estados'] else recurso_coroa

        if bloco_original == bloco_vencedor and estado_perdido not in bloco_vencedor['estados']:
            estados_perdidos.pop()
            bloco_vencedor['estados'].append(estado_perdido)
def arma():
    arma_nova = input()
    if arma_nova not in letalidade:
        print("@ selecione uma arma válida! @")
        return arma()
    return arma_nova


def calcular_dano(bloco_perdedor, porcentagem):
    dano = bloco_perdedor['qtd_vida'] / porcentagem
    bloco_perdedor['qtd_vida'] = round(dano, 2)

def printar_relatoria(recurso_alianca, recurso_coroa):
    print(f"=== resultado da {i}º batalha ===\n")
   
    print(f"número de estados da aliança: {len(recurso_alianca['estados'])}")
    print(f"vitorias: {recurso_alianca['vitorias']}")
    print(f"derrotas: {recurso_alianca['derrotas']}")
    print(f"riqueza: {recurso_alianca['qtd_dinheiro']:.1f}")
    print(f"nº soldados: {recurso_alianca['qtd_soldados']}")
    print(f"pontos de vida: {recurso_alianca['qtd_vida']:.2f}")
   
    print(f"\nnúmero de estados da coroa: {len(recurso_coroa['estados'])}")
    print(f"vitórias: {recurso_coroa['vitorias']}")
    print(f"derrotas: {recurso_coroa['derrotas']}")
    print(f"riqueza: {recurso_coroa['qtd_dinheiro']:.1f}")
    print(f"nº soldados: {recurso_coroa['qtd_soldados']}")
    print(f"pontos de vida: {recurso_coroa['qtd_vida']:.2f}\n")
   

def verificar_recursos(recurso_alianca, recurso_coroa):
    if recurso_alianca['qtd_dinheiro'] <= 0 or recurso_alianca['qtd_soldados'] <= 0 or recurso_alianca['qtd_vida'] <= 0:
        print("a alianca não possui recursos suficientes para continuar com a guerra! O vencedor será aquele que tiver o maior ponto de vida")
        return True
    if recurso_coroa['qtd_dinheiro'] <= 0 or recurso_coroa['qtd_soldados'] <= 0 or recurso_coroa['qtd_vida'] <= 0:
        print("a coroa não possui recursos suficientes para continuar com a guerra! O vencedor será aquele que tiver o maior ponto de vida")
        return True
   
alianca = ['PE', 'PB', 'RN', 'CE', 'AL', 'BA']
coroa = ['SP', 'RJ', 'ES', 'PR', 'RS', 'MG']
alianca_forte = ('PE', 'PB', 'RN')

recursos_alianca = {
    'qtd_vida': 1000,
    'qtd_dinheiro': 20000,
    'qtd_soldados': 10000,
    'estados': alianca,
    'vitorias': 0,
    'derrotas': 0
}

recurso_coroa = {
    'qtd_vida': 1000,
    'qtd_dinheiro': 20000,
    'qtd_soldados': 10000,
    'estados': coroa,
    'vitorias': 0,
    'derrotas': 0
}

letalidade = {
    'Mosquete': 7000,
    'Baioneta': 3000,
    'Canhão': 10000,
    'Espada': 3500,
    'Pederneira': 5000
}
empate = True
ultimo_estado_perdido = None
recursos_ataque = {}
recursos_defesa = {}
estados_perdidos = []
for i in range(1, 4):
    if verificar_recursos(recursos_alianca, recurso_coroa):
        break
    estado_ataque = input()
    while estado_ataque not in alianca and estado_ataque not in coroa:
        print('@ estado não encontrado ou não faz parte das regiões em guerra! @')
        estado_ataque = input()
   
    dinheiro_ataque = int(input())
    soldados_ataque = int(input())
    arma1_ataque = arma()
    arma2_ataque = arma()
    arma3_ataque = arma()
   
    recursos_ataque[estado_ataque] = {
        'nome': estado_ataque,
        'dinheiro': dinheiro_ataque,
        'soldados': soldados_ataque,
        'arma1': arma1_ataque,
        'arma2': arma2_ataque,
        'arma3': arma3_ataque
    }
   
    estado_defesa = input()
    while estado_defesa not in alianca and estado_defesa not in coroa:
        print('@ escolha um estado válido para contra-atacar! @')
        estado_defesa = input()
   
    if estado_ataque in alianca_forte:
        print(f'o estado de {estado_ataque} ganhou 10% de força pois está lutando em um campo de batalha que lhe confere vantagem!')
   
    dinheiro_defesa = int(input())
    soldados_defesa = int(input())
    arma1_defesa = arma()
    arma2_defesa = arma()
    arma3_defesa = arma()
   
    recursos_defesa[estado_defesa] = {
        'dinheiro': dinheiro_defesa,
        'soldados': soldados_defesa,
        'arma1': arma1_defesa,
        'arma2': arma2_defesa,
        'arma3': arma3_defesa
    }

    letalidade_ataque, letalidade_defesa = adicao_letalidade(letalidade, recursos_ataque[estado_ataque], recursos_defesa[estado_defesa])
   
    vencedor, perdedor, porcentagem = batalha(recursos_ataque, recursos_defesa, recursos_alianca, recurso_coroa, alianca, coroa, alianca_forte, letalidade_ataque, letalidade_defesa, estado_ataque, estado_defesa)
   
    if vencedor:
        print(f'o estado de {vencedor} acaba de consagrar mais uma vitória e derrotou o estado de {perdedor} e agora o anexará!')
        if perdedor in recurso_coroa['estados']:  
            anexar_estado(recursos_alianca, recurso_coroa, perdedor, estados_perdidos)
        elif perdedor in recursos_alianca['estados']:  
            anexar_estado(recurso_coroa, recursos_alianca, perdedor, estados_perdidos)
       
        if estados_perdidos and estados_perdidos[-1][1] != vencedor:    
            armazenar_estados(estados_perdidos, vencedor, recursos_alianca, recurso_coroa)
        empate = False
    else:
        print('na batalha desta rodada houve um empate!!!')
        empate = True

    if vencedor in alianca:
        calcular_dano(recurso_coroa, porcentagem)  
    elif vencedor in coroa:
        calcular_dano(recursos_alianca, porcentagem)
    if verificar_recursos(recursos_alianca, recurso_coroa):
        break
   
    printar_relatoria(alianca, coroa, recursos_alianca, recurso_coroa)
    if empate == False:        
        bloco = "coroa" if estados_perdidos[0][1] == recursos_alianca else "alianca"
        estados_perdidos_str = [estado[0] for estado in estados_perdidos]
        print(f"a {bloco} anexou o(s) seguinte(s) estado(s): {','.join(estados_perdidos_str)}")


if recursos_alianca['qtd_vida'] > recurso_coroa['qtd_vida']:
    print('VIVA! A Revolução vingou, Pernambuco se uniu aos outros estados do Nordeste e ao Estado de Minas Gerais e criou a república Pernambucana!')
elif recursos_alianca['qtd_vida'] < recurso_coroa['qtd_vida']:
    print('infelizmente o sonho acabou! A revolução falhou o império Português venceu!')
else:
  print('a guerra foi em vão! As coisas ficarão como estão!') 