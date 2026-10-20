"""Gráfico de dispersão: altura x peso, colorido por sexo.

Entrada : dados/dados_dispersao.csv
Saída   : graficos/03_dispersao.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_dispersao.csv")

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(11, 7))

sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo", style="sexo",
                palette={"Feminino": "#d6336c", "Masculino": "#1c7ed6"},
                s=90, alpha=0.75, edgecolor="white", linewidth=0.6, ax=ax)

ax.set_title("Relação entre altura e peso", fontweight="bold", pad=15)
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo", frameon=False)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "03_dispersao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
