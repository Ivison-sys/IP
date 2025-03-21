def soma_letalidade(tabela_letalidade, arsenal_ataque, arsenal_defesa):
    # Equipamentos de ataque
    equipamento1_atq, equipamento2_atq, equipamento3_atq = arsenal_ataque['arma1'], arsenal_ataque['arma2'], arsenal_ataque['arma3']

    # Poder do primeiro equipamento de ataque
    if equipamento1_atq in tabela_letalidade:
        poder_equipamento1_atq = tabela_letalidade[equipamento1_atq]
    else:
        poder_equipamento1_atq = 0

    # Poder do segundo equipamento de ataque
    if equipamento2_atq in tabela_letalidade:
        poder_equipamento2_atq = tabela_letalidade[equipamento2_atq]
    else:
        poder_equipamento2_atq = 0

    # Poder do terceiro equipamento de ataque
    if equipamento3_atq in tabela_letalidade:
        poder_equipamento3_atq = tabela_letalidade[equipamento3_atq]
    else:
        poder_equipamento3_atq = 0

    # Calculando poder total de ataque
    poder_total_ataque = poder_equipamento1_atq + poder_equipamento2_atq + poder_equipamento3_atq

    # Equipamentos de defesa
    equipamento1_def, equipamento2_def, equipamento3_def = arsenal_defesa['arma1'], arsenal_defesa['arma2'], arsenal_defesa['arma3']

    # Poder do primeiro equipamento de defesa
    if equipamento1_def in tabela_letalidade:
        poder_equipamento1_def = tabela_letalidade[equipamento1_def]
    else:
        poder_equipamento1_def = 0

    # Poder do segundo equipamento de defesa
    if equipamento2_def in tabela_letalidade:
        poder_equipamento2_def = tabela_letalidade[equipamento2_def]
    else:
        poder_equipamento2_def = 0

    # Poder do terceiro equipamento de defesa
    if equipamento3_def in tabela_letalidade:
        poder_equipamento3_def = tabela_letalidade[equipamento3_def]
    else:
        poder_equipamento3_def = 0

    # Calculando poder total de defesa
    poder_total_defesa = poder_equipamento1_def + poder_equipamento2_def + poder_equipamento3_def

    return poder_total_ataque, poder_total_defesa

def batalha(recursos_ataque, recursos_defesa, recurso_alianca, recurso_coroa, alianca, coroa, alianca_forte, poder_total_ataque, poder_total_defesa, estado_ataque, estado_defesa):
    # Força de ataque com bônus
    if estado_ataque in alianca_forte:
        forca_ataque = ((recursos_ataque[estado_ataque]['dinheiro'] * 2) + (recursos_ataque[estado_ataque]['soldados'] * 4) + (poder_total_ataque * 4)) / 10
        forca_ataque += (forca_ataque * 10) / 100  # Bônus de 10% para estados fortes
    else:
        forca_ataque = ((recursos_ataque[estado_ataque]['dinheiro'] * 2) + (recursos_ataque[estado_ataque]['soldados'] * 4) + (poder_total_ataque * 4)) / 10

    # Força de defesa
    forca_defesa = ((recursos_defesa[estado_defesa]['dinheiro'] * 2) + (recursos_defesa[estado_defesa]['soldados'] * 4) + (poder_total_defesa * 4)) / 10

    # Determina o vencedor com base na força calculada
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

    # Atualiza contadores de vitórias e derrotas
    if vencedor in recurso_alianca['estados']:
        recurso_alianca['vitorias'] += 1
        recurso_coroa['derrotas'] += 1
    elif vencedor in recurso_coroa['estados']:
        recurso_coroa['vitorias'] += 1
        recurso_alianca['derrotas'] += 1

    # Reduz recursos dos participantes da batalha
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

def reintegrar_estado(estados_perdidos, vencedor, recurso_alianca, recurso_coroa):
    if estados_perdidos:
        estado_perdido, bloco_original = estados_perdidos[-1]
        bloco_vencedor = recurso_alianca if vencedor in recurso_alianca['estados'] else recurso_coroa

        if bloco_original == bloco_vencedor and estado_perdido not in bloco_vencedor['estados']:
            estados_perdidos.pop()
            bloco_vencedor['estados'].append(estado_perdido)

def arma():
    # Solicita e valida a escolha de arma do usuário
    arma_nova = input()
    if arma_nova not in tabela_letalidade:
        print("@ selecione uma arma válida! @")
        return arma()
    return arma_nova


def calcular_dano(bloco_perdedor, porcentagem):
    # Dano sofrido pelo bloco perdedor
    dano = bloco_perdedor['qtd_vida'] / porcentagem
    bloco_perdedor['qtd_vida'] = round(dano, 2)

def exibir_relatorio_batalha(alianca, coroa, recurso_alianca, recurso_coroa):
    # Relatório após cada batalha
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

# Estados e seus blocos
alianca = ['PE', 'PB', 'RN', 'CE', 'AL', 'BA']
coroa = ['SP', 'RJ', 'ES', 'PR', 'RS', 'MG']
alianca_forte = ('PE', 'PB', 'RN')

# Recursos dos blocos
recurso_alianca = {
    'qtd_vida': 1000, 'qtd_dinheiro': 20000,
    'qtd_soldados': 10000, 'estados': alianca,
    'vitorias': 0, 'derrotas': 0
}

recurso_coroa = {
    'qtd_vida': 1000, 'qtd_dinheiro': 20000,  
    'qtd_soldados': 10000, 'estados': coroa,
    'vitorias': 0, 'derrotas': 0
}

# Tabela de poder dos equipamentos
tabela_letalidade = {
    'Mosquete': 7000, 'Baioneta': 3000,
    'Canhão': 10000, 'Espada': 3500,
    'Pederneira': 5000
}

empate = True
ultimo_estado_perdido = None
recursos_ataque = {}
recursos_defesa = {}
estados_perdidos = []

for i in range(1, 4):
    if verificar_recursos(recurso_alianca, recurso_coroa):
        break

    # Coleta informações do estado atacante
    estado_ataque = input()
    while estado_ataque not in alianca and estado_ataque not in coroa:
        print('@ estado não encontrado ou não faz parte das regiões em guerra! @')
        estado_ataque = input()

    dinheiro_ataque = int(input())
    soldados_ataque = int(input())
    equipamento1_atq = arma()
    equipamento2_atq = arma()
    equipamento3_atq = arma()

    # Guarda informações do atacante
    recursos_ataque[estado_ataque] = {
        'nome': estado_ataque, 'dinheiro': dinheiro_ataque,
        'soldados': soldados_ataque, 'arma1': equipamento1_atq,
        'arma2': equipamento2_atq,  'arma3': equipamento3_atq
    }

    # Coleta informações do estado defensor
    estado_defesa = input()
    while estado_defesa not in alianca and estado_defesa not in coroa:
        print('@ escolha um estado válido para contra-atacar! @')
        estado_defesa = input()

    # Informa sobre vantagem de campo de batalha
    if estado_ataque in alianca_forte:
        print(f'o estado de {estado_ataque} ganhou 10% de força pois está lutando em um campo de batalha que lhe confere vantagem!')

    dinheiro_defesa = int(input())
    soldados_defesa = int(input())
    equipamento1_def = arma()
    equipamento2_def = arma()
    equipamento3_def = arma()

    # Guarda informações do defensor
    recursos_defesa[estado_defesa] = {
        'dinheiro': dinheiro_defesa, 'soldados': soldados_defesa,
        'arma1': equipamento1_def, 'arma2': equipamento2_def,
        'arma3': equipamento3_def
    }

    poder_total_ataque, poder_total_defesa = soma_letalidade(tabela_letalidade, recursos_ataque[estado_ataque], recursos_defesa[estado_defesa])

    # Realiza a batalha e obtém o resultado
    vencedor, perdedor, porcentagem = batalha(recursos_ataque, recursos_defesa, recurso_alianca, recurso_coroa, alianca, coroa, alianca_forte, poder_total_ataque, poder_total_defesa, estado_ataque, estado_defesa)

    # Resultado da batalha
    if vencedor:
        print(f'o estado de {vencedor} acaba de consagrar mais uma vitória e derrotou o estado de {perdedor} e agora o anexará!')
        if perdedor in recurso_coroa['estados']:
            anexar_estado(recurso_alianca, recurso_coroa, perdedor, estados_perdidos)
        elif perdedor in recurso_alianca['estados']:
            anexar_estado(recurso_coroa, recurso_alianca, perdedor, estados_perdidos)

        if estados_perdidos and estados_perdidos[-1][1] != vencedor:
            reintegrar_estado(estados_perdidos, vencedor, recurso_alianca, recurso_coroa)
        empate = False
    else:
        print('na batalha desta rodada houve um empate!!!')
        empate = True

    # Calcula dano ao bloco perdedor
    if vencedor in alianca:
        calcular_dano(recurso_coroa, porcentagem)
    elif vencedor in coroa:
        calcular_dano(recurso_alianca, porcentagem)

    if verificar_recursos(recurso_alianca, recurso_coroa):
        break

    exibir_relatorio_batalha(alianca, coroa, recurso_alianca, recurso_coroa)

    # Mostra estados anexados se houver
    if empate == False:
        bloco = "coroa" if estados_perdidos[0][1] == recurso_alianca else "alianca"
        estados_perdidos_str = [estado[0] for estado in estados_perdidos]
        print(f"a {bloco} anexou o(s) seguinte(s) estado(s): {','.join(estados_perdidos_str)}")

# Determina o vencedor final da guerra
if recurso_alianca['qtd_vida'] > recurso_coroa['qtd_vida']:
    print('VIVA! A Revolução vingou, Pernambuco se uniu aos outros estados do Nordeste e ao Estado de Minas Gerais e criou a república Pernambucana!')
elif recurso_alianca['qtd_vida'] < recurso_coroa['qtd_vida']:
    print('infelizmente o sonho acabou! A revolução falhou o império Português venceu!')
else:
    print('a guerra foi em vão! As coisas ficarão como estão!')