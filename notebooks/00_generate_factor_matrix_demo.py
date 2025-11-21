import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

# parâmetros do exemplo
dates = pd.date_range("2024-01-01", periods=6, freq="M")  # 6 meses
tickers = ["AAA3", "BBB4", "CCC3", "DDD4", "EEE3"]        # 5 ativos

rows = []
for date in dates:
    for ticker in tickers:
        value_score = np.random.normal(0, 1)
        mom_126d    = np.random.normal(0, 1)
        quality     = np.random.normal(0, 1)
        size        = np.random.normal(0, 1)
        volatility  = np.random.normal(0, 1)

        # retorno futuro "fake"
        ret_fwd_21d = (
            0.03 * value_score
            + 0.05 * mom_126d
            + 0.02 * quality
            - 0.01 * volatility
            + np.random.normal(0, 0.02)
        )

        rows.append(
            {
                "date": date,
                "ticker": ticker,
                "value_score": value_score,
                "mom_126d": mom_126d,
                "quality": quality,
                "size": size,
                "volatility": volatility,
                "ret_fwd_21d": ret_fwd_21d,
            }
        )

df = pd.DataFrame(rows)

# garantir ordenação bonitinha
df.sort_values(["date", "ticker"], inplace=True)
df.reset_index(drop=True, inplace=True)

output_path = Path("data/examples/factor_matrix_demo.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)
print(f"Arquivo salvo em: {output_path}")
