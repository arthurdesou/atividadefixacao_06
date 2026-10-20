"""Regressão linear simples: gasto mensal em função da renda mensal.

Entrada : dados/dados_regressao.csv
Saída   : graficos/09_regressao.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from scipy import stats

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_regressao.csv")

# Ajuste por mínimos quadrados
res = stats.linregress(df["renda_mensal"], df["gasto_mensal"])
r2 = res.rvalue ** 2
sinal = "+" if res.intercept >= 0 else "−"
equacao = (f"y = {res.slope:.3f}x {sinal} {abs(res.intercept):.0f}\n"
           f"R² = {r2:.3f}").replace(".", ",")

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(11, 7))

sns.regplot(data=df, x="renda_mensal", y="gasto_mensal", ci=95,
            scatter_kws={"s": 60, "alpha": 0.65, "color": "#4263eb"},
            line_kws={"color": "#e03131", "linewidth": 2.5}, ax=ax)

brl = FuncFormatter(lambda v, _: f"R$ {v:,.0f}".replace(",", "."))
ax.xaxis.set_major_formatter(brl)
ax.yaxis.set_major_formatter(brl)

ax.text(0.04, 0.95, equacao, transform=ax.transAxes, va="top", fontsize=14,
        bbox={"boxstyle": "round", "facecolor": "white", "edgecolor": "gray"})

ax.set_title("Regressão linear: gasto mensal × renda mensal",
             fontweight="bold", pad=15)
ax.set_xlabel("Renda mensal")
ax.set_ylabel("Gasto mensal")
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "09_regressao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
