CREATE TABLE CadMotoristas
(
	ID_TABLE INT PRIMARY KEY IDENTITY (1,1),
	SK_Motorista VARCHAR(50) NOT NULL,
	Motorista VARCHAR(100),
	HORARIO_INSERCAO datetime default getdate()
)