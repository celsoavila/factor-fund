# Stage 02 — Calendars, FX & Normalization (with Corporate Data Ingestion)

**Objective**  
Harmonize trading calendars, timezones, and currencies to a daily EOD standard **and** ingest the corporate/economic blocks coming from Excel extracts (sourced from Bloomberg and Economatica). This stage produces clean, chronologically ordered, numeric tables that downstream stages can merge by `date` and `ticker`.

> **Context:** The Excel files (`02 - a..g - input_data_corp.xlsx`) are curated exports from Bloomberg/Economatica containing both *corporate* (fundamentals) and *macro/economic* data. We ingest them in two passes: **corp_data_1** (wide block D:BK) and **corp_data_2** (selected metrics in BO:BT).

---

## Inputs

- Directory: `data/input_bbg/`  
  Files (seven workbooks with similar layout):  
  - `02 - a - input_data_corp.xlsx`  
  - `02 - b - input_data_corp.xlsx`  
  - `02 - c - input_data_corp.xlsx`  
  - `02 - d - input_data_corp.xlsx`  
  - `02 - e - input_data_corp.xlsx`  
  - `02 - f - input_data_corp.xlsx`  
  - `02 - g - input_data_corp.xlsx`  

- Each workbook contains multiple worksheets. We iterate **from `sheets[4:]`** (first four are headers/index pages).  
- **Ticker extraction**: from cell **E5** of each sheet (first 5 chars).  
- **Dates** are read from the first column of each block and parsed as UTC, then converted to naive `YYYY-MM-DD` strings.

**Upstream sources (for context only):** Bloomberg and Economatica. No provider credentials or raw dumps are committed to the repository.

---

## Process (high‑level)

We run two ingestion scripts (public description; code remains private):

### 1) `stage02_concat_corp1.py` — *corp_data_1* block (wide fundamentals/economic panel)
- **Excel block**: columns **D:BK**, header starts at line 7 (`skiprows=6` in pandas), engine `openpyxl`.
- Normalizes the first column name to `date` if it appears as `Dates`/`Date`.
- Coerces **all non-`date`/`ticker` columns** to numeric (`errors="coerce"`).
- Appends a `ticker` column (from E5) and concatenates all sheets from all files.
- Sorts by `date` (naive) and `ticker`.
- **Output**
  - CSV: `data/interim/02 - corp_data_1.csv`
  - XLSX (only if row count ≤ 1,048,576): `data/interim/02 - corp_data_1.xlsx`

### 2) `stage02_concat_corp2.py` — *corp_data_2* block (selected metrics)
- **Excel block**: columns **BO:BT**, read with `header=None`, `skiprows=7`.
- Explicitly renames the six columns to:
  - `date`  
  - `CUR_MKT_MKT_CAP`  
  - `MKT_CAP_TO_ASSETS`  
  - `PX_TO_FREE_CASH_FLOW`  
  - `PX_TO_BOOK_RATIO`  
  - `EARN_YLD`
- Inserts `ticker` (from E5) as the **second column**.
- Coerces the five metrics to numeric (`errors="coerce"`).
- Sorts by `date` (naive) and `ticker`.
- **Output**
  - CSV: `data/interim/02 - corp_data_2.csv`
  - XLSX (only if row count ≤ 1,048,576): `data/interim/02 - corp_data_2.xlsx`

**Shared conventions (both scripts):**
- `date` parsed as pandas datetime with `utc=True` → then `tz_localize(None)` → format `YYYY-MM-DD`.
- Missing files or sheets are logged with `[WARN]` messages but do not stop the entire run.
- Iteration uses `tqdm` progress bars when available.

---

## Outputs (Stage 02)

- **Private (intermediate)**: full outputs in `data/interim/`  
  - `02 - corp_data_1.csv` (+ optional `.xlsx`)  
  - `02 - corp_data_2.csv` (+ optional `.xlsx`)

- **Public (samples only)**: optionally publish tiny sanitized slices under `data/public_samples/` to illustrate the schema (no sensitive values, no provider payloads).

---

## Minimal validation

- **Schema checks**: presence/order of `date` and `ticker`; expected metric columns in corp2.  
- **Date integrity**: no `NaT` after coercion; final `YYYY-MM-DD` strings are monotonic per ticker.  
- **Numeric coercion**: non‑numeric entries become `NaN` (no exceptions).  
- **Duplicates**: per `(date, ticker)` pair are flagged and, if present, summarized in a log.  
- **Row counts**: ensure XLSX export only when ≤ 1,048,576 rows.

---

## Public vs. Private

- **Public**: this documentation, the column dictionaries, and small synthetic samples.  
- **Private**: the full Excel extracts, provider‑specific sheets/fields, and the complete CSV/XLSX outputs in `data/interim/`.

---

## Notes & caveats

- This stage **does not** compute features or returns; it only **standardizes** and **aligns** raw corporate/economic panels to a clean daily format. Feature engineering happens in later stages.  
- Bloomberg/Economatica brand names appear here **only** to document provenance; no API keys or raw exports are included in the repository.
