# Stage 06 — Train/Validation/Test Splits & Cross-Validation

**Objective**  
Define temporal partitions and a **walk-forward** (or expanding windows) evaluation scheme, with clear **out-of-sample** policy and backtest hygiene.

## Inputs
- `features_base.parquet` (Stage 05)
- Partition definitions (private)

## Process (high-level)
- Create a **partition schema**: Train/Valid/Test (e.g., 2009–2016 / 2017–2019 / 2020–2025) or rolling walk-forward with periodic retraining.
- Balance asset/time coverage while preserving **temporal order**.
- Save reproducible partition indices and seeds (private).

## Outputs
- **Private** split indices: `private/data_processed/splits/index_train_valid_test.json`.
- **Public** walk-forward diagram and a summary table with cut dates.

## Minimal validation
- No unintended overlap between train and test.
- Minimum coverage per window.

## Public vs. Private
- **Public**: method diagram and (optional) rounded cut dates.
- **Private**: exact indices/seeds and internal split files.
