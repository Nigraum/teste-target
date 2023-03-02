import pandas as pd
from pandasql import sqldf

path = "dados.json"
dados = pd.read_json(path)
df = pd.DataFrame(dados, columns=['dia', 'valor'])
avgMonth = df['valor'].mean()
zeroIgnore = df.loc[df['valor'] != 0]
lowerValue = zeroIgnore['valor'].min()
maxValue = df['valor'].max()
daysAboveAvg = (df['valor'] > avgMonth).sum()


print(f'Menor valor de faturamento: R$ {lowerValue:.2f}')
print(f'Maior valor de faturamento: R$ {maxValue:.2f}')
print(
    f'Número de dias que o faturamento foi superior a média mensal: {daysAboveAvg}')
