import pandas as pd
import pyodbc

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
    # ajustando as datas para 2021 e 2022
    data = (df['Mês'][i]).strftime('%Y-%m-%d')
    SK_Veiculo = df['SK_Veiculo'][i]
    SK_Motorista = df['SK_Motorista'][i]
    km_percorrido  = float(df['Km Percorrido'][i])
    Litros  = float(df['Litros'][i])
    comb  = float(df['Combustível'][i])
    manut  = float(df['Manutenção'][i])
    custo_fixo  = float(df['Custo Fixo'][i])
    
    script = f''' 
        INSERT INTO Fretes 
        (DATA_KM,SK_VEICULO,SK_Motorista,KM_PERCORRIDO,LITROS,COMBUSTIVEL,MANUTENCAO,CUSTO_FIXO)
        VALUES 
        ('{data}','{SK_Veiculo}','{SK_Motorista}',{km_percorrido},{Litros},{comb},{manut},{custo_fixo})
        
        '''

    
    cursor.execute(script)
    cursor.commit()