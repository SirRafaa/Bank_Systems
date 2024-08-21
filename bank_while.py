contas = {}

while True:
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar saldo")
    print("5. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        numero_conta = input("Digite o número da conta: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        contas[numero_conta] = saldo_inicial
        print("Conta criada com sucesso!")

    elif opcao == 2:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if numero_conta in contas:
            contas[numero_conta] += valor_deposito
            print("Depósito realizado com sucesso!")
        else:
            print("Conta não encontrada.")

    elif opcao == 3:
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if numero_conta in contas:
            if contas[numero_conta] >= valor_saque:
                contas[numero_conta] -= valor_saque
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta não encontrada.")

    elif opcao == 4:

        if numero_conta in contas:
            print("Saldo:", contas[numero_conta])
        else:
            print("Conta não encontrada.")

    elif opcao == 5:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")