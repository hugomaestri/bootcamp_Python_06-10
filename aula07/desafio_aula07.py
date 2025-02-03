## Analise de vendas de produtos
# Ler CSV
# Processar dados
# Filtrar produtos en
# Exibir resultados

from etl import ler_csv, filtrar_produtos_entregues, somar_valores_produtos

path_arquivo = "vendas.csv"

lista_produtos = ler_csv(path_arquivo)
print(lista_produtos)
produtos_entregues = filtrar_produtos_entregues(lista_produtos)
print(produtos_entregues)

valor_produtos_entregues = somar_valores_produtos(produtos_entregues)
print(valor_produtos_entregues)