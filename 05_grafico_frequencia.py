"""Gráfico de frequência: quantidade de chamados por tipo de atendimento.

Entrada : dados/dados_frequencia.csv
Saída   : graficos/05_frequencia.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_frequencia.csv")

freq = df["tipo_atendimento"].value_counts()   # já ordenado do maior p/ o menor
total = freq.sum()

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(11, 6))

barras = ax.barh(freq.index, freq.values, color=sns.color_palette("mako_r", len(freq)))
ax.invert_yaxis()                              # maior frequência no topo

# Rótulos: contagem absoluta e percentual
rotulos = [f"{n}  ({n / total * 100:.1f}%)".replace(".", ",") for n in freq.values]
ax.bar_label(barras, labels=rotulos, padding=6, fontsize=12)
ax.set_xlim(0, freq.max() * 1.22)

ax.set_title("Frequência de chamados por tipo de atendimento",
             fontweight="bold", pad=15)
ax.set_xlabel(f"Número de chamados (total: {total})")
ax.set_ylabel("")
sns.despine(left=True)

fig.tight_layout()
saida = RAIZ / "graficos" / "05_frequencia.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
