
nomeFeiticeiro = input()
vidaFeiticeiro = int(input())
ataqueFeiticeiro = int(input())
defesaFeiticeiro = int(input())
reversaoFeitico = input() == "True"
expansaoDominio = input() == "True"

vidaMahoraga = int(input())
ataqueMahoraga = int(input())
defesaMahoraga = int(input())

listaGolpes = input().split(", ")

if reversaoFeitico:
    print("Mesmo com a regeneração, ainda não vai ser fácil! Vamos nessa!")
else:
    print("Exorcizar o Mahoraga sem conseguir me curar vai ser bem difícil, mas eu não tenho escolha!")

adaptacoes_nome = []
adaptacoes_vezes = []


while vidaFeiticeiro > 0 and vidaMahoraga > 0:
    movimentoFeiticeiro = input()

    if movimentoFeiticeiro == "expansão de domínio":
        if expansaoDominio:
            if nomeFeiticeiro == "Satoru Gojo":
                print(f"Como assim o Mahoraga já se adaptou ao infinito de {nomeFeiticeiro}!?")
            else:
                print("Nem mesmo a sua adaptação pode derrotar isto!")
                print(f"{nomeFeiticeiro} conseguiu!")
                if nomeFeiticeiro == "Megumi Fushiguro":
                    print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado. Fushiguro é o primeiro usuário das dez sombras a conseguir esse feito!")
                elif nomeFeiticeiro == "Sukuna":
                    print("Você me mostrou o caminho, Megumi Fushiguro, e por isso eu sou grato!")
                else:
                    print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado, mas Fushiguro não participou da luta, logo o ritual foi anulado.")
                break
        else:
            print("Droga. Eu não aprendi a expandir meu domínio ainda!")
            continue

    if movimentoFeiticeiro == "black flash":
        print("As faíscas negras ignoram qualquer tipo de defesa! Toma essa Mahoraga!")
        dano = (ataqueFeiticeiro + 25) * 2
    elif movimentoFeiticeiro == "reversão de feitiço":
        if reversaoFeitico:
            vidaFeiticeiro += 25
            print("Eu posso continuar lutando mais um pouco...")
        continue
    elif movimentoFeiticeiro not in listaGolpes:
        print("Eu não sei que ideia é essa de tentar usar um golpe que eu não domino!")
        continue
    else:
        fator = 1
        if movimentoFeiticeiro in adaptacoes_nome:
            indice = adaptacoes_nome.index(movimentoFeiticeiro)
            adaptacoes_vezes[indice] += 1
            if adaptacoes_vezes[indice] == 2:
                print(f"A roda do Mahoraga girou pela segunda vez! {movimentoFeiticeiro} só vai funcionar mais uma vez")
                fator = 2
            elif adaptacoes_vezes[indice] == 3:
                print(f"A roda do Mahoraga girou pela terceira vez! {movimentoFeiticeiro} não vai funcionar mais")
                fator = 4
            else:
                print("Esse ataque é inútil! Melhor tentar outra coisa.")
                continue
        else:
            print(f"A roda do Mahoraga girou uma vez! {movimentoFeiticeiro} só vai funcionar mais duas vezes")
            adaptacoes_nome.append(movimentoFeiticeiro)
            adaptacoes_vezes.append(1)
        dano = max(((ataqueFeiticeiro - defesaMahoraga) + 25) // fator, 0)
    
    vidaMahoraga -= dano
    if vidaMahoraga <= 0:
        print(f"{nomeFeiticeiro} conseguiu!")
        if nomeFeiticeiro == "Megumi Fushiguro":
            print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado. Fushiguro é o primeiro usuário das dez sombras a conseguir esse feito!")
        elif nomeFeiticeiro == "Sukuna":
            print("Você me mostrou o caminho, Megumi Fushiguro, e por isso eu sou grato!")
        elif nomeFeiticeiro == "Satoru Gojo":
            print("Nem você sua adaptação é páreo para o infinito, queridinho.")
        else:
            print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado, mas Fushiguro não participou da luta, logo o ritual foi anulado.")
        break

    movimentoMahoraga = input()
    if movimentoMahoraga == "ataque":
        vidaFeiticeiro -= max(((ataqueMahoraga - defesaFeiticeiro) + 25), 0)
    elif movimentoMahoraga == "regeneração":
        vidaMahoraga += 25
        print("Ele está se regenerando.")
    elif movimentoMahoraga == "adaptação":
        if movimentoFeiticeiro == "black flash":
            print("Nem você vai conseguir se adaptar a isso, mahoraga!")
        elif movimentoFeiticeiro in adaptacoes_nome:
            indice = adaptacoes_nome.index(movimentoFeiticeiro)
            adaptacoes_vezes[indice] += 1
            if adaptacoes_vezes[indice] == 2:
                print(f"A roda do Mahoraga girou pela segunda vez! {movimentoFeiticeiro} só vai funcionar mais uma vez")
            elif adaptacoes_vezes[indice] == 3:
                print(f"A roda do Mahoraga girou pela terceira vez! {movimentoFeiticeiro} não vai funcionar mais")

    if vidaFeiticeiro <= 0:
        if nomeFeiticeiro == "Satoru Gojo":
            print("Magnífico, Satoru Gojo. Lembrarei de você enquanto eu durar nesta vida.")
        else:
            print(f"Parece que nem mesmo {nomeFeiticeiro} foi páreo contra o Mahoraga...")
        break
