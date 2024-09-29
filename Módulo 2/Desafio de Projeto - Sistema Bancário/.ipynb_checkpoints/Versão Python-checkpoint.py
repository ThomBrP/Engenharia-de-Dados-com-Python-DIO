def sacar(saldo, extrato,cont):
    saque = float(input("Digite o valor a sacar: R$"))
    limite = 500.0
    if(saque < 0):
        print("Impossível sacar um valor negativo! Reiniciando operação")
        return saldo, cont
    elif(saque > 500):
        print("Valor de saque acima do limite! Reiniciando operação")
        return saldo, cont
    elif(saque == 0):
        print(f"Saque de R$0.00 realizado! Saldo atual: R${saldo}")
        return saldo, cont+1
    elif(saque <= saldo):
        print(f"Valor sacado com sucesso! Saldo atual: R${saldo-saque}")
        extrato.append(["Saque", saque])
        return saldo-saque, cont+1
    else:
        print("Valor de saque inválido. Reiniciando operação")
        return saldo, cont

def depositar(saldo, extrato):
    deposito = float(input("Digite o valor a depositar: R$"))
    if(deposito<0):
        print("Valor inválido, favor inserir um valor positivo")
        return saldo
    elif(deposito == 0):
        print(f"Depósito de R$0.00 realizado com sucesso, saldo atual: R${saldo}")
        extrato.append(["Depósito", deposito])
        return saldo
    else:
        print(f"Depósito realizado com sucesso! Saldo atual: R${saldo+deposito}")
        extrato.append(["Depósito", deposito])
        return saldo + deposito

def insere_espacos_direita(string,quantidade):
    if(len(string) >= quantidade):
        return string
    else:
        while(len(string) < quantidade):
            string += " " 
        return string

def mostra_extrato(saldo, extrato):
    print(" Extrato Santandesco ".center(31,"-"))
    print("|"+ ("Saldo atual = R$" + str(saldo)).center(30," ") + "|")
    print("|" + "-".center(30,"-") + "|")
    print("|" + "Operação".center(15," "),end="")
    print("Valor".center(15," ") + "|")
    for operacao, valor in extrato:
        print("| " + insere_espacos_direita(operacao, 18) + "R$" + insere_espacos_direita(str(valor),9) + "|")
    print("-".center(31,"-"))
    

def main():
    entrada = -1
    saldo = 0.0
    extrato = []
    cont_saque = 0
    print("Seja bem vindo ao Santandesco! Seu saldo inicial é de R$0.00")
    while(entrada!=0):
        print("\n")
        print("[1] Sacar\n[2] Depositar\n[3] Visualizar Saldo\n[0] Sair")
        entrada = int(input("Digite seu comando: "))
        
        if(entrada == 1):
            if(cont_saque>=3):
                print("Operação bloqueada devido ao limite de saques diários!")
            else:
                saldo,cont_saque = sacar(saldo, extrato, cont_saque)
        elif(entrada == 2):
            saldo = depositar(saldo, extrato)
        elif(entrada == 3):
            mostra_extrato(saldo, extrato)
        elif(entrada == 0):
            print("Desligando o sistema!")
        else:
            print("Favor inserir uma entrada válida!")

main()