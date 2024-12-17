import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

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

# Questão3 - Correlogramas de ACF e PACF: identificação de alta persistência e sazonalidade
# Gráficos de ACF e PACF
plt.figure(figsize=(14, 6))

# ACF
plt.subplot(1, 2, 1)
plot_acf(df, lags=24, ax=plt.gca())
plt.title("ACF (Autocorrelação)", fontsize=14)

# PACF
plt.subplot(1, 2, 2)
plot_pacf(df, lags=24, ax=plt.gca(), method='ywm')
plt.title("PACF (Autocorrelação Parcial)", fontsize=14)

plt.tight_layout()
plt.show()