import pandas as pd
import matplotlib.pyplot as plt

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

# Questão1 - Gráfico de Série Temporal: visualizando tendência, sazonalidade, ciclos ou outliers
# Criando o gráfico
plt.figure(figsize=(10, 5))  # Definindo o tamanho do gráfico
plt.plot(df[[515088]], label="Série Temporal", color="blue", linewidth=2)

# Configurações adicionais
plt.title("Série Temporal - SER20", fontsize=16)
plt.xlabel("Observação", fontsize=12)
plt.ylabel("SER20", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Exibindo o gráfico
plt.show()