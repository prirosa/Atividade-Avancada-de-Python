#Reescreva seu programa de notas usando a função computarNotas que recebe a pontuação como parâmetro 
# e retorna a nota como uma string.

pontuacao = float(input ("Digite a pontuação entre 0.0 e 1.0: ")) 

def computarNotas (pontuacao):
     if (pontuacao <= 1 and pontuacao >=0):
        if pontuacao >= 0.9:
            return ("A nota é A")
        if pontuacao == 0.8:
            return ("A nota é B")
        if pontuacao == 0.7:
            return ("A nota é C")
        if pontuacao == 0.6:
            return ("A nota é D")
        if pontuacao < 0.6:
            return ("A nota é F")
        else:
            print("Pontuação Inválida")  

notas = computarNotas(pontuacao)

print(notas)

