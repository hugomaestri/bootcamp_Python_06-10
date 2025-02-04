### Exercicio 1
# Calcular Média de Valores em uma Lista
# def calcular_media_de_lista(lista: list[float]) -> float:
#     media = sum(lista) / len(lista)
#     return media

# lista_teste = [10, 40, 25, 55, 61]
# print(calcular_media_de_lista(lista_teste))

### Exercicio 2
# Filtrar Dados Acima de um Limite
# def filtrar_dados_acima_valor(dados: list[float], limite: float) -> float:
#     return [valor for valor in dados if valor > limite]

# lista_teste = [10, 40, 25, 55, 61, 102.3, 22.5, 99.9]
# valor_limite = 39.9
# print(filtrar_dados_acima_valor(dados=lista_teste, limite=valor_limite))

### Exercicio 3
# Contar Valores Únicos em uma Lista
# from typing import Any

# def contar_valores_unicos(lista: list[Any]) -> int:
#     valores_unicos = {}
#     for valor in lista:
#         if valor in valores_unicos:
#             valores_unicos[valor] += 1
#         else:
#             valores_unicos[valor] = 1
    
#     print(f"Dicionarios contendo a quantidade de ocorrências:")
#     print(valores_unicos)

#     return len(set(lista))

# lista_teste = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8]
# qtd_valores_unicos = contar_valores_unicos(lista_teste)
# print(f"A quantidade de valores únicos é: {qtd_valores_unicos} e a quantidade total de itens é {len (lista_teste)}")