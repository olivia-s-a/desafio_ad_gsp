#DESAFIO 1 PARA PROCESSO SELETIVO DE ESTÁGIO EM ANÁLISE DE DADOS
#Governo da Cidade de São Paulo
#QUESTÃO 1
#CANDIDATA: OLÍVIA SILVA AMANN
#
# Importar o "pandas" e as tabelas
import pandas as pd
geosampa = pd.read_csv("geosampa_distritos.csv")
obs = pd.read_csv("observasampa_familias_extrema_pobreza.csv")
#
#QUESTÃO 1. Quantas famílias em situação de extrema pobreza existiam em São Paulo em 2023?
print("Questão 1")
dados_2023 = obs[obs["ano"]==2023]
soma_1 = dados_2023["qtd_familias"].sum()
#RESPOSTA:
print("A quantidade de famílias em situação de extrema pobreza que existiam em São Paulo em 2023 é de:", soma_1)
#
