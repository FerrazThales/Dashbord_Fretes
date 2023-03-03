import pandas as pd
import pyodbc
import numpy as np
from datetime import datetime
import time

# criação lista de situações do documento emitido
doc = ['C','P','R']

#  conexão com o banco de dados
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-RFSFG8V;"
    "Database=EmpresaLogistica;"
)

conexao  = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# importando as planilhas
df = pd.read_csv('Base_de_Dados/fFrete.csv',encoding='UTF-16',sep='\t',parse_dates=['Data'],
                 decimal=',' , date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y'))
n = df.shape[0]

# percorrendo  a tabela
for i in range(n):
    data = (df['Data'][i]).strftime('%Y-%m-%d')
    SK_Cliente = df['SK_Cliente'][i]
    SK_Veiculo = df['SK_Veiculo'][i]
    doc_fiscal  = df['Numero Documento Fiscal'][i]
    cod_viagem  = df['Viagem'][i]
    cod_IBGE  = df['Cod IBGE'][i]
    valor_frete  = df['Valor do Frete Líquido'][i]
    peso_kg  = df['Peso (KG)'][i]
    peso_cubo  = df['Peso (Cubado)'][i]
    valor_mercadoria  = df['Valor da Mercadoria'][i]
    Tempo_de_insercao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sit = np.random.choice(doc,p=[0.8,0.15,0.05])
    
    script = f''' 
        INSERT INTO Fretes 
        (DATA_FISCAL,SK_CLIENTE,SK_VEICULO,DOC_FISCAL,COD_VIAGEM,Cod_IBGE,VALOR_FRETE,PESO_KG,PESO_CUBADO,VALOR_MERCADORIA,TEMPO_DE_INSERCAO,SITUACAO)
        VALUES ('{data}','{SK_Cliente}','{SK_Veiculo}','{doc_fiscal}','{cod_viagem}','{cod_IBGE}',{valor_frete},{peso_kg},{peso_cubo},{valor_mercadoria},'{Tempo_de_insercao}','{sit}')
        '''
    time.sleep(np.random.randint(2, 60))
    
    cursor.execute(script)
    cursor.commit()