def sacar(*, saldo, extrato, cont):
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

def depositar(saldo, extrato, /):
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

def insere_espacos_direita(string, quantidade):
    string = str(string)
    if(len(string) >= quantidade):
        return string
    else:
        while(len(string) < quantidade):
            string += " " 
        return string

def mostra_extrato(saldo, /, *, extratoo):
    print(" Extrato Santandesco ".center(31,"-"))
    print("|"+ ("Saldo atual = R$" + str(saldo)).center(30," ") + "|")
    print("|" + "-".center(30,"-") + "|")
    print("|" + "Operação".center(15," "),end="")
    print("Valor".center(15," ") + "|")
    for operacao, valor in extratoo:
        print("| " + insere_espacos_direita(operacao, 18) + "R$" + insere_espacos_direita(str(valor),9) + "|")
    print("-".center(31,"-"))





def verifica_existencia_cpf(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if(usuario[0]["cpf"] == cpf):
            return True
    return False


def cadastra_usuario(lista_usuarios):
    cpf = int(input("Digite seu CPF: "))
    if(verifica_existencia_cpf(lista_usuarios, cpf) == True):
        print("Usuário já criado, favor fazer login para alterar os dados ou cadastrar novo usuário!")
        return None
    else:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de Nascimento: ")
        endereco = input("Digite seu endereço: ")
        senha = input("Digite sua senha: ")
        return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "senha": senha}
    
    
def valida_login(lista_usuarios):
    index_usuario = -1
    cpf = int(input("Digite o seu CPF para login: "))
    senha = ""
    if(verifica_existencia_cpf(lista_usuarios, cpf) == True):
        senha = input("Digite sua senha: ")
    else:
        print("CPF não encontrado!")
        return index_usuario

    index_usuario = 0
    for usuario in lista_usuarios:
        if usuario[0]["cpf"] == cpf:
            if usuario[0]["senha"] == senha:
                print(f"Seja bem vindo {usuario[0]["nome"]}! Seu saldo é de R${usuario[2]}.")
                return index_usuario
            else:
                print("Senha incorreta, tente novamente!")
                return -1
        else:
            index_usuario += 1
    
def mostra_usuarios(lista_usuarios):
    print(" Lista de Usuários Santandesco ".center(41,"-"))
    print("|" + " ".center(40," ") + "|")
    print("|" + "Usuário".center(25," "),end="")
    print("CPF".center(15," ") + "|")
    for usuario in lista_usuarios:
        print("| " + insere_espacos_direita(usuario[0]["nome"], 29) + insere_espacos_direita(usuario[0]["cpf"],10) + "|")
    print("-".center(41,"-"))

def mostra_atributos_usuario(usuario):
    for atributo, valor in usuario.items():
        print(f"{atributo}: {valor}")

def altera_atributos_usuario(lista_usuarios, usuario):
    print("\nQual informação você deseja alterar:\n",end="")
    print("[1] Nome\n",end="")
    print("[2] Data de Nascimento\n",end="")
    print("[3] CPF\n",end="")
    print("[4] Endereço\n",end="")
    print("[5] Senha\n",end="")
    print("[0] Sair\n",end="")
    info = int(input("Digite seu comando: "))

    if(info == 1): # Nome
        nome = input("Digite o nome alterado: ")
        usuario["nome"] = nome
        print("Nome alterado com sucesso!")
        return usuario

    elif(info == 2): # Data Nascimento
        data_nascimento = input("Digite o data de nascimento alterada: ")
        usuario["data_nascimento"] = data_nascimento
        print("Data de nascimento alterado com sucesso!")
        return usuario
        
    elif(info == 3): # CPF
        cpf = int(input("Digite seu novo CPF: "))
        if(cpf == usuario["cpf"]):
            print("Número de CPF inalterado!")
            return usuario
        elif(verifica_existencia_cpf(lista_usuarios, cpf) == True):
            print("CPF já utilizado, impossível fazer a troca!")
            return usuario
        else:
            usuario["cpf"] = cpf
            print("CPF alterado com sucesso!")
            return usuario
            
    elif(info == 4): # Endereço
        endereco = input("Digite o endereço alterado: ")
        usuario["endereco"] = endereco
        print("Endereço alterado com sucesso!")
        return usuario
        
    elif(info == 5): # Senha
        senha = input("Digite o senha alterado: ")
        usuario["senha"] = senha
        print("Senha alterada com sucesso!")
        return usuario
        
    elif(info == 0): # Sair
        print("Saindo!")
        return usuario
    else:
        print("Não foi possível identificar o atributo que você deseja alterar!")
        return usuario




def menu_inicial():
    print("\n")
    print("[1] Entrar\n[2] Cadastrar Usuário\n[3] Visualizar Usuários\n[0] Sair")
    return int(input("Digite seu comando: "))
    

def menu_usuario():
    print("\n")
    print("[1] Sacar\n[2] Depositar\n[3] Visualizar Extrato\n[4] Verificar infos pessoais\n[5] Alterar infos pessoais\n[0] Sair")
    return int(input("Digite seu comando: "))





def main():
    menu = 0 # 0 = inicial, 1 = usuario
    
    entrada = -1
    saldo = 0.0
    cont_saque = 0

    index_usuario = -1
    usuario = {"nome": None, "data_nascimento": None, "cpf": None, "endereco": None, "senha": None}
    extrato = []
    lista_usuarios = [] # {atributos_usuario, extrato, saldo_atual}
    
    
    print("Seja bem vindo ao Santandesco!")
    while(menu != -1):

        # Faz o gerenciamento das opções do usuário
        if(menu == 0): # se estiver no menu Inicial:
            entrada = menu_inicial()
            if(entrada == 1): # Fazer Login
                index_usuario = valida_login(lista_usuarios)

                if(index_usuario != -1): # Validou o usuário!
                    saldo = 0.0
                    extrato = []

                    
                    usuario = lista_usuarios[index_usuario][0]
                    extrato = lista_usuarios[index_usuario][1].copy()
                    saldo = lista_usuarios[index_usuario][2]
                    cont_saque = 0
                    menu = 1
                print("")
                
            elif(entrada == 2): # Cadastrar novo usuário
                novo_usuario = cadastra_usuario(lista_usuarios)
                if(novo_usuario != None):
                    lista_usuarios.append([novo_usuario,[],0])
                    print("Usuário criado com sucesso!")
                
            elif(entrada == 3): # Visualizar usuários
                mostra_usuarios(lista_usuarios)
                
            elif(entrada == 0): # Sair do sistema
                menu = -1
                print("Desligando o sistema")
            else: # Erro
                print("Favor inserir uma entrada válida!")
                
            
        elif(menu == 1): # se estiver no menu do usuário:
            entrada = menu_usuario()
            if(entrada == 1): # 
                if(cont_saque>=3):
                    print("Operação bloqueada devido ao limite de saques diários!")
                else:
                    saldo, cont_saque = sacar(saldo = saldo, extrato = extrato, cont = cont_saque)
           
            elif(entrada == 2): # 
                saldo = depositar(saldo, extrato)
                
            elif(entrada == 3): # 
                mostra_extrato(saldo, extratoo = extrato)

            elif(entrada == 4): # Verificar infos pessoais
                mostra_atributos_usuario(usuario)

            elif(entrada == 5): # Alterar infos pessoais
                usuario = altera_atributos_usuario(lista_usuarios, usuario)

            elif(entrada == 0): # 
                print("Fazendo logoff")
                menu = 0 # Volta para o menu inicial

                # Sobe as alterações para a lista de usuarios
                lista_usuarios[index_usuario][0] = usuario
                lista_usuarios[index_usuario][1] = extrato.copy()
                lista_usuarios[index_usuario][2] = saldo

                # Reseta as variáveis de usuário
                cont_saque = 0 # Se o usuário deslogar e logar em seguida, a contagem de saque reseta! Usuário safadinho!
                index_usuario = -1
                usuario = {"nome": None, "data_nascimento": None, "cpf": None, "endereco": None, "senha": None}
                extrato = []
                saldo = 0
                
                # Subir todas as alterações do usuario na lista de usuarios
            else:
                print("Favor inserir uma entrada válida!")
                
        else:
            raise Exception("ID do Menu inválido, revisar e corrigir!")

main()