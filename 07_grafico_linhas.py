"""Gráfico de linhas: evolução diária das vendas por loja.

Entrada : dados/dados_linhas.csv
Saída   : graficos/07_linhas.png
"""
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_linhas.csv", parse_dates=["data"])
df = df.sort_values("data")

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(13, 6.5))

sns.lineplot(data=df, x="data", y="vendas", hue="loja", style="loja",
             markers=True, dashes=False, linewidth=2, markersize=7,
             palette={"Loja A": "#1c7ed6", "Loja B": "#f08c00"}, ax=ax)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b/%Y"))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO))

ax.set_title("Evolução das vendas por loja (1º trimestre de 2026)",
             fontweight="bold", pad=15)
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.legend(title="Loja", frameon=False)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "07_linhas.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
