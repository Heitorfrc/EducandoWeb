'''
Problema "terreno"
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular, bem como 
o valor do metro quadrado do terreno. Em seguida, o programa deve mostrar o valor da área do terreno,
bem como o valor do preço do terreno, ambos com duas casas decimais, conforme exemplo.
'''

largura = float(input("Escreva a largura do terreno: "))
comprimento = float(input("Escreva o comprimento do terreno: "))
metroQuadrado = float(input("Valor do metro quadrado: "))

print ("Área do terreno:", "{:.2f}".format(largura * comprimento), "metros quadrados.")
print ("Valor do terreno:", "{:.2f}".format(largura * comprimento * metroQuadrado), "reais.")