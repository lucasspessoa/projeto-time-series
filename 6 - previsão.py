import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import numpy as np
import matplotlib.pyplot as plt

# Arquivo com pré-Tratamento de dados
read_excel = pd.read_excel('dados_trabalho_ajustado.xlsx')

df = pd.DataFrame(read_excel)

# Tratamento de dados
# Transformar a coluna 'Matricula' em índice
df = df.set_index("Matricula")

# Coluna '515088'
df = df[[515088]]

# Questão6 - Previsão a partir do melhor modelo: ARIMA(0,0,2)
# Divisão treino-teste (IN SAMPLE-OUT SAMPLE)
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]

# Conforme explicado acima, MA(2) será usado pois foi considerado o melhor modelo
model = ARIMA(train, order=(0, 0, 2))
fit = model.fit()

# Previsão do modelo
predictions = fit.forecast(steps=len(test))

# Modelos para verificar qualidade da previsão
rmse = np.sqrt(mean_squared_error(test, predictions))
mae = mean_absolute_error(test, predictions)
mape = mean_absolute_percentage_error(test, predictions)
print()
print(f"Root Mean Squared Error: {rmse}")
print(f"Mean Absolute Error: {mae}")
print(f"Mean Absolute Percentage Error: {mape}")
print()

# Visualização gráfica de Previsão x Real
plt.plot(test, label="Valores Reais")
plt.plot(predictions, label="Previsões", color="red")
plt.title("Comparação de Previsões e Valores Reais")
plt.legend()
plt.show()