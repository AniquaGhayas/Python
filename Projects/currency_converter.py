#a program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Pesos = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

total = (Pesos * 0.00026 + soles * 0.30 + reais * 0.18)
print(total)
