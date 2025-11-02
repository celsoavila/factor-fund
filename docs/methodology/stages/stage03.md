# Stage 03 — Corporate Actions & Price Adjustments

**Objective**  
Apply dividends/JSCP, splits/reverse splits, and spinoffs to produce **consistent daily returns** and adjusted prices when required.

## Inputs
- `prices_normalized.parquet` (Stage 02)
- Corporate action tables per asset (Bloomberg/Economatica/B3)

## Process (high-level)
- Build cumulative adjustment factors per asset/date.
- Compute **adjusted price** (when needed) and **daily returns** robust to events.
- Track quality flags: `corporate_action_gap`, applied `ex_date`, etc.

## Outputs
- **Private** daily returns: `private/data_processed/adjusted/returns_daily.parquet`.
- **Public** small window sample: `reports/tables/returns_sample.csv`.

## Minimal validation
- Check `ex_date` alignment for dividends/splits vs. sources
- Highlight outliers (e.g., returns > X standard deviations)

## Public vs. Private
- **Public**: methodology + before/after visual examples (no full datasets).
- **Private**: full event tables and adjusted series.
