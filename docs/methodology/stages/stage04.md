# Stage 04 — Advanced Cleaning, Outliers & Gaps

**Objective**  
Handle residual outliers, stale prints, and gaps. Standardize winsorization/clipping policy and build a **quality mask** per asset/date.

## Inputs
- `returns_daily.parquet` (Stage 03)
- Heuristics/thresholds for detection (private)

## Process (high-level)
- Detect spikes and stale prices.
- Apply winsorization (e.g., 0.5%–99.5%) where allowed.
- Build `quality_mask` (boolean per asset/date) and confidence scores.

## Outputs
- **Private** clean returns: `private/data_processed/clean/returns_clean.parquet`.
- **Private** masks: `private/data_processed/clean/quality_mask.parquet`.
- **Public**: description and illustrative heatmap in `reports/figures/`.

## Minimal validation
- % of clipped points per asset
- Impact on aggregate metrics (volatility/mean return)

## Public vs. Private
- **Public**: general rules and charts; no exact thresholds.
- **Private**: exact thresholds and full masks.
