SELECT
	-- COLUNAS DO Fretes
	F.DATA_FISCAL, F.DOC_FISCAL, F.Cod_IBGE, F.VALOR_FRETE, F.PESO_KG, F.VALOR_MERCADORIA,
	-- COLUNAS DO CadClientes
	CC.Cidade + ' - ' + CC.UF AS LOCAL,
	-- COLUNAS DO CadVeiculos
	CV.Placa, CV.Marca, CV.Tipo_Veiculo, CV.Bau, CV.Ano,
	-- Horário de Inserção
	F.TEMPO_DE_INSERCAO, CAST(CONVERT(VARCHAR(8), F.TEMPO_DE_INSERCAO, 108)AS TIME) AS Horario
FROM Fretes F
INNER JOIN CadClientes CC ON
	F.SK_CLIENTE = CC.SK_CLIENTE
INNER JOIN CadVeiculos CV ON
	F.SK_VEICULO = CV.SK_VEICULO