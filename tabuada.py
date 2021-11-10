while True:
    erros = 0
    acertos = 0

    recebe_tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    respostas_tabuada = []
    resposta_usuario = []
    escolha = input('Qual tabuada gostaria de aprender [ 1 - 10 ] ou [0] para sair  ? :  ')

    if not escolha.isnumeric():
        print('DIGITE APENAS NUMEROS NESTE CAMPO')
    else:
        escolha = int(escolha)

    for i in range(0,11):
        if escolha == 0:
            break
        if escolha == 1:
            respostas_tabuada.append(recebe_tabuada[0] * i)
        if escolha == 2:
            respostas_tabuada.append(recebe_tabuada[1] * i)
        if escolha == 3:
            respostas_tabuada.append(recebe_tabuada[2] * i)
        if escolha == 4:
            respostas_tabuada.append(recebe_tabuada[3] * i)
        if escolha == 5:
            respostas_tabuada.append(recebe_tabuada[4] * i)
        if escolha == 6:
            respostas_tabuada.append(recebe_tabuada[5] * i)
        if escolha == 7:
            respostas_tabuada.append(recebe_tabuada[6] * i)
        if escolha == 8:
            respostas_tabuada.append(recebe_tabuada[7] * i)
        if escolha == 9:
            respostas_tabuada.append(recebe_tabuada[8] * i)
        if escolha == 10:
            respostas_tabuada.append(recebe_tabuada[9] * i)

        for i in range(0,11):
            recebe_resposta = input(f'Quanto que é {escolha} x {i} ? : ')

            if not recebe_resposta.isnumeric():
                print('Digite apenas numeros aqui !!')
            else:
                recebe_resposta = int(recebe_resposta)
            if recebe_resposta in respostas_tabuada:
                print(f' {escolha} x {i} = {recebe_resposta} !  Você acertou ! ')
                acertos += 1
            else:
                print(f' {escolha} x {i} = {recebe_resposta} !  Você ERROOOOOOOOU ! ')
                erros += 1
            print(f'Total de Erros = {erros}\t Total de Acertos = {acertos}')
        break