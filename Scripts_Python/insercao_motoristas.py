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
df = pd.read_excel('Base_de_Dados/Cadastros.xlsx',sheet_name='Motoristas')
n = df.shape[0]

# percorrendo  a tabela
for i in range(n):
    SK_Motorista = df['SK_Motorista'][i]
    Motorista = df['Motorista'][i]
    script = f''' 
    INSERT INTO CadMotoristas (SK_MOTORISTA,MOTORISTA) 
    VALUES ('{SK_Motorista}', '{Motorista}')
        '''
    cursor.execute(script)
    cursor.commit()