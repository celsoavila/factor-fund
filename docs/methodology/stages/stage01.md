# Stage 01 — Ingestion & Source Catalog

**Objective**  
Define the data universe and ingest raw time series from major market data providers into a unified catalog. Establish a minimal schema and conventions that downstream stages can rely on.

---

## Inputs (high-level)
- Price series (equities, indices, benchmarks).  
- Reference series (e.g., CDI/SELIC).  
- Corporate/economic indicators (covered in Stage 02).  
- Sources include well-known providers (e.g., Bloomberg, Economatica).

All time series are treated as **daily end‑of‑day** and organized around:
- `date` (YYYY‑MM‑DD)
- `ticker` (for security‑level series)
- numeric fields (e.g., `px_last`, `px_open`, `px_high`, `px_low`, `volume`), when applicable

---

## Process (overview)
1. **Discovery & mapping** — create a **source catalog** that maps provider symbols to internal tickers and metadata (currency, adjustments, notes).  
2. **Landing** — store provider exports locally (outside the repository), preserving original files.  
3. **Integrity checks** — basic validation: missing dates vs. business calendar, duplicated rows, data types.  
4. **Documentation** — maintain a simple CSV catalog describing the universe to be processed in the next stages.

---

## Outputs
- **Private:** raw dumps under a secure local folder and a processed catalog (CSV) with the mapped universe.  
- **Public:** a small illustrative sample of the catalog (optional) under `data/public_samples/`.

---

## Minimal validation
- Coverage by series and by date range.  
- % of missing business days vs. the chosen trading calendar.  
- No duplicated (`date`, `ticker`) pairs in staged tables.  
- Consistent numeric types and date formats.

---

## Public vs. Private
- **Public:** methodology and a tiny sample catalog (no proprietary payloads).  
- **Private:** all provider exports, full catalog, and detailed mapping rules.
