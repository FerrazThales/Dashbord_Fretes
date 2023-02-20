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
df = pd.read_excel('Excel/Cadastros.xlsx',sheet_name='Clientes')
n = df.shape[0]

# percorrendo  a tabela
for i in range(n):
    SK_Cliente = df['SK_Cliente'][i]
    Cidade = df['Cidade'][i]
    UF = df['UF'][i]
    cod_regiao = df['Cod Região'][i]
    cod_ibge =df['Cod IBGE'][i]
    
    script = f''' INSERT INTO CadClientes (SK_CLIENTE,Cidade,UF,Cod_Regiao,Cod_IBGE) VALUES 
                                                                            ('{SK_Cliente}', 
                                                                             '{Cidade}',
                                                                             '{UF}',
                                                                             '{cod_regiao}',
                                                                             '{cod_ibge}')'''
    cursor.execute(script)
    cursor.commit()