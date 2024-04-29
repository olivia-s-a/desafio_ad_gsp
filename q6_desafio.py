#DESAFIO 1 PARA PROCESSO SELETIVO DE ESTÁGIO EM ANÁLISE DE DADOS
#Governo da Cidade de São Paulo
#QUESTÃO 6
#CANDIDATA: OLÍVIA SILVA AMANN
#
# Importar bibliotecas e as tabelas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


geosampa = pd.read_csv("geosampa_distritos.csv")
obs = pd.read_csv("observasampa_familias_extrema_pobreza.csv")
#
#QUESTÃO 6. Complete a seguinte frase: "De acordo com os dados do ObservaSampa, em 2023 metade dos Distritos de São Paulo, no máximo, ___ famílias em situação de extrema pobreza". Qual informação você utilizou par acompletar a frase
print("Questão 6")

obs2023_sort = obs[obs['ano'] == 2023].sort_values(by='qtd_familias', ascending=False)
metade_linhas = len(obs2023_sort) // 2
linhas_1 = obs2023_sort.head(metade_linhas)
soma_max_mid = linhas_1['qtd_familias'].sum()

#print("sort 2023", obs2023_sort)
#print ("só a metade", linhas_1)
#print("soma =", soma_max_mid)

#resposta
x = "tinha " + str(soma_max_mid)
print("De acordo com os dados do ObservaSampa, em 2023 metade dos Distritos de São Paulo, no máximo,", x, "famílias em situação de extrema pobreza")
#explicação
print("A informação utilizada para completar a frase foi a soma da quantidade de famílias em situação de extrema pobreza de metade dos distritos de São Paulo.")
print('Os distritos escolhidos foram os com a maior qauntidade de famílias.') 





