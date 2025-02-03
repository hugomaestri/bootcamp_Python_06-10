## Analise de vendas de produtos

from etl import ler_csv, filtrar_produtos_entregues, somar_valores_produtos

path_arquivo = "vendas.csv"

lista_produtos = ler_csv(path_arquivo)
print(f"Lista de produtos: {lista_produtos}")

produtos_entregues = filtrar_produtos_entregues(lista_produtos)
print(f"\nLista de produtos entregues: {produtos_entregues}")

valor_produtos_entregues = somar_valores_produtos(produtos_entregues)
print(f"\nO valor dos produtos entregues é de: R$ {valor_produtos_entregues:.2f}")