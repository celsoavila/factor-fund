# Stage 05 — Base Features & Lag Alignment

**Objective**  
Compute base features (e.g., momentum, reversal, volatility, liquidity) and enforce **lags** to prevent look‑ahead bias. Produce a **feature matrix** aligned to the execution policy (e.g., features at D → trade at D+1).

---

## Inputs
- Cleaned panels and `quality_mask` from Stage 04.
- Business calendar and any reference series needed for certain features.

---

## Process (overview)
1. **Feature set (examples)**  
   - Cumulative returns (1m/3m/6m/12m), rolling volatility (21/63/252d), turnover, short‑term drawdown, etc.  
   - Normalize cross‑sectionally if needed (e.g., z‑scores).

2. **Lagging & alignment**  
   - Enforce T+1 execution: features computed with data up to day D are associated with signals for **D+1**.  
   - Drop or mask rows where lags cannot be satisfied.

3. **Mask application**  
   - Apply `quality_mask` to avoid polluted observations.

---

## Outputs
- **Private**: `private/data_processed/features/features_base.parquet` (feature matrix).  
- **Public**: dictionary of feature names/intuition (no hyperparameters), possibly a small synthetic example for docs.

---

## Validation
- **Leakage checks**: verify no feature uses data from the future.  
- Coverage by asset/time after lagging and mask application.  
- Basic stability diagnostics (e.g., rolling means/vol of key features).

---

## Public vs. Private
- **Public**: feature list and high‑level definitions.  
- **Private**: exact windows, hyperparameters, normalization details.
