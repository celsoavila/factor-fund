# Stage 02 — Calendars, FX & Normalization

**Objective**  
Harmonize trading calendars, timezones, and currencies; standardize to daily end-of-day in a chosen **base currency** and **master calendar**.

## Inputs
- `universe.csv` (from Stage 01)
- Raw series with their original timezone and currency
- ANBIMA/B3 holiday calendars

## Process (high-level)
- Choose **base currency** (e.g., BRL) and **master calendar** (e.g., B3 + ANBIMA).
- Controlled forward-fill only for reference series where allowed (e.g., benchmarks).
- FX conversion with consistent EOD rates; align indices/timezones to UTC EOD.

## Outputs
- **Private** normalized parquet: `private/data_processed/normalized/prices_normalized.parquet`.
- **Public** sample: `data/public_samples/prices_normalized_sample.parquet`.

## Minimal validation
- Timezone differences removed; aligned date index
- FX conversion audit trail (source + method)

## Public vs. Private
- **Public**: process description + small illustrative samples.
- **Private**: complete normalized series.
