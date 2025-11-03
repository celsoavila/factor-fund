# Stage 06 — Train / Validation / Test Split

**Objective**  
Separate the model‑building period from the final out‑of‑sample evaluation to avoid look‑ahead bias.

---

## Current setup (single hold‑out scheme)

| Segment | Period | Purpose |
|---------|--------|---------|
| **Training + Validation** | **2002 → 2017** | Fit the model and tune hyperparameters (internal folds remain inside this window). |
| **Testing (Out‑of‑Sample)** | **2018 → Aug 2025** | Unseen data used only for final evaluation/reporting. |

**Rules**
- Fit scalers/transformations using **2002–2017** only; apply unchanged to **2018–2025**.  
- Keep chronological order in merges and joins.  
- Targets respect execution lag (e.g., T+1).

---

## Future extension — walk‑forward (optional)
Define multiple rolling tests with periodic retraining, e.g.:
```
Train 1: 2002–2017 → Test 1: 2018–2020
Train 2: 2002–2020 → Test 2: 2021–2023
Train 3: 2002–2023 → Test 3: 2024–2025
```

---

## Outputs
- **Private**: `private/data_processed/splits/index_train_valid_test.json` (exact indices/seeds).  
- **Public**: description and optional diagram under `reports/figures/`.

---

## Validation
- No leakage from 2018+ into fitting.  
- Transformations fitted on Train only.  
- Adequate coverage in each window.
