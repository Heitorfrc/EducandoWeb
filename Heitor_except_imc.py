'''
Use função e except para fazer uma calculadora de IMC. Em caso de erro o programa deve enviar uma mensagem e rodar novamente
'''

def imcFunction(num1, num2) :
    return num1 / (num2 * num2)

print("Programa de calcular o IMC")
rodar = True

while(rodar) :
    try :
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        imc = imcFunction(peso, altura)
        print("Seu IMC é:", imc)
        rodar = False
    except :
        print("Dados inseridos incorretamente")
print("Obrigado")