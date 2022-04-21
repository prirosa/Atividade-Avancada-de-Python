#Faça um programa que recebe do usuário o caminho para um arquivo, lê esse arquivo, e diz a quantidade 
#de linhas, a quantidade de palavras e a quantidade de números. Faça tratamento de exceções e declare 
#funções (def function():) para partes do seu programa, por exemplo: a abertura de um arquivo, 
#as contagens no arquivo.

def arquivoParaLer():
    nome = input("Digite o nome do arquivo : ")
    try:
     arquivo = open(nome,"r")
     return arquivo
 
    except(FileNotFoundError, TypeError):
      print("Arquivo não pode ser encontrado:", nome)
      exit()
 
def contadorTotal():
    contaLinhas = 0
    contaPalavras = 0
    varNum = 0
    varEsc = 0
    arquivo = arquivoParaLer()
    for line in arquivo:
        words = line.split()
        contaLinhas = contaLinhas + 1
        for word in words:
            contaPalavras = contaPalavras + 1
            new_string=word.strip()
            try:
              a = int(new_string)
              varNum = varNum + 1
            except:
                varEsc = varEsc + 1
       
    return contaLinhas, contaPalavras, varNum, varEsc
 
def final():
    contaLinhas, contaPalavras, varNum, varEsc = contadorTotal()  
    print()
    print("Quantidade de linhas: ", str(contaLinhas))
    print("Quantidade de palavras totais: ", str(contaPalavras))
    print("Quantidade de números encontrado: ", str(varNum))
    print("quantidade de palavras escritas: ", str(varEsc))
    print()
   
final()
