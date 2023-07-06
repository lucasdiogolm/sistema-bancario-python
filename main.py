# CRIANDO SIATEMA BANCÁRIO EM PYTHON

menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f} \n"
        else:
            print("Operação falhou! O valor informado é inválido :( ")
    
    elif opcao == 's':
        valor = float(input("Qual o valor você deseja sacar? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Você não possui saldo suficiente.')
        elif excedeu_limite:
            print('Ops! O vaor do saque excedeu o limite.')
        elif excedeu_saques:
            print('Impossível realizar essa ação. Você excedeu o seu limite de saques.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado. Valor: R${valor:.2f} \n"
            numero_saques += 1

        else:
            print("Algo deu errado! A operação falhou. Tente novamente.")
    
    elif opcao == 'e':
        print('\n =============== EXTRATO ===============')
        print('Não foram realizadas movimentação.' if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("===========================================")

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor, selecione novamente a operação desejada.')

    
