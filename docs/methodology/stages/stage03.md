# Stage 03 — Cleaning & Gap Handling for Corporate/Economic Panels

**Objective**  
Standardize and clean the corporate/economic panels produced in Stage 02, resolving missing values per ticker with a conservative, time-aware rule. The output is a chronologically ordered, numeric dataset ready for downstream feature engineering.

---

## Inputs (from Stage 02)

- Corporate/economic panels (daily), indexed by `date` and `ticker`.
- All fields are treated as numeric indicators (except `date`/`ticker`).

---

## Process (overview)

1. **Type coercion & ordering**  
   - Convert all indicator columns to numeric (invalid values become `NaN`).  
   - Sort by `ticker` and `date` to ensure stable per-ticker operations.

2. **Time-aware gap handling (per ticker)**  
   - For each missing entry at day *D*, first **look ahead** (future) within a limited window and take the average of the first available values.  
   - If not enough future values exist, **fallback** to past observations within a limited window.  
   - If neither side yields enough data, the value may remain missing (rare by design).

3. **Final ordering & date normalization**  
   - Convert dates to `YYYY-MM-DD` (naive, EOD).  
   - Re-sort by (`date`, `ticker`) for downstream merges.

---

## Outputs

- Cleaned daily panels saved to an intermediate area (e.g., `data/interim/03 - corp_data_*.csv`).  
- Excel export is optional and used only for reasonably sized tables.

---

## Validation

- No structural changes: `date`/`ticker` preserved; indicators remain numeric.  
- Monotonic dates per ticker after normalization.  
- Diagnostics: number of filled vs. missing entries per column/ticker (kept in logs).

---

## Public vs. Private

- **Public**: methodology summary and rationale for the time-aware filling rule.  
- **Private**: exact window sizes, thresholds, and script parameters for each panel.

---

## Notes

This stage **does not** create model features; it only ensures that the base corporate/economic panels are consistent, numeric, and aligned. Feature computation happens later.
