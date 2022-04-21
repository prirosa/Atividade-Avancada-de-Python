#Escreva um programa que lê repetidamente números até que o usuário digite "pronto". Quando pronto for 
# digitado, mostre a soma total, a quantidade, o maior, o menor e a média dos números digitados. 
# Se o usuário digitar qualquer coisa que não seja um número, detecte o erro usando o try except e 
# mostre uma mensagem de erro na tela, seguindo para receber o próximo número

valores = []

while True:
    try:
        valores.append(int(input("Digite um número: ")))
    except (ValueError,TypeError):
        print("Detectou um erro, por favor digite um número válido")
    finally:
        resp = str(input("Quer continuar? [sim/pronto]"))
        if resp in "pronto":
            break
        else:
            continue

print('=--= ' * 15)
print(f"A soma total é {sum(valores)}")
print(f"A quantidade de números na lista é: {len(valores)}") 
print(f"O maior valor é: {max(valores)}") 
print(f"O menor valor é {min(valores)}")
print(f"A media é {sum(valores)/len(valores)}")