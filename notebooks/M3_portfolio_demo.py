import pandas as pd
import numpy as np
from pathlib import Path
import joblib

# Caminhos
DATA_PATH = Path("data/examples/factor_matrix_demo.csv")
MODELS_DIR = Path("models")
OUTPUT_PATH = Path("data/examples/portfolio_weights_demo.csv")

MODEL_PATH = MODELS_DIR / "ridge_demo.pkl"
SCALER_PATH = MODELS_DIR / "scaler_demo.pkl"

feature_cols = ["value_score", "mom_126d", "quality", "size", "volatility"]
target_col = "ret_fwd_21d"

print(f"Lendo dados de: {DATA_PATH}")
df = pd.read_csv(DATA_PATH, parse_dates=["date"])

print(f"Lendo modelo de: {MODEL_PATH}")
model = joblib.load(MODEL_PATH)

print(f"Lendo scaler de: {SCALER_PATH}")
scaler = joblib.load(SCALER_PATH)

# Ordena por data/ticker
df_sorted = df.sort_values(["date", "ticker"]).reset_index(drop=True)

# Calcula model_score
X = df_sorted[feature_cols].values
X_scaled = scaler.transform(X)
df_sorted["model_score"] = model.predict(X_scaled)

# Parâmetros da carteira
top_n = 2   # número de ativos na carteira por data

def build_portfolio_for_date(group: pd.DataFrame) -> pd.DataFrame:
    g = group.copy()
    g = g.sort_values("model_score", ascending=False)
    g["rank"] = np.arange(1, len(g) + 1)

    # seleciona top_n
    g["weight"] = 0.0
    mask_top = g["rank"] <= top_n
    if mask_top.any():
        g.loc[mask_top, "weight"] = 1.0 / mask_top.sum()

    return g

# Aplica por data
df_port = (
    df_sorted
    .groupby("date", group_keys=False)
    .apply(build_portfolio_for_date)
    .reset_index(drop=True)
)

# Mantém colunas relevantes
cols_out = ["date", "ticker", "model_score", "weight"]
df_port_out = df_port[cols_out].copy()

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df_port_out.to_csv(OUTPUT_PATH, index=False)

print(f"\nPortfólio de exemplo salvo em: {OUTPUT_PATH}")
print(df_port_out.head(10))
