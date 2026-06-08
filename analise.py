import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('launches.csv')
df.columns = df.columns.str.strip()

df_rocket = pd.to_numeric(df['Rocket'], errors='coerce').dropna()

k = int(1 + 3.322 * np.log10(len(df_rocket)))
print('Número de classes:', k)
classes = pd.cut(df_rocket, bins=k)

fa = df['Year'].value_counts().sort_index()
total = len(df)
fr = fa / total
fr_pct = fr * 100
Fa = fa.cumsum()

fa_c = classes.value_counts().sort_index()
total_c = len(df_rocket)
fr_c = fa_c / total_c
fr_pct_c = fr_c * 100
Fa_c = fa_c.cumsum()



tabela_discreta = pd.DataFrame({
    'fa': fa,
    'fr': fr.round(4),
    'fr%': fr_pct.round(2),
    'Fa': Fa
})

tabela_discreta.index.name = 'Ano'

tabela_continua = pd.DataFrame({
    'fa': fa_c,
    'fr': fr_c.round(4),
    'fr%': fr_pct_c.round(2),
    'Fa': Fa_c
})

tabela_continua.index.name = 'Custo (milhões $)'


print(tabela_discreta)
print(tabela_continua)

plt.figure(figsize=(14, 6))
plt.bar(fa.index, fa.values, color='pink')
plt.title('Lançamentos Espaciais por Ano (1957–2020)')
plt.xlabel('Ano')
plt.ylabel('Número de Lançamentos')
plt.tight_layout()
plt.savefig('grafico_barras.png', dpi=150, bbox_inches='tight')
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(df_rocket, bins=k, color='pink', edgecolor='black')
plt.title('Distribuição de Custos de Lançamentos Espaciais')
plt.xlabel('Custo (milhões de dólares)')
plt.ylabel('Número de Lançamentos')
plt.tight_layout()
plt.savefig('histograma.png', dpi=150, bbox_inches='tight')
plt.show()

print('\n=== ANÁLISE UNIVARIADA — ANO ===')

media_ano = df['Year'].mean()
mediana_ano = df['Year'].median()
moda_ano = df['Year'].mode()[0]

print(f'Média: {media_ano:.2f}')
print(f'Mediana: {mediana_ano:.2f}')
print(f'Moda: {moda_ano}')

maximo_ano = df['Year'].max()
minimo_ano = df['Year'].min()
amplitude_ano = maximo_ano - minimo_ano
variancia_ano = df['Year'].var()
desvio_ano = df['Year'].std()
cv_ano = (desvio_ano / media_ano) * 100

print(f'Máximo: {maximo_ano}')
print(f'Mínimo: {minimo_ano}')
print(f'Amplitude: {amplitude_ano}')
print(f'Variância: {variancia_ano:.2f}')
print(f'Desvio Padrão: {desvio_ano:.2f}')
print(f'Coeficiente de Variação: {cv_ano:.2f}%')

q1_ano = df['Year'].quantile(0.25)
q2_ano = df['Year'].quantile(0.50)
q3_ano = df['Year'].quantile(0.75)

print(f'Q1: {q1_ano}')
print(f'Q2 (Mediana): {q2_ano}')
print(f'Q3: {q3_ano}')

print('\n=== ANÁLISE UNIVARIADA — CUSTO (ROCKET) ===')

media_r = df_rocket.mean()
mediana_r = df_rocket.median()
moda_r = df_rocket.mode()[0]

print(f'Média: {media_r:.2f}')
print(f'Mediana: {mediana_r:.2f}')
print(f'Moda: {moda_r:.2f}')

maximo_r = df_rocket.max()
minimo_r = df_rocket.min()
amplitude_r = maximo_r - minimo_r
variancia_r = df_rocket.var()
desvio_r = df_rocket.std()
cv_r = (desvio_r / media_r) * 100

print(f'Máximo: {maximo_r:.2f}')
print(f'Mínimo: {minimo_r:.2f}')
print(f'Amplitude: {amplitude_r:.2f}')
print(f'Variância: {variancia_r:.2f}')
print(f'Desvio Padrão: {desvio_r:.2f}')
print(f'Coeficiente de Variação: {cv_r:.2f}%')

q1_r = df_rocket.quantile(0.25)
q2_r = df_rocket.quantile(0.50)
q3_r = df_rocket.quantile(0.75)

print(f'Q1: {q1_r:.2f}')
print(f'Q2 (Mediana): {q2_r:.2f}')
print(f'Q3: {q3_r:.2f}')


