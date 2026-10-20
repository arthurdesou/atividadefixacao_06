"""Mapa de calor: movimento de clientes por dia da semana e horário.

Entrada : dados/dados_heatmap.csv
Saída   : graficos/06_heatmap.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_heatmap.csv")

ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

matriz = (df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
            .reindex(ordem_dias))          # garante a ordem cronológica dos dias

sns.set_theme(style="white", context="talk")
fig, ax = plt.subplots(figsize=(12, 7))

sns.heatmap(matriz, annot=True, fmt="d", cmap="YlOrRd", linewidths=0.8,
            linecolor="white", cbar_kws={"label": "Clientes"}, ax=ax)

ax.set_title("Movimento de clientes por dia da semana e horário",
             fontweight="bold", pad=15)
ax.set_xlabel("Horário")
ax.set_ylabel("")
ax.tick_params(axis="y", rotation=0)

fig.tight_layout()
saida = RAIZ / "graficos" / "06_heatmap.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
