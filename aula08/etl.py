import pandas as pd
import os
import glob

# função de extract, que lê e consolida json
def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# função que transforma

def calcular_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# função que dá load em csv ou parquet
def carregar_dados(df: pd.DataFrame, formato_saida: list) -> None:
    for formato in formato_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet", index=False)

def pipeline_calcular_kpi_de_venda_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(path=pasta)
    data_frame_calculado = calcular_kpi_total_de_vendas(data_frame)
    carregar_dados(df=data_frame_calculado, formato_saida=formato_de_saida)
