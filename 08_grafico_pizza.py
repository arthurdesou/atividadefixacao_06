"""Gráfico de pizza: participação de cada canal no faturamento.

Entrada : dados/dados_pizza.csv
Saída   : graficos/08_pizza.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_pizza.csv")
df = df.sort_values("faturamento", ascending=False)

total = df["faturamento"].sum()
cores = sns.color_palette("Set2", len(df))

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(
    df["faturamento"], colors=cores, startangle=90, counterclock=False,
    autopct=lambda p: f"{p:.1f}%".replace(".", ","),
    pctdistance=0.72, textprops={"fontsize": 14, "fontweight": "bold"},
    wedgeprops={"edgecolor": "white", "linewidth": 2})

# Legenda com os valores absolutos em reais
legendas = [f"{c} — R$ {v:,.0f}".replace(",", ".")
            for c, v in zip(df["canal_venda"], df["faturamento"])]
ax.legend(legendas, title="Canal de venda", loc="center left",
          bbox_to_anchor=(1, 0.5), frameon=False, fontsize=12, title_fontsize=13)

ax.set_title(f"Faturamento por canal de venda\nTotal: R$ {total:,.0f}".replace(",", "."),
             fontweight="bold", fontsize=16)

fig.tight_layout()
saida = RAIZ / "graficos" / "08_pizza.png"
fig.savefig(saida, dpi=150, bbox_inches="tight")
print(f"Gráfico salvo em: {saida}")
