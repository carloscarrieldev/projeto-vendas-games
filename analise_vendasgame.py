# BIBLIOTECA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mostrando todas colunas
pd.set_option('display.max_columns', None)

# Lendo arquivo
df = pd.read_csv('vendas_videogame.csv')

# Verificando dados é colunas
print('Visualização:\n',df.head(10))
print('Estrutura dos dados:\n', df.shape)
print('Colunas:\n',df.columns.tolist())

# 5 Analises exploratorias

# GRAFICOS E VISUALIZAÇÕES

# Analise distribuições das vendas
# Grafico Histograma
plt.figure(figsize = (10, 6))
plt.hist(df['Global_Sales'], bins=30, color='Black')
plt.title('Distribuição de Vendas')
plt.xlabel('Vendas')
plt.ylabel('Quantidade')
plt.show()

# Correlações entre as vendas por Região
# Grafico Dispersão
plt.figure(figsize = (10,6))
plt.scatter(y = df['NA_Sales'], x = df['EU_Sales'], color='Green')
plt.title('Dispersão entre America x Norte')
plt.ylabel('Vendas - America')
plt.xlabel('Vendas - Europa')
plt.show()

# Analise de valores alto nas vendas
# Grafico de Caixa
plt.figure(figsize= (10, 6))
plt.boxplot(df['Global_Sales'])
plt.title('Outliers nas Vendas')
plt.ylabel('Vendas')
plt.ylim(0, 5)
plt.show()

# Juntando colunas para visualização
correlacao_vendas = df[['NA_Sales', 'EU_Sales', 
'JP_Sales', 'Other_Sales', 'Global_Sales']].corr()

# Analise valores entre colunas
# Grafico Correlação
plt.figure(figsize=(10, 6))
sns.heatmap(correlacao_vendas, annot=True)
plt.title('Correlações entre Regiões')
plt.show()

# Analisando valores da Media é Mediana
media_vendas = df['Global_Sales'].mean()
mediana_vendas = df['Global_Sales'].median()
# Criando tabela para exibição dos valores
media = pd.DataFrame({ 'Valores': ['Media', 'Mediana'],
                        'Vendas': [media_vendas,mediana_vendas],
})
print(media)
