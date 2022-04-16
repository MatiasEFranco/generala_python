'''
escoger_el_más_repetido
objetivos: dado un conjunto de dados elegir aquel número que más se repitió entre ellos.
entrada: dados....¿cuántos? No importa :). La entrada es un conjunto de números
salida: número que más se repitió
'''

# entrada: La entrada es un conjunto de números

# objetivo:
# 1) dado un conjunto de dados [5-4-3-4-1]
# 2) elegir aquel número que más se repitió entre ellos. --> salida espera un 4

lista_dados = [5, 4, 3, 4, 1]

#print(len(lista_dados))

max_repeticiones = max(lista_dados, key=lista_dados.count)
print("Cuál fue el número más repetido?", max_repeticiones)
# salida: el número que más se repitió