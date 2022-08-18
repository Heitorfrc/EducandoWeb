import math

print("#############################################")
print("Bem vindo a calculadora de DPR médio da Ellen")
print("#############################################")

# dano do d10 da Glaive
danoGlaive = 5.5
# dano do d4 da bunda da glaive
danoBunda = 2.5
# modificador de força + modificador mágico da Glaive
modificador = 4
# dano extra do Spirit Shroud D8
bonusSpirit = 4.5
# dano extra do Crusaders Mantle D4
bonusCrusader = 2.5
# dano extra do Improved Divine Smite D8
improvedDivine = 4.5

puro = (danoGlaive + modificador)*2 + (danoBunda + modificador)

puro11 = (danoGlaive + modificador + improvedDivine)*2 + (danoBunda + modificador + improvedDivine)

primeiroSpirit = (danoGlaive + modificador + bonusSpirit)*2
segundoSpirit = (danoGlaive + modificador + bonusSpirit)*2 + (danoBunda + modificador + bonusSpirit)

primeiroSpirit11 = (danoGlaive + modificador + bonusSpirit + improvedDivine)*2
segundoSpirit11 = (danoGlaive + modificador + bonusSpirit + improvedDivine)*2 + (danoBunda + modificador + bonusSpirit + improvedDivine)

primeiroHaste = (danoGlaive + modificador) + (danoBunda + modificador)
segundoHaste = (danoGlaive + modificador)*3 + (danoBunda + modificador)

primeiroHaste11 = (danoGlaive + modificador + improvedDivine) + (danoBunda + modificador + improvedDivine)
segundoHaste11 = (danoGlaive + modificador + improvedDivine)*3 + (danoBunda + modificador + improvedDivine)

segundoCrusader = (danoGlaive + modificador + bonusCrusader)*2 + (danoBunda + modificador + bonusCrusader)
d4Prejuizo = primeiroSpirit / bonusCrusader
d4PrejuizoSub = (segundoSpirit - segundoCrusader) / bonusCrusader

segundoCrusader11 = (danoGlaive + modificador + bonusCrusader + improvedDivine)*2 + (danoBunda + modificador + bonusCrusader + improvedDivine)
d4Prejuizo11 = primeiroSpirit11 / bonusCrusader
d4PrejuizoSub11 = (segundoSpirit11 - segundoCrusader11) / bonusCrusader

print()
print("O DPR puro sem nehum buff ou magia é:", puro)
print("O DPR utilizando Spirit Shroud no primeiro turno é", primeiroSpirit, "e em turnos subsequentes", segundoSpirit)
print("O DPR utilizando Haste no primeiro turno é", primeiroHaste, "e em turnos subsequentes", segundoHaste)

print()
print("Considerações sobre Crusaders Mantle; ela utiliza uma ação inteira para ser castada, então nenhum dano é causado no primeiro turno." )
print("ou seja seriam necessários pelo menos", math.ceil(d4Prejuizo), "D4s serem rolados para que o prejuízo de dano fosse alcançado")
print("A partir do segundo ela causa emm média", segundoCrusader,"ou seja", math.ceil(d4PrejuizoSub), "D4s de dano de prejuízo por turno subsequente" )

print()
print("No próximo nível, o 11o, o DPR muda")
print("No 11o nível o DPR puro sem nehum buff ou magia é:", puro11)
print("No 11o nível o DPR utilizando Spirit Shroud no primeiro turno é", primeiroSpirit11, "e em turnos subsequentes", segundoSpirit11)
print("No 11o nível o DPR utilizando Haste no primeiro turno é", primeiroHaste11, "e em turnos subsequentes", segundoHaste11)

print()
print("Considerações sobre Crusaders Mantle; ela utiliza uma ação inteira para ser castada, então nenhum dano é causado no primeiro turno." )
print("ou seja seriam necessários pelo menos", math.ceil(d4Prejuizo11), "D4s serem rolados para que o prejuízo de dano fosse alcançado")
print("A partir do segundo ela causa emm média", segundoCrusader11,"ou seja", math.ceil(d4PrejuizoSub11), "D4s de dano de prejuízo por turno subsequente" )



# print(d4Prejuizo)
# print(d4PrejuizoSub)
# print(d4Prejuizo11)
# print(d4PrejuizoSub11)