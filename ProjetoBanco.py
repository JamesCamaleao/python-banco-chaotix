saldo = 0
numero_saques = 0
adiciona_saldo = 0
remove_saldo = 0
movimentacoes = []
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

while True:

    if escolha == "1":
        adiciona_saldo = float(input(f"Seu saldo atual é de R${saldo:.2f} gostaria de depositar?"))
        saldo = saldo + adiciona_saldo
        movimentacoes.append(f"Depósito: R$ {adiciona_saldo:.2f}")
        print(f"Seu novo saldo é de R${saldo:.2f}.")
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

    if escolha == "2":
        remove_saldo = float(input(f"""Seu saldo atual é de R${saldo:.2f} gostaria de sacar? 
        Obs: Você não pode sacar mais de R$500 por vez e nem mais de três vezes ao dia."""))
        
        if remove_saldo > 500:
            print("Saque invalido! Seu limite é de R$500.")            

        elif saldo < remove_saldo:
            print("Você não pode sacar mais do que tem na sua conta!")

        elif numero_saques >= 3:
            print("Você não pode sacar mais de três vezes ao dia!")
    
        else:
            saldo = saldo - remove_saldo
            movimentacoes.append(f"Saque: R$ {remove_saldo:.2f}")
            numero_saques += 1
            print (f"Seu novo saldo é de R${saldo:.2f}.")
            
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
        
    elif escolha == "3":
            
        if not movimentacoes:
            print("Não foram realizadas movimentações na tua conta!")
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

                elif voltar_menu == "N":
                    print("Agradecemos por ecolher os bancos Chaotix! Volte sempre!")
                    exit()
                else:
                    print("Resposta inválida! Tente novamente!")
                    break
        else:
            print("Suas movimentações realizadas até agora foram:")
            for m in movimentacoes:
                print(m)
            print(f"Seu saldo é de R${saldo:.2f}.")

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

                elif voltar_menu == "N":
                    print("Agradecemos por ecolher os bancos Chaotix! Volte sempre!")
                    exit()
                else:
                    print("Resposta inválida! Tente novamente!")
                    break

    elif escolha == "0":
        print("Agradecemos por ecolher os bancos Chaotix! Volte sempre!")
        exit()
    
    else:
        print("Desculpe, sua resposta é inválida! Tente novamente!")
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
