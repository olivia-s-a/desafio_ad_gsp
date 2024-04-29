#DESAFIO 1 PARA PROCESSO SELETIVO DE ESTÁGIO EM ANÁLISE DE DADOS
#Governo da Cidade de São Paulo
#QUESTÃO 2
#CANDIDATA: OLÍVIA SILVA AMANN
#
# Importar bibliotecas e as tabelas
import pandas as pd
import numpy as np
geosampa = pd.read_csv("geosampa_distritos.csv")
obs = pd.read_csv("observasampa_familias_extrema_pobreza.csv")
#
#QUESTÃO 2. Qual o percentual (em relação ao total da cidade) de famílias em situação de extrema pobreza por Distrito em 2023?
print("Questão 2")
###encontrar o total de famílias em 2023 em SP (como na questão 1):
dados_2023 = obs[obs["ano"]==2023]
soma_1 = dados_2023["qtd_familias"].sum()

###tabela para a apresentação dos dados
###    primeiro precisa criar a lista
apresenta = []

for index, row in geosampa.iterrows():
    ds = row['ds_nome']
    ds_2023 = obs.loc[(obs['ds_nome'] == ds) & (obs['ano'] == 2023)] 
#definir ds_2023 como a(s) linha(s) onde ds_nome é ds e o ano é 2023
    
    if not ds_2023.empty:
        familias = ds_2023['qtd_familias'].values
        percentual = (familias/soma_1)*100
        perc = np.round(percentual, 2) #arredonda e deixa apenas 2 casas depois da vírgula
        perc_form = np.vectorize(lambda x: "{:.2f}%".format(x))(perc) #coloca "%" no resultado de perc, para a vizualização
        
        #adiciona o perc_form à lista
        apresenta.append({'ds_nome': ds, 'percentual': perc_form})
        
                                                    
    else:
        apresenta.append({'ds_nome': ds, 'percentual': "Não encontrado"})

#transforma a lista criada em um Data Frame 
tabela_q2 = pd.DataFrame(apresenta)
#RESPOSTA:
print(tabela_q2)



#prova real
#soma_pr2 = tabela_q2['percentual'].sum()
#print("prova real = ", soma_pr2)
#
### OBS: A prova real só funciona desabilitando quando os valores de 'percentual' são perc, não perc_form
    


