def soma(valor_1: float, valor_2: float) -> float:
    """
    Uma função simples que soma dois valores e retorna o resultado.
    """
    valor_3 = valor_1 + valor_2
    return valor_3

def soma_com_valor_fixo(valor_1: float, valor_2: float = 10) -> float:
    """
    Uma função simples que soma dois valores e retorna o resultado.
    """
    valor_3 = valor_1 + valor_2
    return valor_3

valor_1 = 10
valor_2 = 5

resultado = soma(valor_1=valor_1, valor_2=valor_2)
print(resultado)

resultado_2 = soma_com_valor_fixo(valor_1=valor_1)
resultado_3 = soma_com_valor_fixo(valor_1=valor_1, valor_2=15)
print(resultado_2)
print(resultado_3)