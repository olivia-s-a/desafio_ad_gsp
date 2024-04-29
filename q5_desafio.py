#DESAFIO 1 PARA PROCESSO SELETIVO DE ESTÁGIO EM ANÁLISE DE DADOS
#Governo da Cidade de São Paulo
#QUESTÃO 5
#CANDIDATA: OLÍVIA SILVA AMANN
#
# Importar bibliotecas e as tabelas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


geosampa = pd.read_csv("geosampa_distritos.csv")
obs = pd.read_csv("observasampa_familias_extrema_pobreza.csv")
#
#QUESTÃO 5. Como variou o número de famílias em situação de pobreza entre 2013 e 2023 nos Distritos de Grajaú, Jardim Ângela, Cidade Ademar? Exiba graficamente o resultado, escolhendo a visualização que achar mais adequada.
print("Questão 5")
distritos = ['Grajaú', 'Jardim Ângela', 'Cidade Ademar']
#obs_dsano = obs[(obs['distrito'] == 'Grajaú') | (obs['distrito'] == 'Jardim Ângela') | (obs['distrito'] == 'Cidade Ademar') & (obs['ano'] >= 2013) & (obs['ano'] <= 2023)]
obs_dsano = obs[obs['distrito'].isin(distritos) & (obs['ano'] >= 2013) & (obs['ano'] <= 2023)]

print(obs_dsano)


#fazer um 'dicionário' pra armazenar as informações dos grupos como DataFrames
dici = {}

for nome in distritos:
    df_distrito = obs_dsano[obs_dsano['distrito'] == nome]
    # Armazenar o DataFrame do distrito no dicionário, usando o nome do distrito como chave
    dici[nome] = df_distrito

#print das tabelinhas
print('Tabelas:')
for nome, df_distrito in dici.items():
    print(f'Distrito: {nome}')
    print(df_distrito)
    print('\n')

print('Gráfico')
for nome, df_distrito in dici.items():
    plt.plot(df_distrito['ano'], df_distrito['qtd_familias'], label=nome)


plt.legend()

# Adicionando rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Quantidade de Famílias')
plt.title('Variação do número de famílias em situação de pobreza entre 2013 e 2023')

# Exibindo o gráfico
plt.grid(True)
plt.show()