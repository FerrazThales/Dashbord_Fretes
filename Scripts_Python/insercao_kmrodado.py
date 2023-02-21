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
df = pd.read_excel('fKMRodado.xlsx',names = cabecalho)
df.dropna(subset=cabecalho[1:8], inplace=True)
df = df[~df.isin(cabecalho).any(axis=1)]
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
        (DATA_FISCAL,SK_CLIENTE,SK_VEICULO,DOC_FISCAL,COD_VIAGEM,Cod_IBGE,VALOR_FRETE,
        PESO_KG,PESO_CUBADO,VALOR_MERCADORIA)
        VALUES 
        ('{data}','{SK_Cliente}','{SK_Veiculo}','{doc_fiscal}','{cod_viagem}','{cod_IBGE}',
        {valor_frete},{peso_kg},{peso_cubo},{valor_mercadoria})'''

    
    cursor.execute(script)
    cursor.commit()