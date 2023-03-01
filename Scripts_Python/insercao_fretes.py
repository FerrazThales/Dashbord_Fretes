import pandas as pd
import pyodbc
import time

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
    # ajustando as datas para 2021 e 2022
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
    script = f''' 
        INSERT INTO Fretes 
        (DATA_FISCAL,SK_CLIENTE,SK_VEICULO,DOC_FISCAL,COD_VIAGEM,Cod_IBGE,VALOR_FRETE,PESO_KG,PESO_CUBADO,VALOR_MERCADORIA)
        VALUES ('{data}','{SK_Cliente}','{SK_Veiculo}','{doc_fiscal}','{cod_viagem}','{cod_IBGE}',{valor_frete},{peso_kg},{peso_cubo},{valor_mercadoria})
        '''
    time.sleep(5)
    
    cursor.execute(script)
    cursor.commit()