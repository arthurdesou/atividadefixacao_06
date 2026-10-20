"""Boxplot: distribuição salarial por departamento.

Entrada : dados/dados_boxplot.csv
Saída   : graficos/02_boxplot.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_boxplot.csv")

# Ordena os departamentos pela mediana salarial (facilita a comparação)
ordem = df.groupby("departamento")["salario"].median().sort_values(ascending=False).index

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(11, 6.5))

sns.boxplot(data=df, x="departamento", y="salario", order=ordem, hue="departamento",
            palette="Set2", width=0.55, showmeans=True, legend=False,
            meanprops={"marker": "D", "markerfacecolor": "white",
                       "markeredgecolor": "black", "markersize": 8}, ax=ax)

# Formata o eixo Y em reais, no padrão brasileiro (R$ 7.500)
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda v, _: f"R$ {v:,.0f}".replace(",", ".")))

ax.set_title("Distribuição salarial por departamento", fontweight="bold", pad=15)
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário mensal")
ax.text(0.99, 0.02, "◆ = média   |   linha central = mediana",
        transform=ax.transAxes, ha="right", fontsize=10, color="gray")
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "02_boxplot.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
