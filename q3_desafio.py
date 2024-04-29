#DESAFIO 1 PARA PROCESSO SELETIVO DE ESTÁGIO EM ANÁLISE DE DADOS
#Governo da Cidade de São Paulo
#QUESTÃO 3
#CANDIDATA: OLÍVIA SILVA AMANN
#
# Importar bibliotecas e as tabelas
import pandas as pd
import numpy as np
geosampa = pd.read_csv("geosampa_distritos.csv")
obs = pd.read_csv("observasampa_familias_extrema_pobreza.csv")
#
#QUESTÃO 3. Qual distrito apresentou o maior aumento de famílias em situação de pobreza entre 2022 e 2023?
print("Questão 3")
lista = []

for index, row in obs.iterrows():
    ds= row['ds_nome']
    ds_v = obs.loc[obs['ds_nome'] == ds]
    v_2022 = ds_v.loc[ds_v['ano'] == 2022]
    v_2023 = ds_v.loc[ds_v['ano'] == 2023]

    if not ds_v.empty & v_2022.empty & v_2023.empty:
        qtd_2023 = v_2023.loc[v_2023['ano'] == 2023, 'qtd_familias'].values
        qtd_2022 = v_2022.loc[v_2022['ano'] == 2022, 'qtd_familias'].values
        aumento = qtd_2023 - qtd_2022
        
        #adiciona os dados na lista
        lista.append({'ds_nome': ds, 'qtd_2022': qtd_2022, 'qtd_2023': qtd_2023, 'aumento': aumento})

    else:
        lista.append({'ds_nome': ds, 'qtd_2022': np.nan, 'qtd_2023': np.nan, 'aumento': np.nan})

#transforma a lista criada em um Data Frame 
tabela_q3 = pd.DataFrame(lista)
print(tabela_q3)

tabela_q3['aumento'] = tabela_q3['aumento'].astype(float)
ds_maior = tabela_q3.loc[tabela_q3['aumento'].idxmax(), 'ds_nome']


maior = tabela_q3['aumento'].max()
menor = tabela_q3['aumento'].min()

#Resposta:
print(ds_maior, " teve um aumento de ", maior, "famílias, e foi o distrito com maior aumento entre 2022 e 2023")

