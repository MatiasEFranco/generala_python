'''
Tirar los dados
objetivos: obtener nuevos números, esos números son aleatorios.
entrada: ¿cuántos nuevos números deseo? ¿qué tipo dado?
salida: dados/números resultantes. 
Si yo ingrese "deseo tirar 3 dados obtendré como salida 3 dados, 
que representan 3 números aleatorios
'''

import random

# entrada: ¿cuántos nuevos números deseo?

# Objetivo
# 1) obtener nuevos números [1 al 6]
numero = 4
# 2) esos númeroS son aleatorios.
dados_deseados_a_tirar = int(input("¿Cuántos dados desea usted tirar?"))

lista_dados = []

for tirada in range(dados_deseados_a_tirar):
    dado = random.randint(1, 6)
    print("tirada:", tirada, " dado:", dado)
    lista_dados.append(dado)

# salida: dados/números resultantes
print("dados tirados:", lista_dados)