# Methodology — Overview

This section summarizes the preparation pipeline and links to detailed pages.

## Stages 01–03 (Data Preparation)

### [Stage 01 — Ingestion & Source Catalog](./stages/stage01.md)
Defines the data universe and ingests raw time series (prices, benchmarks, references) from major providers into a simple catalog. Establishes minimal schema and conventions (daily EOD, `date`, `ticker`, numeric fields).

**Outputs (public/private):**
- Public: small illustrative sample of the catalog (optional).
- Private: raw exports and the full catalog of mapped series.

---

### [Stage 02 — Corporate and Economic Data Integration](./stages/stage02.md)
Integrates corporate fundamentals and macroeconomic indicators from well-known providers (e.g., Bloomberg, Economatica). Harmonizes dates, numeric types, and aligns panels for later merges.

**Outputs (public/private):**
- Public: methodology notes; optional synthetic samples.
- Private: provider exports and full intermediate tables under `data/interim/`.

---

### [Stage 03 — Cleaning & Gap Handling for Corporate/Economic Panels](./stages/stage03.md)
Cleans the Stage 02 panels and resolves gaps per ticker using a time‑aware rule (future‑first average, fallback to past) within limited windows. Final tables are chronologically ordered (`YYYY‑MM‑DD`) and numeric‑only.

**Outputs (public/private):**
- Public: description of the filling rationale and final format.
- Private: exact windows/thresholds and full cleaned CSV/XLSX tables.

---

## What comes next
- **Stage 04** — Outlier handling, stale print detection, quality masks.
- **Stage 05** — Base features (momentum, volatility, liquidity, etc.) with lags.
- **Stage 06** — Train/Validation/Test split (currently: 2002–2017 vs. 2018–Aug 2025), with walk‑forward as a future extension.
- **Stages 07–11** — Consolidation, strategies, fees, charts, and risk/metrics for the public showcase.

> Sensitive code, parameters, and raw datasets remain outside the repository under `private/` (ignored by git) or non‑versioned local folders.
