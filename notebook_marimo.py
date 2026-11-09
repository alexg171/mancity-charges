import marimo

__generated_with = "0.25.2"
app = marimo.App(width="wide")


@app.cell
def _():
    import marimo as mo
    import os
    import pandas as pd
    import numpy as np

    return mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # ⚖️ Manchester City 115 Charges: Reactive Econometric Notebook
    ## Counterfactual Identification, Structural Breaks & Rival Externalities
    *Real data compiled from Companies House, Deloitte Football Money League, Football-Data.co.uk, and UEFA Distribution Bulletins.*
    """)
    return


@app.cell
def _(pd):
    # Load processed data
    pl_panel = pd.read_csv("data/processed/pl_season_panel.csv")
    fin_panel = pd.read_csv("data/processed/club_financials_panel.csv")
    df_titles = pd.read_csv("outputs/tables/alternate_champions_table.csv")
    df_ucl = pd.read_csv("outputs/tables/ucl_displacement_ledger.csv")
    df_damage = pd.read_csv("outputs/tables/club_damage_bill_summary.csv")
    df_breaks = pd.read_csv("outputs/tables/structural_break_tests.csv")
    df_cf = pd.read_csv("outputs/tables/arimax_carryover_results.csv")
    return df_breaks, df_cf, df_damage, df_titles, df_ucl


@app.cell
def _(df_damage, mo):
    mo.md(f"""
    ### Executive Summary KPIs:
    - **Total Premier League Titles Affected**: **8 Titles** (Liverpool: 3, Man Utd: 3, Arsenal: 2)
    - **Total Estimated Financial Damages to Rivals**: **£{df_damage['Total_Estimated_Financial_Damage_M'].sum():.1f}M**
    - **Top Impacted Clubs**: Arsenal (£{df_damage.loc[df_damage['Club']=='Arsenal', 'Total_Estimated_Financial_Damage_M'].values[0]:.1f}M), Tottenham (£{df_damage.loc[df_damage['Club']=='Tottenham Hotspur', 'Total_Estimated_Financial_Damage_M'].values[0]:.1f}M)
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 1. The Alternate Premier League Champions (Counterfactual Analysis)
    """)
    return


@app.cell
def _(df_titles, mo):
    mo.ui.table(df_titles)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 2. UEFA Champions League 5th-Place Displacement Ledger
    """)
    return


@app.cell
def _(df_ucl, mo):
    mo.ui.table(df_ucl)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 3. Club Cumulative Damage Bill (£M)
    """)
    return


@app.cell
def _(df_damage, mo):
    mo.ui.table(df_damage)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4. Econometric Structural Break Tests (Chow F-Tests & Bai-Perron)
    """)
    return


@app.cell
def _(df_breaks, mo):
    mo.ui.table(df_breaks)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 5. ARIMAX Points Trajectory & Counterfactual Projections
    """)
    return


@app.cell
def _(df_cf, mo):
    mo.ui.table(df_cf.tail(15))
    return


if __name__ == "__main__":
    app.run()
