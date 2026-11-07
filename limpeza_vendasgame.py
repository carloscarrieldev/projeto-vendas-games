# BIBLIOTECA
import pandas as pd

# Visualização das colunas
pd.set_option('display.max_columns', None)

# Lendo arquivo
df = pd.read_csv('vendas_videogame.csv')

# LIMPEZA

# Verificando colunas
print('Visualização:\n', df.head(30))
print('Valores nulos:\n', df.isnull().sum())
print('Duplicatas:\n', df.duplicated().sum())
print('Informações:\n', df.info())
print('Tipos:\n', df.dtypes)

# Alterando formato de coluna
df['Year'] = df['Year'].astype('Int64')

# Verificando nomes de colunas
print(df['Genre'].unique())
print(df['Platform'].unique())
print(df['Publisher'].unique())
print(df['Rank'].unique())
print(df['Name'].unique())

# Valores nulos encontrados
print('Colunas nulas:\n',df[df['Year'].isnull()][['Year', 'Publisher']])

# Criando colunas colunas para analise
# America + Europa
df['Vendas_Região'] = df['NA_Sales'] + df['EU_Sales']
# America, Europa + Venda Global mostrando em porcentagem
df['Percentual_Vendas'] = (df['Vendas_Região'] / df['Global_Sales']) * 100
# Criando coluna para região
df_regiao = df.melt(
    id_vars = ['Name', 'Genre','Platform','Publisher', 'Year','Percentual_Vendas'],
    var_name= 'regiao',
    value_vars = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
)

# SALVAMENTO
df.to_csv('output/games/vendasgames_limpos.csv', index=False)
df_regiao.to_csv('output/games/regiões.csv', index= False)

# Visualizando tabela nova
print('Tabela Atualizada:\n', pd.read_csv('output/games/vendasgames_limpos.csv').head(10))
print(df.columns.tolist())
