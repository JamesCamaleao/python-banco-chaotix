Python-Banco_Chaotix

Banco Chaotix

Este código foi feito como uma atividade do programa “Vivo - Python AI Backend Developer, promovido pela DIO”, o desafio consiste em criar um sistema que se imita um banco, o trabalho final deve permitir o usuário de realizar o depósito, saque e verificar o extrato. Além disso, o projeto exige a criação de funções usando diferentes modos de passagem de argumentos (somente posicional, somente nomeado e misto), e também a implementação do cadastro de usuários e contas bancárias.

Menu: Um menu de escolhas vai aparecer e o utilizador deve responder qual parte do programa gostaria de usar agora, as opções são:

Cadastro de Usuário: O programa deve permitir que o usuário cadastre um novo cliente informando nome, data de nascimento, CPF e endereço. O sistema deve garantir que não existam dois cadastros com o mesmo CPF.

Cadastro de Conta Bancária: Depois de criar um usuário, o programa permite criar uma conta associada a ele. Cada conta tem número sequencial, agência fixa “0001” e pertence a um único usuário.

Depósito: O usuário deve ser capaz de efetuar um depósito que vai ser armazenado em uma variável e ser exibido mais tarde no campo de extrato. Esta operação é feita através da função de depósito, que deve receber apenas argumentos posicionais.

Saque: O banco deve permitir que o usuário faça apenas 3 saques por dia e com o valor máximo de R$500,00 em cada um dos saques, mas claro, o sistema não deve permitir que o usuário saque mais do que tem na conta e tudo isso no final também será armazenado e exibido no extrato. Esta operação é feita através da função de saque, que deve receber apenas argumentos nomeados.

Extrato: Nessa parte o programa vai mostrar todos os depósitos, saques e saldo da conta, usando uma função que aceita argumentos tanto posicionais quanto nomeados, mas se não tiver extrato ainda o programa vai exibir uma mensagem avisando isso.

Sair: Ele dá uma mensagem de despedida e fecha o programa.
