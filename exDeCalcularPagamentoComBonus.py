#Reescreva seu programa de cálculo de pagamento com um adicional de 50% de hora extra trabalhada acima de 40hrs.
#Crie uma função chamada calculoPagamento que aceite dois parâmetros (horas e taxa hora).
#Exemplo: horas = 45; taxa = 10; total = 475,00
 
def calculo(horas,taxa):
    calculoPagamento = horas * taxa
    if horas > 40:  
        mais50 = calculoPagamento + (calculoPagamento * 50/100)
        print(f"O adicional de 50% é de R$ {calculoPagamento*50/100}")
        return mais50
        
    return calculoPagamento
 
horas = int (input("Qual é o tempo de trabalho: "))
taxa = int (input("Qual o valor da taxa: "))
 
print(f"O valor é de R$ {calculo(horas,taxa)}")
