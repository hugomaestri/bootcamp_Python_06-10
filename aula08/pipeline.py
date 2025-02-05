from etl import pipeline_calcular_kpi_de_venda_consolidado

pasta: str = "data"
formato_de_saida: list = ["csv", "parquet"]

pipeline_calcular_kpi_de_venda_consolidado(pasta=pasta, formato_de_saida=formato_de_saida)