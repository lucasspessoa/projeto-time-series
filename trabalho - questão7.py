import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.diagnostic import het_arch

# Arquivo com pré-Tratamento de dados em relação ao anterior
read_excel = pd.read_excel('dados_trabalho_ajustado.xlsx')

df = pd.DataFrame(read_excel)

# Tratamento de dados
# Transformar a coluna 'Matricula' em índice
df = df.set_index("Matricula")

# Coluna '515088'
df = df[[515088]]

# Questão7 - ainda em melhor modelo ARIMA(0,0,2)
# Estimação do correlograma dos resíduos ao quadrado para verificação de efeitos ARCH. Em conjunto, Teste de White para verificar a Heterocedasticidade na série
model = ARIMA(df, order=(0, 0, 2))
fit = model.fit()
residuals = fit.resid
# Resíduos ao quadrado
residuals_squared = residuals ** 2

# Correlograma dos resíduos ao quadrado
plot_acf(residuals_squared, lags=36, title="Correlograma dos Resíduos ao Quadrado")
plt.show()

# Teste de Engle para efeitos ARCH
test_arch = het_arch(residuals)
print("Teste ARCH")
print(f"Estatística LM: {test_arch[0]}")
print(f"p-valor: {test_arch[1]}")
print(f"Estatística F: {test_arch[2]}")
print(f"p-valor F: {test_arch[3]}")