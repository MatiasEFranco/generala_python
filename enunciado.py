# Python Inicial [Python]
# Ejercicio integrador

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira la dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números
(la función "lista_aleatoria" se creó en los ejercicios de profudización de funciones)

Esa lista de datos generada aleatoriamente se llamará "dados_tirados"
Lista "dados_tirados" se utiliza para guardar 5 dados, cada dado es de 6 caras,
es decir que cada dado puede valer un número de 1 a 6.

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió en esa tirada. 
Consultar los ejemplos de anexo de la clase de funciones en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una variable aparte llamda "contador_generala"
cuantas veces se repitió hasta ahora el número más repetido. 
Ese número será el candidato para buscar sacar generala.

Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4",
por lo canto el "contador_generala" valdrá 3, porque el primer número
más repetido fue 4, y este número salio tres veces en la primera tirada.

4) Debe volver a tira los dados, generar nuevos
números aleatorios.
Si en el contador "contador_generala" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados (5-3). 
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a contar cuantas veces aparece el número "4",
ya que es el número que estoy buscando almacenar para llegar a generala.
Se deberá aumentar el contador por cada cuatro que haya salido en la tirada.
Sino salió el "4" vuelvo a tirar sin aumentar el contador (repetir el punto 4)

5) Debe repetir este proceso hasta que el contador "contador_generala"
haya llegado a 5, es decir, he sacado 5 números iguales

NOTA: Recordar que en este ejemplo se buscó alcanzar la generala con "4" porque
fue el primero número más repetido en la primera tirada. Tener eso en cuenta que el
número que deberá buscar para alcanzar la generala depende de cual fue el más repetido
en la primera tirada.
'''

import random

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice

def lista_aleatoria(cantidad):   
    lista_aux = []      #se genera una lista axuliar para ir guardadno los valores generados aleatoreamente
    
    for i in range(cantidad):

        lista_aux.append(random.randint(1,6))

    return lista_aux    #retornamos la lista axuliar con los valores generados entre los limites indicados como "inicio" y "fin"


'''def elegir_numero(numero, elegido):
    num_elegido = None
   
    if (elegido == None):   #elegido toma el parametro del arguemnto numero_elegido que inicialmente esta como None
      num_elegido = max(numero, key = numero.count)   #indica que numero se repitio mas veces y lo selecciono
    
    else:
        for i in numero:    #en la segunda y tercer tirada el argumento de la variable elegido ya tiene un valor po lo tanto ingresa a este for para recorrer la lista
            if i == elegido:
                return i
            

    return num_elegido  #retorno el numero elegido'''


def elegir_numero(numero, elegido):
    num_elegido = max(numero, key = numero.count)   #indica que numero se repitio mas veces y lo selecciono
    
    return num_elegido  #retorno el numero elegido


def  contar_numero(dados, numero):
    cantidad_dados = dados.count(numero)  #indica cuantas veces se repitio el numero elegido

    return cantidad_dados   #retorno cuantos dados guarde, que es igual ala cantidad de veces que se repite el numero elegido
# --------------------------------
 
# --------------------------------

if __name__ == '__main__':
    print("¡El juego de la generala!")
    # A partir de aquí escriba el código que
    # invoca a las funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    
    contador_generala = 0   #indicador de los dados que voy guardando en cada tirada
    dados_tirados = []      #Aqui guardamos los valores en cada tirada
    dados = 5               #indica la cantidad de dados a tirar
    tirada = 0              #indica el numeor de la tirada
    numero_elegido = None   #en esta variable guardo el numero elegido, inicialmente aparece como None
    dados_guardados = 0     #aqui guardamos la cantidad de dados guardados
    
    while tirada < 3 and contador_generala != 5:   #aqui generamos las 3 tiradas con este bucle
        tirada += 1 #aumento el numero de la tirada
        dados_tirados = lista_aleatoria(dados)   #llamo a la funcion para generar la lista con los valores tirados por cada dado
              
        if tirada == 1:
            numero_seleccionado = elegir_numero(dados_tirados, numero_elegido)  #llamo a la funcion para elegir el numero que mas veces se repite en la lista

            if (numero_elegido == None) or (numero_elegido == numero_seleccionado): #aqui guardo el numero que mas veces se repitio en la tirada
                numero_elegido = numero_seleccionado
                contador_generala = contar_numero(dados_tirados,  numero_elegido)   #guardo el nuevp valor del contador generala sabiendo cuantos dados guarde
                dados -= contador_generala  #descuento los dados guardados
                dados_guardados += contador_generala    #cantidad de dados que voy guardando
        else:
            contador_generala = contar_numero(dados_tirados,  numero_elegido)   #guardo el nuevp valor del contador generala sabiendo cuantos dados guarde
            dados -= contador_generala  #descuento los dados guardados
            dados_guardados += contador_generala    #cantidad de dados que voy guardando

        print("En la tirada", tirada, " los dados tirados fueron", dados_tirados)   #mostramos en que torada estamos y los valores que salieron en esa tirada
        print("El numero elegido es", numero_elegido, " la cantidad de dados guardados es ", dados_guardados, "\n") #aqui indicamos el numero elegido y la cantidad de veces  que salio        
        
    if dados_guardados == 5:
        print("Felicidades hiciste GENERALA con el numero", numero_elegido)

    else:
        print("Lo siento perdiste")  


    print("fin")