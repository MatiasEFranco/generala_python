import random

# entrada: ¿cuántos nuevos números deseo?
def tirar_dados(dados_deseados_a_tirar):
    lista_dados = []
    for tirada in range(dados_deseados_a_tirar):
        dado = random.randint(1, 6)
        #print("tirada:", tirada, " dado:", dado)
        lista_dados.append(dado)

    return lista_dados
# salida: dados/números resultantes

if __name__ == "__main__":
    # Vamos a hacer nuestras millones de pruebas
    #cantidad_desea = int(input("¿Cuántos dados desea usted tirar?"))
    print("Deseo tirar 4")
    dados_tirados_1 = tirar_dados(4)
    print(dados_tirados_1)

    print("Deseo tirar 1")
    dados_tirados_2 = tirar_dados(1)
    print(dados_tirados_2)

    print("Deseo tirar 10")
    dados_tirados_3 = tirar_dados(10)
    print(dados_tirados_3)

    print("Deseo tirar 0")
    dados_tirados_4 = tirar_dados(0)
    print(dados_tirados_4)

    print("Deseo tirar -1") # prueba invalida
    dados_tirados_5 = tirar_dados(-1)
    print(dados_tirados_5)