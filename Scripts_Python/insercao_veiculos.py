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
df = pd.read_excel('Base_de_Dados/Cadastros.xlsx',sheet_name='Veículos')
n = df.shape[0]

# percorrendo  a tabela
for i in range(n):
    SK_VEICULO = df['SK_Veiculo'][i]
    Placa = df['Placa'][i]
    Marca = df['Marca'][i]
    tipo_veiculo = df['Tipo Veículo'][i]
    bau = df['Baú'][i]
    Ano = df['Ano'][i]
    
    script = f''' 
    INSERT INTO CadVeiculos 
        (SK_VEICULO,Placa,Marca,Tipo_Veiculo,Bau,Ano) 
    VALUES
    ('{SK_VEICULO}','{Placa}','{Marca}','{tipo_veiculo}','{bau}',{Ano})
               '''
    cursor.execute(script)
    cursor.commit()