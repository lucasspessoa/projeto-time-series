import pandas as pd
from statsmodels.tsa.stattools import adfuller

read_excel = pd.read_excel('dados_trabalho1.xlsx')

df = pd.DataFrame(read_excel)

# Tratamento de dados
# Definir a primeira linha como cabeçalho
df.columns = df.iloc[0]  # Transforma a primeira linha em cabeçalho
df = df[1:]  # Remove a linha que virou cabeçalho
df = df.reset_index(drop=True)  # Reseta o índice, se necessário

# Remover a linha de índice 0
df = df.drop(0).reset_index(drop=True)  # Reseta o índice para evitar gaps

# Transformar a coluna 'Matricula' em índice
df = df.set_index("Matricula")

# Manter apenas coluna '515088' typeInt
df = df[[515088]]

# Questão2 - Teste ADF e realização de Diferenciação para estacionariedade
# Realizando o teste ADF
adf_result = adfuller(df)

# Exibindo os resultados
print("Estatística ADF:", adf_result[0]) # Valores menores indicam maior evidência de estacionariedade
print("p-valor:", adf_result[1]) # Se for menor que 0.05, rejeitamos a hipótese nula (H0) de que a série possui uma raiz unitária (não estacionária)
print("Número de Lags Utilizados:", adf_result[2])
print("Número de Observações:", adf_result[3])
print("Valores Críticos:") # Valores críticos para diferentes níveis de significância (1%, 5%, 10%)
for key, value in adf_result[4].items():
    print(f"  {key}: {value:.3f}")

# Interpretação do p-valor
if adf_result[1] <= 0.05:
    print("\nA série é estacionária (Rejeitamos H0).")
else:
    print("\nA série não é estacionária (Não rejeitamos H0).")