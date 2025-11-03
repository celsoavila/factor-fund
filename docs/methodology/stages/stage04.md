# Stage 04 — Outliers, Stale Prints & Quality Masks

**Objective**  
Detect and mitigate outliers and stale prints, and produce a **quality mask** per (`date`, `ticker`) to flag observations that should be excluded or down‑weighted in later stages.

---

## Inputs (from Stage 03)
- Cleaned corporate/economic panels (daily), indexed by `date` and `ticker`.
- Optionally, reference price/volume series for stale‑print checks.

---

## Process (overview)
1. **Outlier detection**  
   - Identify extreme values using robust statistics (e.g., percentiles or MAD‑based rules).  
   - Apply **winsorization/clipping** where allowed to stabilize tail behavior.

2. **Stale prints / flatlines**  
   - Flag sequences with unchanged values when variation would be expected (e.g., price with volume).

3. **Quality mask**  
   - Build a boolean mask `quality_mask[date, ticker]` (True=usable) and optional confidence scores.  
   - This mask is consumed downstream to filter features and training rows.

4. **Documentation**  
   - Summary diagnostics (percent clipped per column, per ticker).  
   - Illustrative heatmap of usable coverage.

---

## Outputs
- **Private**: `private/data_processed/clean/returns_clean.parquet` (or equivalent) and `private/data_processed/clean/quality_mask.parquet`.  
- **Public**: high‑level description, plus optional figures (e.g., coverage heatmap) under `reports/figures/`.

---

## Validation
- % of points flagged/clipped by column and by ticker.  
- Impact on aggregate stats (mean/volatility).  
- No leakage: thresholds derived **only** from in‑window data where applicable.

---

## Public vs. Private
- **Public**: methodology, rationale, and figures.  
- **Private**: exact thresholds, parameters, and full masks/clean tables.
