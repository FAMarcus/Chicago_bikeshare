# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])

# É o cabeçalho dos dados, para que possamos identificar as colunas.
# Alberto: Quero guardar o cabecalho para uso futuro. 
file_header = data_list[0]

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(20):
    print(data_list[i]);

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# Escrita original
#for i in range(20):
#    print(i+1," - ",data_list[i][6]);

# Escrita sugerida pelo revisor
for i, line in enumerate(data_list[:20],start=1):
    print("Line : {}\tGender: {}".format(i,line[-2]))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
      Função para converter uma coluna em uma lista de dados.
      Argumentos:
          param1: Matriz de dados.
          param2: Coluna da matriz a ser convertida em lista.
      Retorna:
          Uma lista de valores da coluna.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in range(len(data)):
        column_list.append(data[i][index])
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
not_espc = 0
for gender in column_to_list(data_list, -2):
    if gender == "Male":
        male += 1
    elif gender == "Female":
        female += 1
    else:
        not_espc += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)
print("Nao especificado: ", not_espc)
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
      Função que conta cada genero de uma dada lista.
      Argumentos:
          data_list: Arquivo de dados.
      Retorna:
          Uma lista com o número de de pessoas do gênero masculino e feminino.
    """
    male = 0
    female = 0
    genders = [x[-2] for x in data_list] # Lê cada linha da matriz e seleciona o penultimo elemento.
    for gender in genders:
        if gender == "Male":
            male += 1
        elif gender == "Female":
            female += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
      Função para verificar o gênero predominante.
      Argumentos:
          data_list: Arquivo de dados.
      Retorna:
          O genero predominante: Masculino, Feminino ou Igual.
      Função Auxiliar: count_gender(...)    
    """
    answer = ""
# Escrita original - Chama a função count_gender muitas vezes  
#    if count_gender(data_list)[0] > count_gender(data_list)[1]:
#        answer = "Masculino"
#    elif count_gender(data_list)[0] < count_gender(data_list)[1]:
#        answer = "Feminino"
#    else:
#        answer = "Igual"        
#    return answer

# Escrita sugerida para reduzir as chamadas
    male, female = count_gender(data_list)
    if male > female:
        answer = "Masculino"
    else:
        answer = "Feminino"
    return answer
            
print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
item_types = []
count_items = []
column_list = column_to_list(data_list, -3)
find_type = set(column_list)
item_types = list(find_type)
for i in range(len(item_types)):
    contador = 0;
    for j in range(len(column_list)):
        if column_list[j] == item_types[i]:
            contador += 1
    count_items.append(contador)

print("\n Imprimindo resultados para count_items()")
print("Tipos:", item_types, "Counts:", count_items)

y_pos = list(range(len(item_types)))

fig, ax = plt.subplots()
rects1 = ax.bar(y_pos, count_items)

plt.axis([-0.5, 2.5, 0, 1500000])
plt.ylabel('Quantidade')
plt.xlabel('User Type')
plt.xticks(y_pos, item_types)
plt.title('Quantidade por tipo de usuario')

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    (c) From Matplotlib tutorial
    https://matplotlib.org/examples/api/barchart_demo.html
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)

plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Por que não foi considerado as pessoas que não declararam o gênero."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

def achar_min(lista):
    """Returns the minimum value of a list.
    use: min_list = achar_min(lista)
    """
    lista[:] = [float(j) for j in lista] # garantir que a lista seja numeros.
    menor_valor = lista[0]
    for i in range(len(lista)-1):
        if menor_valor > lista[i+1]:
            menor_valor = lista[i+1]
    return menor_valor
    
def achar_max(lista):
    """Returns the maximum value of a list.
    use: max_list = achar_max(list)
    """
    lista[:] = [float(j) for j in lista] # garantir que a lista seja numeros.
    maior_valor = lista[0]
    for i in range(len(lista)-1):
        if maior_valor < lista[i+1]:
            maior_valor = lista[i+1]
    return maior_valor
    
def media(lista):
    """Returns the average of a list.
    use: media = media(lista)
    """
    lista[:] = [float(j) for j in lista] # garantir que a lista seja numeros.
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma / len(lista)    

def quicksort(arr):
    """
    Return input list in crescent order.
    use: new_list = quicksort(list)
    Arguments:
        list - data set
    References:
       * Written by Michael Neumann
         https://wiki.python.org.br/QuickSort
       * "Introduction to Algorithms". By Thomas H. Cormen, 
          Charles E. Leiserson and Ronald L. Rivest. MIT Press.
    """
    if len(arr) <= 1: return arr
    m = arr[0]
    return quicksort([i for i in arr if i < m]) + \
           [i for i in arr if i == m] + \
           quicksort([i for i in arr if i > m])
        
def mediana(lista):
    """
    Return the median of a list.
    use: X = mediana(list)
    Arguments:
        list - vector of data.
    Auxiliary functions: 
        quicksort(list)
    (c) F. Alberto Marcus, 8.08.2018
    """
    lista[:] = [float(j) for j in lista] # garantir que a lista seja numeros.
    lista_ordenada = quicksort(lista)
    if len(lista) % 2 == 0:
        index = int(len(lista)/2)
        return (lista_ordenada[index] + lista_ordenada[index-1]) / 2
    else:
        index = round(len(lista)/2)
        return lista_ordenada[index]   
       
min_trip = achar_min(trip_duration_list)
max_trip = achar_max(trip_duration_list)        
mean_trip = media(trip_duration_list)
median_trip = mediana(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list,3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(start_stations)
print(len(start_stations))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
def new_function(param1: int, param2: str) -> list:
    """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.
    """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
      Função que detecta os diferentes elementos de uma lista e os conta.
      Argumentos:
          column_list: lista de itens a serem identificados.
      Retorna:
          Uma lista de itens - item_types.
          Uma lista com a contagem de cada item - count_items
    """
    item_types = []
    count_items = []
    find_type = set(column_list)
    item_types = list(find_type)
    for i in range(len(item_types)):
        contador = 0;
        for j in range(len(column_list)):
            if column_list[j] == item_types[i]:
                contador += 1
        count_items.append(contador)
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
