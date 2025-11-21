import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_squared_error

import joblib
import matplotlib.pyplot as plt

# Caminhos
DATA_PATH = Path("data/examples/factor_matrix_demo.csv")
MODELS_DIR = Path("models")
MODELS_DIR.mkdir(exist_ok=True)

print(f"Lendo dados de: {DATA_PATH}")
df = pd.read_csv(DATA_PATH, parse_dates=["date"])

feature_cols = ["value_score", "mom_126d", "quality", "size", "volatility"]
target_col = "ret_fwd_21d"

# Ordena por data só por segurança
df_sorted = df.sort_values("date").reset_index(drop=True)

X = df_sorted[feature_cols].values
y = df_sorted[target_col].values

# Split simples: 70% primeiras linhas treino, 30% teste
n = len(df_sorted)
split_idx = int(n * 0.7)

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(f"Tamanho treino: {len(X_train)} | teste: {len(X_test)}")

# Padronização
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelo Ridge
model = Ridge(alpha=1.0, random_state=42)
model.fit(X_train_scaled, y_train)

y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)

print(f"R² train: {r2_train:.3f} | R² test: {r2_test:.3f}")
print(f"MSE train: {mse_train:.6f} | MSE test: {mse_test:.6f}")

# Coeficientes (interpretabilidade rápida)
coef_series = pd.Series(model.coef_, index=feature_cols).sort_values()
print("\nCoeficientes do modelo (Ridge):")
print(coef_series)

# Salvar modelo e scaler
model_path = MODELS_DIR / "ridge_demo.pkl"
scaler_path = MODELS_DIR / "scaler_demo.pkl"

joblib.dump(model, model_path)
joblib.dump(scaler, scaler_path)

print(f"\nModelo salvo em: {model_path}")
print(f"Scaler salvo em: {scaler_path}")

# Gráfico simples y_real vs y_pred (teste)
fig_path = MODELS_DIR / "ridge_demo_y_true_vs_pred.png"
plt.figure(figsize=(5, 5))
plt.scatter(y_test, y_test_pred, alpha=0.7)
plt.axline((0, 0), slope=1, linestyle="--")
plt.xlabel("ret_fwd_21d real")
plt.ylabel("ret_fwd_21d previsto")
plt.title("Ridge – conjunto de teste")
plt.grid(True)
plt.tight_layout()
plt.savefig(fig_path)
plt.close()

print(f"Gráfico salvo em: {fig_path}")

