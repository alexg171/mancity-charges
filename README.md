# Manchester City 115 Charges: Econometric Impact & Counterfactual Engine

An empirical research package, econometric modeling pipeline, and multimedia visualization suite analyzing the sporting and financial consequences of the Premier League's 115 charges against Manchester City (2009/10–2017/18) and the subsequent carryover era (2018/19–2023/24).

---

## 🚀 Live Applications & Interactive Reports

| Application | Description | Links & Deployment |
| :--- | :--- | :--- |
| **📊 Quarto Technical Report** | Full empirical compendium containing regression tables, structural break tests, counterfactual projections, and publication charts. | • **Local Report**: [Open `analysis.html`](analysis.html)<br>• **Source Code**: [`analysis.qmd`](analysis.qmd)<br>• **Web Deploy**: Run `quarto publish quarto-pub analysis.qmd` or `quarto publish netlify analysis.qmd` |
| **⚡ Streamlit Interactive Explorer** | Dynamic dashboard with counterfactual scenario sliders, alternate table re-simulations, and rival damage calculators. | • **App Code**: [`app.py`](app.py)<br>• **Launch Locally**: `streamlit run app.py`<br>• **Cloud Deploy**: Free via [Streamlit Community Cloud](https://share.streamlit.io/) |
| **📓 Marimo Reactive Notebook** | Transparent, reactive Python computational notebook for reproducible econometric analysis. | • **Notebook Code**: [`notebook_marimo.py`](notebook_marimo.py)<br>• **Launch Locally**: `marimo edit notebook_marimo.py` |

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
├── analysis.qmd                  # Quarto technical compendium (run: quarto render analysis.qmd)
├── analysis.html                 # Rendered standalone HTML technical report
├── app.py                        # Streamlit interactive application (run: streamlit run app.py)
├── notebook_marimo.py            # Reactive Marimo notebook (run: marimo edit notebook_marimo.py)
└── requirements.txt              # Project dependencies
```

---

## ⚡ How to Run

### 1. Interactive Streamlit Dashboard
Launch the interactive web app to explore alternate league tables, toggle counterfactual scenarios, and view the rival club damage bill:
* **File**: [`app.py`](app.py)
```bash
streamlit run app.py
```

### 2. Standalone Quarto Technical Report
* **Rendered Report**: [Open `analysis.html`](analysis.html) directly in any web browser.
* **Source**: [`analysis.qmd`](analysis.qmd)
* **Re-render Command**:
```bash
quarto render analysis.qmd
```
* **Deploy to Web**:
```bash
quarto publish quarto-pub analysis.qmd
```

### 3. Reactive Marimo Notebook
Open the reactive Python notebook in your browser:
* **File**: [`notebook_marimo.py`](notebook_marimo.py)
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
