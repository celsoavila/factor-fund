# Stage 05 — Base Features & Lag Alignment

**Objective**  
Compute base features (momentum, reversal, volatility, liquidity, etc.), enforce **lags** to prevent look-ahead bias, and assemble the **feature matrix**.

## Inputs
- `returns_clean.parquet`, `quality_mask.parquet` (Stage 04)
- Feature catalog (private: list + hyperparameters)

## Process (high-level)
- Compute classical features: cumulative returns (1m/3m/6m/12m), vol 21/63/252d, turnover, short drawdown, etc.
- Enforce execution lag (e.g., predict at D using info up to D; execute at D+1).
- Optional z-scores by asset/time and null handling via `quality_mask`.

## Outputs
- **Private** features parquet: `private/data_processed/features/features_base.parquet`.
- **Public** dictionary of features (names + intuition) under `docs/methodology/`.

## Minimal validation
- Leakage checks: no feature should use future information.
- Coverage after lag application (assets × time).

## Public vs. Private
- **Public**: feature names and intuition.
- **Private**: exact windows, hyperparameters, normalizations.
