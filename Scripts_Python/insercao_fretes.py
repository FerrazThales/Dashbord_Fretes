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
df = pd.read_csv('Base_de_Dados/fFrete.csv')
n = df.shape[0]

# percorrendo  a tabela
for i in range(n):
    data = df['Data']
    SK_Cliente = df['SK_Cliente'][i]
    SK_VEICULO = df['SK_Veiculo'][i]
    doc_fiscal  = df['Numero Documento Fiscal'][i]

    print(data)
    #script = f''' INSERT INTO CadClientes (SK_CLIENTE,Cidade,UF,Cod_Regiao,Cod_IBGE) VALUES 
     #                                                                       ('{SK_Cliente}', 
     #                                                                        '{Cidade}',
     #                                                                        '{UF}',
     #                                                                        '{cod_regiao}',
     #                                                                        '{cod_ibge}')'''
    # cursor.execute(script)
    # cursor.commit()