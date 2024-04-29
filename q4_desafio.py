#DESAFIO 1 PARA PROCESSO SELETIVO DE ESTÁGIO EM ANÁLISE DE DADOS
#Governo da Cidade de São Paulo
#QUESTÃO 4
#CANDIDATA: OLÍVIA SILVA AMANN
#
# Importar bibliotecas e as tabelas
import pandas as pd
import numpy as np
geosampa = pd.read_csv("geosampa_distritos.csv")
obs = pd.read_csv("observasampa_familias_extrema_pobreza.csv")
#
#QUESTÃO 4. Quantas famílias em situação de extrema pobreza existiam em cada Subprefeitura de São Paulo em 2023?

print("Questão 4")

#filtrar por ano
obs_2023 = obs[obs['ano'] == 2023]

# Mesclar as tabelas apenas pelos dados de 2023
tabela_q4 = pd.merge(geosampa, obs_2023, on='ds_nome', how='right')

# Agora, agrupar e somar as famílias por subprefeitura
soma_por_sub = tabela_q4.groupby('ds_subpref')['qtd_familias'].sum()

# Convertendo a Série em DataFrame
tabela_resposta = pd.DataFrame(soma_por_sub)


# colocando índice
tabela_resposta.reset_index(inplace=True)

#Resposta:
print(tabela_resposta)

