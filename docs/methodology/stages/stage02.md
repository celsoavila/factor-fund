# Stage 02 — Corporate and Economic Data Integration

**Objective**  
Integrate and harmonize corporate fundamentals and macroeconomic indicators obtained from major financial data providers (e.g., Bloomberg, Economatica). The goal is to standardize these datasets into a unified daily format suitable for modeling and feature engineering in later stages.

---

## Inputs (high-level)

- Corporate indicators such as *market capitalization*, *book-to-price ratio*, *cash-flow yield*, and *earnings yield*.
- Economic indicators such as *inflation rate*, *interest rates*, and *unemployment levels*.
- Sources include well-known providers of financial and economic data (Bloomberg, Economatica).

All datasets are treated as time series indexed by `date` and `ticker` (for firm-level indicators) or by `date` only (for macro indicators).

---

## Process (overview)

1. **Extraction and ingestion**  
   - Data are exported periodically from provider terminals or APIs into standardized Excel/CSV files.  
   - Each file may contain multiple entities (companies or indices).  
   - The process consolidates all tabs and merges them into a single chronological dataset.

2. **Standardization**  
   - Dates converted to `YYYY-MM-DD` and aligned to a common business calendar.  
   - Numeric fields coerced to floats, text normalized.  
   - Missing values logged but tolerated (no forward-filling at this stage).

3. **Outputs**  
   - Intermediate CSV files under a secure data folder (`data/interim/`).  
   - Optionally, small public-safe samples may be generated for documentation under `data/public_samples/`.

---

## Validation

- Time alignment across corporate and macro series.  
- Verification that no duplicated (`date`, `ticker`) combinations remain.  
- Consistent numeric types and date formats.  
- No dependency on provider-specific file structures in the downstream pipeline.

---

## Public vs. Private

- **Public:** this description, methodology notes, and illustrative (synthetic) samples.  
- **Private:** raw provider exports, detailed file formats, and the complete ingestion scripts.

---

## Notes

This stage focuses only on cleaning and aligning the data sources.  
Computation of derived metrics and model features occurs in later stages.
