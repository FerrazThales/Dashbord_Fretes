CREATE TABLE CadVeiculos
(
	ID_TABLE INT PRIMARY KEY IDENTITY (1,1),
	SK_VEICULO VARCHAR(50) NOT NULL,
	Placa VARCHAR(10),
    Marca VARCHAR(4),
    Tipo_Veiculo VARCHAR(10) NOT NULL,
    Bau VARCHAR(20),
    Ano INT
)