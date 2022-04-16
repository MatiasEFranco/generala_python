import random

def tirar_dados(dados_deseados_a_tirar):
    lista_dados = []
    for tirada in range(dados_deseados_a_tirar):
        dado = random.randint(1, 6)
        #print("tirada:", tirada, " dado:", dado)
        lista_dados.append(dado)

    return lista_dados

def escoger_mas_repetido(lista_dados):
    try:
        max_repeticiones = max(lista_dados, key=lista_dados.count)
        # salida: el número que más se repitió
    except:
        print("todo mal!!")
        max_repeticiones = 0
    return max_repeticiones


def guardar_mas_repetido(lista_dados, numero_objetivo, dados_guardados):
    for dado in lista_dados:
        if dado == numero_objetivo:
            dados_guardados.append(dado)

    return dados_guardados


if __name__ == "__main__":
    # Inicializamos las variables que utilizaremos en le juego
    dados_guardados = []

    # Empieza mi generala
    # TIRADA 1
    # ---------------------------------------------------
    lista_dados = tirar_dados(5)

    numero_objetivo = escoger_mas_repetido(lista_dados)

    dados_guardados = guardar_mas_repetido(lista_dados, numero_objetivo, dados_guardados)

    print("Dados guardados en la primera tirada:", dados_guardados)
    if len(dados_guardados) == 5:
        print("Generala!")
        exit()
    # ---------------------------------------------------
    # TIRADA 2
    # ---------------------------------------------------
    cantidad_dados_tirar = 5 - len(dados_guardados)
    # Si yo me guarde 1 dado, entonces
    # cantidad_dados_tirar = 5 - 1 = 4 --> 4 dados a tirar

    # Si yo me guarde 3 dados, entonces
    # cantidad_dados_tirar = 5 - 3 = 2 --> 2 dados a tirar
    lista_dados = tirar_dados(cantidad_dados_tirar)

    dados_guardados = guardar_mas_repetido(lista_dados, numero_objetivo, dados_guardados)

    print("Dados guardados en la segunda tirada:", dados_guardados)
    if len(dados_guardados) == 5:
        print("Generala!")
        exit()

    # ---------------------------------------------------
    # TIRADA 3
    # ---------------------------------------------------
    cantidad_dados_tirar = 5 - len(dados_guardados)
    # Si yo me guarde 1 dado, entonces
    # cantidad_dados_tirar = 5 - 1 = 4 --> 4 dados a tirar

    # Si yo me guarde 3 dados, entonces
    # cantidad_dados_tirar = 5 - 3 = 2 --> 2 dados a tirar
    lista_dados = tirar_dados(cantidad_dados_tirar)

    dados_guardados = guardar_mas_repetido(lista_dados, numero_objetivo, dados_guardados)

    print("Dados guardados en la tercera tirada:", dados_guardados)
    if len(dados_guardados) == 5:
        print("Generala!")
        exit()
    else:
        print("bueno perdiste :)")