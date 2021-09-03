#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# ### Passo a passo
# 1- Importar a base de dados;
# 
# 2- Visualizar a base (verificar as informações e apurar os possíveis erros);
# 
# 3- Tratar a base (correção de pendências - valores vazios, valores numéricos lidos como texto, etc);
# 
# 4- Análise inicial dos dados (análise exploratória);
# 
# 5- Verificar cada característica da base (clientes, caso) e ver como as informações estão relacionadas com o problema a ser solucinado (alta de cancelamento dos clientes - churn).

# In[1]:


import pandas as pd

tabela = pd.read_csv("telecom_users.csv")


display(tabela)


# ### Problemas!
# 
# #Coluna Unnamed é inútil (informação que não ajuda em nada);
# 
# #Ver se tem coluna numérica sendo reconhecida como texto - print (tabela.info());
# 
# #A coluna Código tem valor vazio (NaN).
# 

# In[2]:


print(tabela.info())


# In[3]:


### Correções

# 1- Deletar a coluna Unnamed
# 2- Transformar a culuna TotalGasto em float64
# 3- Ver colunas vazias e excluir


# In[4]:


#Correção 1

tabela = tabela.drop("Unnamed: 0", axis = 1)
display (tabela)


# In[5]:


#Corrigido!
#Correção 2 agora
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors = "coerce")
print(tabela.info())


# In[6]:


#Correção 2 feita
#Correção 3 - tratar os campos vazios 
#primeiro as colunas totalmente vazias - vamos usar um método geral de limpeza

tabela = tabela.dropna(how="all", axis=1)

#e para excluir linhas que contenham algum valor vazio - lembrando que a exclusão de cada linha aqui representa a exclusão de dados relativos a um usuário na tabela;
#esse tipo de exclusão tem que ser feita com cuidado - nesse exemplo, não há prejuízo pela exclusão das linhas - 12, de um total de 5986, porque o impacto geral nos dados é baixo.

tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())


# In[12]:


#Passo 4 - Começo da análise - exploração
#Por que os cancelamentos?

display(tabela["Churn"].value_counts())

display(tabela["Churn"].value_counts(normalize=True))


# In[22]:


#Passo 5 - Mais exploração, verificar outras características em conjunto

import plotly.express as px

for coluna in tabela:
    if coluna != "IDCliente":
        # criar a figura
        fig = px.histogram(tabela, x=coluna, color="Churn")
        # exibir a figura
        fig.show()
        display(tabela.pivot_table(index="Churn", columns=coluna, aggfunc='count')["IDCliente"])


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
# 
# Clientes com famílias maiores tedem a cancelar menos;
# 
# MesesComoCliente baixo apresenta alta proporção de cancelamentos - 
# 
#     Possível problema com a retenção de clientes nos primeiros meses,
#     Sugestão: criação de programas, incentivos para manutenção de clientes nos primeiros meses de contrato;
#     
#     Possível problema com a captação de cliente,
#     Sugestão: revisar os benefícios decorrentes dos programas de captação;
#     
# Clientes Fibra tem alta taxa de cancelamento;
# 
#     Verificar possíveis problemas com o serviço de fibra;
# 
# Clientes sem serviços adicionais ou serviços de suporte tem alta taxa de cancelamento;
# 
#     Oportunidade para oferecimento dos serviços com bônus e desconto para diminuir a taxa de cancelamentos;
#     
# Clientes com Contrato Mensal tem alta taxa de cancelamento;
# 
#     Incentivar o cliente para aderir ao plano anual;
# 
# Cliente com FormaDePagamento Boleto Eletrônico tem alta taxa de cancelamento;
#     
#     Incentivar (oferecer eventuais) para adesão ao débito automático como forma de pagamento.
#     
