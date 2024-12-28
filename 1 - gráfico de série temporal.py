import pandas as pd
import matplotlib.pyplot as plt

# Arquivo com pré-Tratamento de dados
read_excel = pd.read_excel('dados_trabalho_ajustado.xlsx')

df = pd.DataFrame(read_excel)

# Tratamento de dados
# Transformar a coluna 'Matricula' em índice
df = df.set_index("Matricula")

# Coluna '515088'
df = df[[515088]]

# Questão1 - Gráfico de Série Temporal: visualizando tendência, sazonalidade, ciclos ou outliers
# Criando o gráfico
plt.figure(figsize=(10, 5))  # Definindo o tamanho do gráfico
plt.plot(df, label="Série Temporal", color="blue", linewidth=2)

# Configurações adicionais
plt.title("Série Temporal - SER20", fontsize=16)
plt.xlabel("Observação", fontsize=12)
plt.ylabel("SER20", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Exibindo o gráfico
plt.show()