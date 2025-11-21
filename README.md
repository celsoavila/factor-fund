# Factor Fund — Factor-based & ML-driven Equity Strategy

This repository presents a clean, modular and production-style research pipeline  
for a systematic equity strategy combining **risk factors** and **machine learning**.

> ⚠️ All datasets used in this repository are synthetic or anonymized.  
> The goal of this project is to serve as a **public showcase** of methodology,
> architecture, and code quality for professional and academic purposes.

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

This modular architecture reflects the design of real-world quant pipelines,
while keeping the public version simple, reproducible and easy to understand.

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
- Cleans raw data (prices, returns, fundamentals)
- Builds standard factor features:
  - Value, Momentum, Quality, Size, Volatility
- Applies scaling, winsorization and ranking  
- Produces the **Factor Matrix**, the main input for M2

---

### **M2 — Prediction Model**
A cross-sectional model predicting relative future performance.

Supports:
- Linear models (Ridge, Lasso)
- Tree-based models (RandomForest, XGBoost)
- Neural networks (Keras/TensorFlow)

Outputs:

date, ticker, model_score


---

### **M3 — Portfolio Construction**
Transforms model scores into implementable target weights under:

- Long-only or long/short rules  
- Maximum/minimum weights  
- Normalization and bucket-based ranking  
- Turnover controls (optional)

Output:

date, ticker, target_weight


---

### **M4 — Backtesting & Performance**

Computes:
- Daily PnL  
- Benchmark-relative returns  
- Annualized volatility  
- Sharpe, Sortino  
- Max drawdown  
- (% of CDI for Brazilian context)

Generates visualizations stored in `reports/figures/`.

---

### **M5 — Factor Analysis**

Includes:
- **Factor importance** (e.g., SHAP or model-based metrics)
- **Factor exposure** (portfolio betas)
- **Factor premia** (future returns of each factor)

This module provides interpretability and economic insight.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/celsoavila/factor-fund.git
cd factor-fund
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Explore the pipeline

Open the notebooks:

- `M1_data_prep.ipynb`
- `M2_model_training.ipynb`
- `M3_portfolio.ipynb`
- `M4_backtest.ipynb`
- `M5_factor_analysis.ipynb`

---
## 🧪 Synthetic demo pipeline (M1–M3)

This repository includes a small **end-to-end demo** using synthetic data,
implemented as simple Python scripts (no external data required).

With your Python environment activated (e.g., conda env `factors`), run:

```bash
cd path/to/factor-fund

# M1 – Generate synthetic factor matrix
python notebooks/00_generate_factor_matrix_demo.py

# M2 – Train Ridge model and save artifacts
python notebooks/M2_model_training_demo.py

# M3 – Build a simple long-only portfolio from model scores
python notebooks/M3_portfolio_demo.py
```

---
## 🎯 Roadmap

**Short term**
- Add synthetic end-to-end demo  
- Add performance figures and factor exposure plots  
- Add minimal CI + unit tests  

**Medium term**
- Add advanced model architectures  
- Add multi-country universes  
- Expand factor research modules  


---
## 👤 About the Author

Quantitative Portfolio Manager & CTO with experience in:

- Factor investing  
- Machine learning for financial prediction  
- Portfolio optimization  
- Credit & multimarket funds  
- Daily research pipelines and production automation  

This project is a curated public showcase of real-world quantitative work.







