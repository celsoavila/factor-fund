# Stage 01 — Ingestion & Source Catalog

**Objective**  
Inventory and ingest all data sources (Bloomberg/Economatica/internal CSVs), define the **minimum price schema**, and produce a **universe catalog** of series/tickers with basic metadata.

## Inputs (examples)
- Daily prices for assets (adjusted or raw as available)
- Benchmarks (CDI, Ibovespa, IFIX, SMLL, etc.)
- Mapping table for tickers/symbols (Bloomberg ↔ B3 ↔ internal alias)

## Process (high-level)
- Define a minimal price schema: `date, ticker, px_last, px_open, px_high, px_low, volume`.
- Build a **series catalog**: `universe.csv` with `ticker, provider, currency, adjustments_flag, notes`.
- Integrity checks: duplicated dates, holes (trading calendar vs. ANBIMA/B3), data types.

## Outputs
- **Private** landing zones by provider under `private/data_raw/`.
- **Private** processed catalog under `private/data_processed/catalog/universe.csv`.
- **Public** sample catalog under `data/public_samples/universe_sample.csv` (no sensitive values).

## Minimal validation
- Temporal coverage by series
- % of missing business days vs. chosen calendar

## Public vs. Private
- **Public**: generic catalog structure and tiny samples.
- **Private**: full raw dumps and provider-specific payloads.
