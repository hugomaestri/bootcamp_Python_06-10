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

### Exercício 4
# Converter Celsius para Fahrenheit em uma Lista
# def converter_Celsius_para_Fahrenheit(lista: list[float]) -> list[float]:
#     return [(valor * 9/5) + 32 for valor in lista]

# lista_temperatura_celsius = [0, 25, 21.2, 48.7]
# print(converter_Celsius_para_Fahrenheit(lista_temperatura_celsius))

### Exercício 5
# Calcular Desvio Padrão de uma Lista
# def calcular_desvio_padrao(lista: list[float]) -> float:
#     media_lista = sum(lista) / len(lista)
#     variancia = (sum((valor - media_lista)**2 for valor in lista)) / len(lista)
#     desvio_padrao = variancia ** (1/2)
#     return desvio_padrao


# lista_teste = [10, 40, 25, 55, 61, 102.3, 22.5, 99.9]
# print(calcular_desvio_padrao(lista_teste))

### Exercício 6
# Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(lista: list[int]) -> int:
    lista_completa = set(range(min(lista), max(lista) + 1))
    return sorted(list(lista_completa - set(lista)))

lista_teste = [1, 2, 2, 4, 4, 5, 6, 6, 7, 9]
print(encontrar_valores_ausentes(lista_teste))