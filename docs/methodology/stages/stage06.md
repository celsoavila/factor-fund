# Stage 06 — Train / Validation / Test Split

**Objective**  
Define the temporal separation between the model-building period and the final out-of-sample evaluation, ensuring no look-ahead bias.

---

## Current setup (single hold-out scheme)

| Segment | Period | Purpose |
|---------|-------|---------|
| **Training + Validation** | **2002 → 2017** | Fit the model and tune hyperparameters. Internal validation folds (if any) remain inside this window. |
| **Testing (Out-of-Sample)** | **2018 → Aug 2025** | Fully unseen data, used only for final evaluation and reporting. |

- The split guarantees that all information used for model training precedes the evaluation period.  
- Feature scaling, transformations, or lagging are **fit only on 2002–2017** and then applied unchanged to the 2018–2025 window.  
- The long test horizon provides one continuous performance check across different regimes.

---

## Possible future extension — walk-forward validation

Later, this static scheme can evolve into a **rolling (walk-forward)** structure:

```
Train 1 = 2002–2017   → Test 1 = 2018–2020
Train 2 = 2002–2020   → Test 2 = 2021–2023
Train 3 = 2002–2023   → Test 3 = 2024–2025
```

That setup:
- Evaluates robustness through time,  
- Simulates periodic model retraining,  
- Produces multiple independent out-of-sample metrics.

---

## Outputs
- **Private**: split index file → `private/data_processed/splits/index_train_valid_test.json`
- **Public**: this description of the split and (optionally) a visual aid in `reports/figures/`.

---

## Minimal validation
- Confirm no data from 2018+ leaks into model fitting.  
- Verify that each feature transformation uses parameters fit on 2002–2017 only.  
- Confirm chronological order in all joins and merges.

---

## Public vs. Private
- **Public**: split description, illustrative diagrams.  
- **Private**: exact date indices, seeds, and cross-validation code.
