"""Gráfico de barras agrupadas: vendas médias por categoria e região.

Entrada : dados/dados_barras.csv
Saída   : graficos/01_barras.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_barras.csv")

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(12, 6.5))

sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao",
            palette="viridis", ax=ax)

for container in ax.containers:
    ax.bar_label(container, fmt="%.0f", padding=3, fontsize=10)

ax.set_title("Vendas médias por categoria e região", fontweight="bold", pad=15)
ax.set_xlabel("Categoria de produto")
ax.set_ylabel("Vendas médias")
ax.legend(title="Região", frameon=False, loc="upper left", bbox_to_anchor=(1.01, 1))
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "01_barras.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
