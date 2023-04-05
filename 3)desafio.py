import json

# Lê o arquivo JSON com os dados de faturamento diário
with open('dados.json') as file:
    faturamento_diario = json.load(file)

# Inicializa as variáveis com o primeiro valor do vetor de faturamento diário
menor_faturamento = faturamento_diario[0]
maior_faturamento = faturamento_diario[0]
soma_faturamento = faturamento_diario[0]

# Itera sobre o vetor de faturamento diário para encontrar o menor, o maior valor e a soma total do faturamento
for valor in faturamento_diario[1:]:
    if valor < menor_faturamento:
        menor_faturamento = valor
    elif valor > maior_faturamento:
        maior_faturamento = valor
    soma_faturamento += valor

# Calcula a média mensal de faturamento, ignorando os dias sem faturamento (valores iguais a 0)
media_mensal = soma_faturamento / len([valor for valor in faturamento_diario if valor != 0])

# Calcula o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len([valor for valor in faturamento_diario if valor > media_mensal])

# Imprime os resultados
print(f"Menor valor de faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento diário acima da média mensal: {dias_acima_da_media}")