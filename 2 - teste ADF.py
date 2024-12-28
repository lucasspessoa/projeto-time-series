import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Arquivo com pré-Tratamento de dados
read_excel = pd.read_excel('dados_trabalho_ajustado.xlsx')

df = pd.DataFrame(read_excel)

# Tratamento de dados
# Transformar a coluna 'Matricula' em índice
df = df.set_index("Matricula")

# Coluna '515088'
df = df[[515088]]

# Questão2 - Teste ADF e realização de Diferenciação para estacionariedade
# Realizando o teste ADF
adf_result = adfuller(df)

# Exibindo os resultados
print("Estatística ADF:", adf_result[0]) # Valores menores indicam maior evidência de estacionariedade
print("p-valor:", adf_result[1])
print("Número de Lags Utilizados:", adf_result[2])
print("Número de Observações:", adf_result[3])
print("Valores Críticos:") # Valores críticos para diferentes níveis de significância (1%, 5%, 10%)
for key, value in adf_result[4].items():
    print(f"  {key}: {value:.3f}")

# Teste de Hipótese para verificação de Estacionariedade
# Interpretação do p-valor: existe raiz unitária?
if adf_result[1] <= 0.05:
    print("\nA série é estacionária (Rejeitamos H0).")
else:
    print("\nA série não é estacionária (Não rejeitamos H0).")