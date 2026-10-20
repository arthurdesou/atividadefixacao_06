"""Histograma com curva de densidade: distribuição da idade dos clientes.

Entrada : dados/dados_distribuicao.csv
Saída   : graficos/04_distribuicao.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_distribuicao.csv")

media = df["idade"].mean()
mediana = df["idade"].median()

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(11, 6.5))

sns.histplot(df["idade"], bins=range(15, 75, 5), kde=True, color="#4263eb",
             edgecolor="white", ax=ax)

ax.axvline(media, color="#e03131", linestyle="--", linewidth=2,
           label=f"Média: {media:.1f} anos".replace(".", ","))
ax.axvline(mediana, color="#2f9e44", linestyle="-.", linewidth=2,
           label=f"Mediana: {mediana:.0f} anos")

ax.set_title("Distribuição da idade dos clientes", fontweight="bold", pad=15)
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de clientes")
ax.legend(frameon=False)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "04_distribuicao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
