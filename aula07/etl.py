import csv

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Funcao que lê um arquivo CSV e retorna uma lista de dicionários
    """

    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Soma todos os produtos da lista
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_produtos(lista: list[dict]) -> int:
    """
    Funcao que filtra produtos onde entrega = True
    """
    valor_total = 0
    for produto in lista:
        valor_total += int(produto.get("price"))
    return valor_total


