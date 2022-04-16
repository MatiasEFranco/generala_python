
# entrada: 
# 1) la lista de datos tirados, 
# 2) el número que se desea guardar (objetivo)
# 3) la lista de dados guardados
def guardar_mas_repetido(lista_dados, numero_objetivo, dados_guardados):
    for dado in lista_dados:
        if dado == numero_objetivo:
            dados_guardados.append(dado)

    return dados_guardados
# salida: dados/números guardados actualizados

if __name__ == "__main__":
    # Vamos a hacer nuestras millones de pruebas
    lista_dados = [4, 1, 4]
    numero_objetivo = 4
    dados_guardados = [4, 4]
    print("Antes de guardar el mas repetiro la lista de dados guardados era:")
    print(dados_guardados)
    dados_guardados = guardar_mas_repetido(lista_dados, numero_objetivo, dados_guardados)
    print("Despues de guardar los dados iguales al numero objetivo la lista queda:")
    print(dados_guardados)

    lista_dados = [6]
    numero_objetivo = 4
    dados_guardados = [4, 4]
    print("Antes de guardar el mas repetiro la lista de dados guardados era:")
    print(dados_guardados)
    dados_guardados = guardar_mas_repetido(lista_dados, numero_objetivo, dados_guardados)
    print("Despues de guardar los dados iguales al numero objetivo la lista queda:")
    print(dados_guardados)

