import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Arquivo com pré-Tratamento de dados
read_excel = pd.read_excel('dados_trabalho_ajustado.xlsx')

df = pd.DataFrame(read_excel)

# Tratamento de dados
# Transformar a coluna 'Matricula' em índice
df = df.set_index("Matricula")

# Coluna '515088'
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