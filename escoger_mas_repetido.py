
# entrada: La entrada es un conjunto de números
def escoger_mas_repetido(lista_dados):
    try:
        max_repeticiones = max(lista_dados, key=lista_dados.count)
        # salida: el número que más se repitió
    except:
        print("todo mal!!")
        max_repeticiones = 0
    return max_repeticiones

    #print("Cuál fue el número más repetido?", max_repeticiones)

if __name__ == "__main__":

    lista_dados_1 = [5, 4, 3, 4, 1]

    print("Lista de dados analizar:", lista_dados_1)

    numero_mas_repetido_1 = escoger_mas_repetido(lista_dados_1)
    
    print(numero_mas_repetido_1)

    lista_dados_2 = []
    print("Lista de dados analizar:", lista_dados_2)
    numero_mas_repetido_2 = escoger_mas_repetido(lista_dados_2)
    print(numero_mas_repetido_2)

    lista_dados_3 = [5]
    print("Lista de dados analizar:", lista_dados_3)
    numero_mas_repetido_3 = escoger_mas_repetido(lista_dados_3)
    print(numero_mas_repetido_3)

    lista_dados_4 = 8
    print("Lista de dados analizar:", lista_dados_4)
    numero_mas_repetido_4 = escoger_mas_repetido(lista_dados_4)
    print(numero_mas_repetido_4)