# Factor Fund — Factor-based & ML-driven Equity Strategy

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

A modular, production-style research pipeline for a systematic equity strategy
combining **risk factors**, **machine learning**, and **portfolio construction**.

All datasets in this public version are **synthetic or anonymized**.  
The goal is to serve as a **professional showcase** of methodology,
architecture, modeling workflow, and engineering quality.

---

## 🔧 Pipeline Overview

The project is structured into **five modules (M1–M5)**:



```
M1 — Data Preparation  
M2 — Prediction Model  
M3 — Portfolio Construction  
M4 — Backtesting & Performance  
M5 — Factor Analysis  
```

This architecture mirrors real-world quant research and production pipelines,
while keeping the public version clean and reproducible.

---

## 📦 Repository Structure


```
factor-fund/
├─ src/factor_fund/
│  ├─ data/         # M1 – data cleaning, factor engineering
│  ├─ models/       # M2 – model training and inference
│  ├─ portfolio/    # M3 – portfolio construction logic
│  ├─ backtesting/  # M4 – performance and analytics
│  └─ analysis/     # M5 – factor importance, exposures, premia
├─ notebooks/       # High-level walkthroughs and demos
├─ data/examples/   # Synthetic example datasets
└─ docs/presentation/slides.qmd
```


---

## 🧩 Module Summary

### **M1 — Data Preparation**
- Builds synthetic or real factor data  
- Features include Value, Momentum, Quality, Size, Volatility  
- Normalization, winsorization, ranking  

### **M2 — Prediction Model**
- Cross-sectional modeling of forward returns  
- Supports Ridge, Lasso, RandomForest, XGBoost, Neural Networks  
- Outputs:

```text
date, ticker, model_score
```


### **M3 — Portfolio Construction**
- Ranking-based long-only or long/short portfolios  
- Constraints: max/min weights, turnover, normalization  
- Outputs:  

```text
date, ticker, target_weight
```

### **M4 — Backtesting & Performance**
- Daily PnL  
- Annualized vol  
- Sharpe, Sortino  
- Drawdown curves  
- Benchmark-relative returns  

### **M5 — Factor Analysis**
- Feature importance (e.g., SHAP)  
- Factor exposure (betas)  
- Factor premia (future returns of factors)

---

## 📊 Example Output (from synthetic demo)

### Model Diagnostic (M2)

*(Image omitted in README to avoid broken link — can be added later)*

Example: real vs. predicted returns from the synthetic Ridge model.

### Sample Portfolio (M3)

| date       | ticker | model_score | weight |
| ---------- | ------ | ----------- | ------ |
| 2024-01-31 | AAA3   | 0.0789      | 0.5    |
| 2024-01-31 | BBB4   | 0.0786      | 0.5    |
| 2024-01-31 | EEE3   | 0.0401      | 0.0    |


---
## 🧪 Synthetic Demo Pipeline (M1–M4)

A fully functional **synthetic end-to-end pipeline** is included using only Python scripts.

### ▶ How to run

With your Python environment activated (e.g., conda env `factors`):

```bash
cd factor-fund

# M1 — Generate synthetic factor matrix
python notebooks/M1_generate_factor_matrix_demo.py

# M2 — Train Ridge model and save artifacts
python notebooks/M2_model_training_demo.py

# M3 — Build a simple long-only portfolio from model scores
python notebooks/M3_portfolio_demo.py

# M4 — Backtest model vs equal-weight benchmark
python notebooks/M4_backtest_demo.py
```

### ▶ This will generate

```text
data/examples/factor_matrix_demo.csv
models/ridge_demo.pkl
models/scaler_demo.pkl
models/ridge_demo_y_true_vs_pred.png
data/examples/portfolio_weights_demo.csv
```

## 🧰 Environment Setup (optional)

Using virtualenv

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac / Linux
pip install -r requirements.txt
```

Using conda:

```bash
conda create -n factor-fund python=3.11 -y
conda activate factor-fund
pip install -r requirements.txt
```



requirements.txt includes:

```bash
numpy
pandas
scikit-learn
matplotlib
joblib
```

## 🎯 Roadmap


**Short term**
- Add synthetic end-to-end demo  
- Add performance figures and factor exposure plots  
- Add minimal CI + unit tests  

**Medium term**
- Add advanced model architectures  
- Add multi-country universes  
- Expand factor research modules  

## 👤 About the Author

Quantitative Portfolio Manager & CTO with experience in:

- Factor investing  
- Machine learning for financial prediction  
- Portfolio optimization  
- Credit & multimarket funds  
- Daily research pipelines and production automation  

This project is a curated public showcase of real-world quantitative work.











