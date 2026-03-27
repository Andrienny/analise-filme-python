import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv("filmes.csv")

# mostrar primeiras linhas
print(df.head())

# média de nota
media = df["nota"].mean()
print("Média das notas:", media)

# filmes mais bem avaliados
top_filmes = df.sort_values(by="nota", ascending=False)
print(top_filmes.head())

# gráfico
df["nota"].hist()
plt.title("Distribuição das notas")
plt.xlabel("Nota")
plt.ylabel("Quantidade")
plt.show()
