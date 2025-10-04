'''resposta = input(
    
    """

        Seja bem-vindo ao banco Chaotix, oque gostaria de fazer hoje?
    
        [1] Depositar
        [2] Sacar
        [3] Ver extrato
    
        Insira a o número da sua resposta:
    """
    
    
    )

saldo = 0


while True:

    if resposta == "1":
        novo_saldo = int(input(f"Seu saldo atual é de R${saldo} gostaria de depositar?"))
        if novo_saldo <= 500:
            saldo = saldo + novo_saldo
            print(f"Valor adicionado com sucesso! Seu novo saldo é de R${saldo}.")
        else:
            print("Valor invcalido! São permitidos apenas valores abaixo de 500 reais!")
    if resposta == "2":
       print("sim")
    elif resposta == "3":
       print("sim")
    else:
       print("Resposta inválida")

"        print(f"Seu saldo atual é de R${saldo:.2f}! Você pode depositar mais ao volta no menu!")
        escolha = input(
    
    """
        Seja bem-vindo ao banco Chaotix, oque gostaria de fazer hoje?
    
        [1] Depositar
        [2] Sacar
        [3] Ver extrato
        [0] Sair
    
        Insira o número da sua resposta:
    """
    )
    '''
'''
        print(f"""Tuas movimentaçoes até agora foram:
            {movimentacoes}""")
            
        while True:
            voltar_menu =input(""" 
            Gostaria de voltar para a tela inicial?
            [S]/[N]
            """)
            if voltar_menu == "S":
                escolha = input(
    
    """
        Seja bem-vindo ao banco Chaotix, oque gostaria de fazer hoje?
    
        [1] Depositar
        [2] Sacar
        [3] Ver extrato
        [0] Sair
    
        Insira o número da sua resposta:
    """
    )
                break
            elif voltar_menu == "N":
                print("Agradecemos por ecolher os bancos Chaotix! Volte sempre!")
                exit()
            else:
                print("Resposta inválida! Tente novamente!")
                break
'''