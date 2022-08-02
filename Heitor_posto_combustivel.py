'''
Problema combustível
Um posto de combustíveis deseja determinar qual de seus produtos tem a preferencia de seus clientes. Escreva um algoritmo para ler o tipo de combustivel abastecido
(codificdo da seguinte forma: 1. álcool 2. gasolina 3. diesel 4. fim). Caso o usuario informe um codigo invalido (fora da faixa de 1 a 4) deve ser solicitado um 
novo código (até que seja válido). O programa será encerrado qnd o codigo informado foi o número 4, devendo então mostrar a mensagem "Muito obrigado", bem como as 
quantidades de cada combustivel
'''

alcool = 0
gasolina = 0
diesel = 0

codigo = int(input("Informe um código(1, 2, 3) ou 4 para parar: "))

while codigo != 4 :
    if codigo == 1 :
        alcool += 1
        codigo = int(input("Informe um código(1, 2, 3) ou 4 para parar: "))        
    if codigo == 2 :
        gasolina += 1
        codigo = int(input("Informe um código(1, 2, 3) ou 4 para parar: "))
    if codigo == 3 :
        diesel += 1
        codigo = int(input("Informe um código(1, 2, 3) ou 4 para parar: "))
    if codigo < 1 or codigo > 4 :
        codigo = int(input("Informe um código(1, 2, 3) ou 4 para parar: "))
else :
    print ("Muito Obrigado!")
    print ("Álcool: ", alcool)
    print ("Gasolina: ", gasolina)
    print ("Diesel: ", diesel)
