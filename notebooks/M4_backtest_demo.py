import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# ------------------ paths ------------------ #
DATA_DIR = Path("data/examples")
MODELS_DIR = Path("models")

FACTOR_PATH = DATA_DIR / "factor_matrix_demo.csv"
PORTFOLIO_PATH = DATA_DIR / "portfolio_weights_demo.csv"
BACKTEST_PATH = DATA_DIR / "backtest_results_demo.csv"
FIG_PATH = MODELS_DIR / "backtest_demo_equity_curves.png"

MODELS_DIR.mkdir(exist_ok=True)

print(f"Lendo factor matrix de: {FACTOR_PATH}")
df_factors = pd.read_csv(FACTOR_PATH, parse_dates=["date"])

print(f"Lendo pesos da carteira de: {PORTFOLIO_PATH}")
df_port = pd.read_csv(PORTFOLIO_PATH, parse_dates=["date"])

# ------------------ preparar dados ------------------ #
# Vamos garantir consistência de nomes/ordem
cols_needed = ["date", "ticker", "ret_fwd_21d"]
df_factors = df_factors[cols_needed].copy()

# Merge: carteira + retornos futuros
df_merged = pd.merge(
    df_port,
    df_factors,
    on=["date", "ticker"],
    how="inner",
    validate="many_to_one",
)

# Ordenar por data só por organização
df_merged = df_merged.sort_values(["date", "ticker"]).reset_index(drop=True)

# ------------------ calcular retornos por data ------------------ #
def compute_returns(group: pd.DataFrame) -> pd.Series:
    """
    Retorno da carteira (modelo) e benchmark equal-weight para uma data.
    """
    g = group.copy()

    # Retorno da carteira do modelo
    port_ret = (g["weight"] * g["ret_fwd_21d"]).sum()

    # Benchmark equal-weight (mesmo universo)
    eqw_ret = g["ret_fwd_21d"].mean()

    return pd.Series(
        {
            "port_ret": port_ret,
            "eqw_ret": eqw_ret,
        }
    )

df_ret = df_merged.groupby("date").apply(compute_returns).reset_index()

# ------------------ equity curves ------------------ #
df_ret["port_equity"] = (1 + df_ret["port_ret"]).cumprod()
df_ret["eqw_equity"] = (1 + df_ret["eqw_ret"]).cumprod()

# ------------------ métricas simples ------------------ #
n_periods = len(df_ret)
if n_periods > 1:
    # assumindo dados mensais (como na demo)
    periods_per_year = 12

    port_cum = df_ret["port_equity"].iloc[-1] - 1
    eqw_cum = df_ret["eqw_equity"].iloc[-1] - 1

    port_ann_ret = (1 + port_cum) ** (periods_per_year / n_periods) - 1
    eqw_ann_ret = (1 + eqw_cum) ** (periods_per_year / n_periods) - 1

    port_ann_vol = df_ret["port_ret"].std(ddof=1) * np.sqrt(periods_per_year)
    eqw_ann_vol = df_ret["eqw_ret"].std(ddof=1) * np.sqrt(periods_per_year)

    port_sharpe = port_ann_ret / port_ann_vol if port_ann_vol > 0 else np.nan
    eqw_sharpe = eqw_ann_ret / eqw_ann_vol if eqw_ann_vol > 0 else np.nan

    # drawdown
    port_peak = df_ret["port_equity"].cummax()
    port_dd = df_ret["port_equity"] / port_peak - 1
    port_max_dd = port_dd.min()

    eqw_peak = df_ret["eqw_equity"].cummax()
    eqw_dd = df_ret["eqw_equity"] / eqw_peak - 1
    eqw_max_dd = eqw_dd.min()

    print("\n=== Métricas da carteira (modelo) ===")
    print(f"Retorno acumulado: {port_cum:.2%}")
    print(f"Retorno anualizado: {port_ann_ret:.2%}")
    print(f"Vol anualizada: {port_ann_vol:.2%}")
    print(f"Sharpe (simples): {port_sharpe:.2f}")
    print(f"Max drawdown: {port_max_dd:.2%}")

    print("\n=== Métricas do benchmark equal-weight ===")
    print(f"Retorno acumulado: {eqw_cum:.2%}")
    print(f"Retorno anualizado: {eqw_ann_ret:.2%}")
    print(f"Vol anualizada: {eqw_ann_vol:.2%}")
    print(f"Sharpe (simples): {eqw_sharpe:.2f}")
    print(f"Max drawdown: {eqw_max_dd:.2%}")
else:
    print("Backtest com menos de 2 períodos — métricas anuais não são calculadas.")

# ------------------ salvar resultados ------------------ #
BACKTEST_PATH.parent.mkdir(parents=True, exist_ok=True)
df_ret.to_csv(BACKTEST_PATH, index=False)
print(f"\nResultados do backtest salvos em: {BACKTEST_PATH}")

# ------------------ gráfico de equity curves ------------------ #
plt.figure(figsize=(7, 4))
plt.plot(df_ret["date"], df_ret["port_equity"], label="Model portfolio")
plt.plot(df_ret["date"], df_ret["eqw_equity"], label="Equal-weight benchmark", linestyle="--")
plt.xlabel("Date")
plt.ylabel("Equity (normalized)")
plt.title("Synthetic Backtest – Model vs Equal-weight")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(FIG_PATH)
plt.close()

print(f"Gráfico de equity curves salvo em: {FIG_PATH}")
