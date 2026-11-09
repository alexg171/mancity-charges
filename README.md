# Manchester City 115 Charges: Econometric Impact & Counterfactual Engine

An empirical research package, econometric modeling pipeline, and multimedia visualization suite analyzing the sporting and financial consequences of the Premier League's 115 charges against Manchester City (2009/10–2017/18) and the subsequent carryover era (2018/19–2023/24).

---

## 🚀 Live Deployed Applications & Reports

| Application | Description | Live Links |
| :--- | :--- | :--- |
| **📊 Quarto Econometric Report** | Complete empirical compendium containing regression tables, structural break tests, counterfactual projections, and publication charts. | • **Live Report**: [alexg171.github.io/mancity-charges/analysis.html](https://alexg171.github.io/mancity-charges/analysis.html)<br>• **Local File**: [`analysis.html`](analysis.html) |
| **⚡ Streamlit Interactive Dashboard** | Interactive web app with scenario sliders, alternate table re-simulations, and rival club damage ledgers. | • **Live Dashboard**: [mancity-charges.streamlit.app](https://mancity-charges.streamlit.app)<br>• **App File**: [`app.py`](app.py) |
| **📓 Marimo Reactive Notebook** | Transparent, reactive Python computational notebook for reproducible econometric analysis. | • **Notebook File**: [`notebook_marimo.py`](notebook_marimo.py) |

---

## 📁 Repository Structure

```
city charges/
├── data/
│   ├── SOURCES.md                # Comprehensive citations, Companies House #, UEFA bulletins
│   ├── raw/                      # Downloaded match CSVs (1993/94 - 2023/24) via football-data.co.uk
│   └── processed/
│       ├── pl_season_panel.csv       # Full 32-season Premier League table panel (1992-2024)
│       ├── club_financials_panel.csv # Audited financials (Turnover, Commercial, Wages, Net Spend)
│       └── ucl_prize_matrix.csv      # UEFA official Champions League prize distributions
├── src/
│   ├── data_loader.py            # Automated scraper & verified panel builder
│   ├── econometrics.py           # Bai-Perron breaks, Chow F-tests, ARIMAX, VAR/IRF, Synthetic Control
│   ├── simulation.py             # Scenario A & B resimulations, alternate champions, rival damage
│   └── visualization.py          # 300 DPI publication plots (PNG/SVG) for Substack
├── outputs/
│   ├── figures/                  # 300 DPI publication figures (Substack horizontal 16:9)
│   │   ├── counterfactual_points_timeline.png (.svg)
│   │   ├── commercial_revenue_vs_peers.png (.svg)
│   │   ├── rival_financial_damage_bar.png (.svg)
│   │   ├── synthetic_control_gap.png (.svg)
│   │   └── var_impulse_response.png (.svg)
│   ├── tables/                   # Clean Markdown & CSV tables ready for Substack
│   │   ├── alternate_champions_table.md (.csv)
│   │   ├── ucl_displacement_ledger.md (.csv)
│   │   ├── club_damage_bill_summary.md (.csv)
│   │   ├── structural_break_tests.md (.csv)
│   │   ├── arimax_carryover_results.md (.csv)
│   │   ├── var_impulse_response.md (.csv)
│   │   └── synthetic_control_weights.md (.csv)
│   └── motion/                   # Animated b-roll assets for Substack / video
│       └── damage_bill_race.gif
├── analysis.qmd                  # Quarto technical compendium
├── analysis.html                 # Rendered standalone HTML technical report
├── app.py                        # Streamlit interactive application
├── notebook_marimo.py            # Reactive Marimo notebook
└── requirements.txt              # Project dependencies
```

---

## ⚡ Running Locally

### 1. Launch Streamlit Dashboard
```bash
streamlit run app.py
```

### 2. Open Quarto Technical Report
Open [`analysis.html`](analysis.html) directly in any web browser, or re-render:
```bash
quarto render analysis.qmd
```

### 3. Launch Marimo Notebook
```bash
marimo edit notebook_marimo.py
```

### 4. Regenerate All Figures & Tables
```bash
python src/data_loader.py
python src/econometrics.py
python src/simulation.py
python src/visualization.py
```

---

## 📊 Key Empirical Findings

1. **Econometric Structural Breaks**:
   * **Commercial Revenue**: Rejection of parameter stability at the 2008 takeover ($F = 40.43, p = 1.43 \times 10^{-7}$) and the 2011 Etihad deal ($F = 39.58, p = 1.68 \times 10^{-7}$).
   * **Wage Bill**: Significant structural break at 2008 ($F = 6.36, p = 0.0077$).
   * **Net Spend**: Break at 2008 ($F = 4.88, p = 0.019$) and significant shift post-2018 ($F = 10.43, p = 0.00088$).

2. **The 8 Premier League Titles Affected**:
   * **2011/12**: Manchester United (tied on 89 pts, lost on GD)
   * **2013/14**: Liverpool (finished 2nd by 2 pts)
   * **2017/18**: Manchester United (finished 2nd)
   * **2018/19**: Liverpool (finished 2nd with 97 pts, lost by 1 pt)
   * **2020/21**: Manchester United (finished 2nd)
   * **2021/22**: Liverpool (finished 2nd with 92 pts, lost by 1 pt)
   * **2022/23**: Arsenal (finished 2nd)
   * **2023/24**: Arsenal (finished 2nd by 2 pts)

3. **Cumulative Financial Damage to Rivals**:
   * **Total Rival Damage Bill**: **-£724.6M** in direct UEFA prize money, broadcast market pools, and domestic merit payouts.
   * **Top Affected Clubs**:
     * **Arsenal**: **-£203.1M** (2 lost titles, 3 lost UCL campaigns)
     * **Tottenham Hotspur**: **-£167.7M** (4 lost UCL campaigns in 2011, 2013, 2015, 2024)
     * **Liverpool**: **-£123.9M** (3 lost titles, 1 lost UCL campaign)
     * **Leicester City**: **-£107.5M** (2 lost UCL campaigns in 2020, 2021)
     * **Manchester United**: **-£105.4M** (3 lost titles, 1 lost UCL campaign in 2016)
     * **Chelsea**: **-£49.7M**
     * **Everton**: **-£34.8M** (denied historic UCL qualification in 2014 with 72 pts)
     * **Newcastle United**: **-£32.5M** (denied UCL in 2012)
