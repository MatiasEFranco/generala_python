'''
objetivos:  Dado un conjunto de dados/números separar un determinado dado/número objetivo
entrada: la lista de datos tirados, el número que se desea guardar (objetivo) y la lista de dados guardados
salida: lista de dados guardados actualizada
'''

# entrada: 
# 1) la lista de datos tirados, 
# 2) el número que se desea guardar (objetivo)
# 3) la lista de dados guardados


# objetivo:
# 1) dado un conjunto de dados --> [4-1-4]
# 2) numero que se desea guardar --> 4
# 3) lista de datos guardados --> [4, 4]

lista_dados = [4, 1, 4]
numero_objetivo = 4
dados_guardados = [4, 4]

for dado in lista_dados:
    if dado == numero_objetivo:
        dados_guardados.append(dado)

print("Lista de dados guardados actualizada", dados_guardados)
#salida: lista de dados guardados actualizada