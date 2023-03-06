import pandas as pd
import pyodbc
import time
import numpy as np

#  conexão com o banco de dados
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-RFSFG8V;"
    "Database=EmpresaLogistica;"
)

conexao  = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# importando as planilhas
cabecalho = ['Mês','SK_Veiculo','SK_Motorista','Km Percorrido','Litros','Combustível','Manutenção','Custo Fixo']
df = pd.read_excel('Base_de_Dados/fKMRodado.xlsx',names = cabecalho)
df.dropna(subset=cabecalho[1:8], inplace=True)
df = df[~df.isin(cabecalho).any(axis=1)]
df['Mês'] = pd.to_datetime(df['Mês'])
n = df.shape[0]

# percorrendo  a tabela
for i in range(n):
    data = (df['Mês'].iloc[i]).strftime('%Y-%m-%d')
    SK_Veiculo = df['SK_Veiculo'].iloc[i]
    SK_Motorista = df['SK_Motorista'].iloc[i]
    km_percorrido  = float(df['Km Percorrido'].iloc[i])
    Litros  = float(df['Litros'].iloc[i])
    comb  = float(df['Combustível'].iloc[i])
    manut  = float(df['Manutenção'].iloc[i])
    custo_fixo  = float(df['Custo Fixo'].iloc[i])
    
    script = f''' 
        INSERT INTO KMRodado 
        (DATA_KM,SK_VEICULO,SK_Motorista,KM_PERCORRIDO,LITROS,COMBUSTIVEL,MANUTENCAO,CUSTO_FIXO)
        VALUES 
        ('{data}','{SK_Veiculo}','{SK_Motorista}',{km_percorrido},{Litros},{comb},{manut},{custo_fixo})
        
        '''
    
    time.sleep(np.random.randint(2, 60))
    cursor.execute(script)
    cursor.commit()