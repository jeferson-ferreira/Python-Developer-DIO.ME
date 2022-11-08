from time import sleep

menu = """
============= SISTEMA BANCÁRIO =============

 [ 1 ] - Depositar
 [ 2 ] - Sacar
 [ 3 ] - Extrato
 [ 0 ] - Sair

    => """
print()
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    print()
    if opcao == "1":
        valor = float(input(" >>> Informe o valor do depósito: "))
        print()
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\033[34m>> Depósito realizado com sucesso! <<\033[m")
        else:
            print("\033[31mOperação falhou! O valor informado é inválido.\033[m")
        print()
        sleep(1)

    elif opcao == "2":
        valor = float(input(" >>> Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("\033[31mOperação falhou! Você não tem saldo suficiente.\033[m")
        elif excedeu_limite:
            print(
                "\033[31mOperação falhou! O valor do saque excede o limite.\033[m")
        elif excedeu_saques:
            print(
                "\033[31mOperação falhou! Número máximo de saques excedido.\033[m")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("\033[31mOperação falhou! O valor informado é inválido.\033[m")
        print()
        sleep(1)

    elif opcao == "3":
        print("================ EXTRATO ================")
        sleep(0.5)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=" * 42)
        print()
        sleep(1)

    elif opcao == "0":
        print('SAINDO DO SISTEMA...')
        sleep(0.6)
        break

    else:
        print(
            "\033[31mOperação inválida, por favor selecione novamente a operação desejada.\033[m")
