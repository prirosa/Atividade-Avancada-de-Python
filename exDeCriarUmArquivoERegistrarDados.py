#Faça um programa utilizando estruturas de função, try..except que tenha as seguintes funcionalidades:
#usuário informe nome, idade e email; salve esses dados num arquivo separado por vírgulas;
#ofereça a opção de exclusão de determinadas linhas do arquivo (informada pelo usuário);
#e coloque os dados em ordem alfabética antes de gravar o arquivo.
 
arq = "cadastrodedados.txt"
 
def arquivoExiste(nome):
    try:
        abrirArq = open(nome,"rt")
        abrirArq.close()
    except FileNotFoundError:
        return False
    else:
        return True
   
def criarArquivo(nome):
    try:
        abrirArq = open (nome,"wt+")
        abrirArq.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")
 
if not arquivoExiste(arq):
    criarArquivo(arq)
       
def listar(arq):
    abrirArq = open(arq, "rt")
    lista = abrirArq.readlines()
    lista.sort()
    abrirArq.close()
    arqNovo = open("cadastrodedados.txt","w")
    arqNovo.writelines(lista)
    arqNovo.close()
   
    abrirArq = open(arq,"r")
    print(abrirArq.read())
    abrirArq.close()
   
def lerArquivo(nome):
    try:
        abrirArq = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        print("-" * 36)
        print("PESSOAS CADASTRADAS".center(36))
        print("-" * 36)
        for linha in abrirArq:
            dado = linha.split(";")
            dado [2] = dado[2].replace("\n","")
            print(f"{dado[0]}, {dado[1]}, {dado[2]}")
        print("-" * 36)
        print("PESSOAS CADASTRADAS ORDEM ALFABÉTICA".center(36))
        print("-" * 36)
        return listar(arq)
    finally:
        abrirArq.close()
       
def cadastrar(arq, nome = "Desconhecido", idade = 0, email = "Desconhecido"):
    try:
        abrirArq = open(arq, "at")
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            abrirArq.write(f"{nome}; {idade}; {email}\n")
        except:
            print("Houve um erro na hora de escrever os dados")
        else:
            print("Novo registro cadastrado")
            abrirArq.close()
       
def removerLinha(arq):
    try:
        abrirArq = open(arq, "rt")
        print("-" * 36)
        print("EXCLUIR DADOS".center(36))
        print("-" * 36)
        dados = abrirArq.readlines()
    except:
        print("Houve um erro ao abrir o arquivo")
        return False
    finally:
        abrirArq.close()
   
    for linha in dados:
        print("Chave: ", dados.index(linha),": ", linha, end="")
   
    excluirLinha = int(input("Digite a chave para excluir: "))
    dados.pop(excluirLinha)
 
    try:
        arqNovo = open (arq, "wt")
        for linha in dados:
            arqNovo.write(linha)
    except:
        pass
    finally:
        arqNovo.close()
       
def menu(lista):
    contador = 1
    for item in lista:
        print (f"{contador} - {item}")
        contador += 1
    opc = int(input("Sua opção é: "))
    return opc
 
while True:
    print("-" * 36)
    print("MENU PRINCIPAL:".center(36))
    print("-" * 36)
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar novas pessoas", "Excluir do sistema", "Sair do sistema"])    
    if resposta == 1:
    #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
       
    elif resposta == 2:
    #Opção de cadastrar uma nova pessoa
        print("-" * 36)
        print("NOVO CADASTRO".center(36))
        print("-" * 36)
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        email = str(input("Email:"))
        cadastrar(arq, nome, idade, email)
       
    elif resposta == 3:
    #Opção de excluir o dado        
        removerLinha(arq)
   
    elif resposta == 4:
        print("Saindo do sistema!")
        break
    else:
        print("Erro! Digite uma opção válida!")