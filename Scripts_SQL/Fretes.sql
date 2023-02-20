CREATE TABLE Fretes
(
	ID_TABLE INT PRIMARY KEY IDENTITY (1,1),
	DATA_FISCAL DATE,
	SK_CLIENTE VARCHAR(50),
    SK_VEICULO VARCHAR(50),
    DOC_FISCAL VARCHAR(100) NOT NULL,
    COD_VIAGEM VARCHAR(100),
    Cod_IBGE VARCHAR(30),
    VALOR_FRETE FLOAT,
    PESO_KG FLOAT,
    PESO_CUBADO FLOAT,
    VALOR_MERCADORIA FLOAT
)