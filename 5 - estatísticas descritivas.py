import pandas as pd
import statsmodels.tsa.api as tsa
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Arquivo com pré-Tratamento de dados
read_excel = pd.read_excel('dados_trabalho_ajustado.xlsx')

df = pd.DataFrame(read_excel)

# Tratamento de dados
# Transformar a coluna 'Matricula' em índice
df = df.set_index("Matricula")

# Coluna '515088'
df = df[[515088]]

# Questão5 - Comportamento dos resíduos e significância dos parâmetros: os modelos estimados são adequados? há algum preferível aos demais?
# Estimação do melhor modelo ARIMA
model = tsa.ARIMA(df, order=(2, 0, 2))
fit = model.fit()
print(fit.summary())

# Resíduos do modelo ajustado
residuos = fit.resid

# ACF dos resíduos
plot_acf(residuos, lags=36)
plt.show()