"""
Streamlit Interactive Application
Manchester City 115 Charges: Econometric Counterfactual & Rival Club Externalities Explorer
"""

import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="City 115 Charges: Econometric Explorer",
    page_icon="⚖️",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        border-left: 4px solid #6CABDD;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .big-num {
        font-size: 26px;
        font-weight: bold;
        color: #1c2c5b;
    }
</style>
""", unsafe_allow_html=True)

# Data Loading
@st.cache_data
def load_all_data():
    pl_panel = pd.read_csv("data/processed/pl_season_panel.csv")
    fin_panel = pd.read_csv("data/processed/club_financials_panel.csv")
    df_titles = pd.read_csv("outputs/tables/alternate_champions_table.csv")
    df_ucl = pd.read_csv("outputs/tables/ucl_displacement_ledger.csv")
    df_damage = pd.read_csv("outputs/tables/club_damage_bill_summary.csv")
    df_breaks = pd.read_csv("outputs/tables/structural_break_tests.csv")
    df_cf = pd.read_csv("outputs/tables/arimax_carryover_results.csv")
    return pl_panel, fin_panel, df_titles, df_ucl, df_damage, df_breaks, df_cf

pl_panel, fin_panel, df_titles, df_ucl, df_damage, df_breaks, df_cf = load_all_data()

# Header
st.title("⚖️ Manchester City 115 Charges: Econometric Impact & Counterfactual Explorer")
st.markdown("*Real data compiled from Companies House filings, Deloitte Football Money League, Football-Data.co.uk, and UEFA Distribution Reports.*")

# Top KPI Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Premier League Titles Affected", "8 Titles", "Liverpool (3), Man Utd (3), Arsenal (2)")
with col2:
    st.metric("UCL Campaigns Displaced", "14 Seasons", "Tottenham (4), Arsenal (3), Leicester (2)...")
with col3:
    st.metric("Total Rival Financial Damages", "£724.6M", "Direct UEFA prize + PL Merit pool")
with col4:
    st.metric("Commercial Rev Structural Break", "p = 1.43e-7", "H0 parameter stability rejected")

st.divider()

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🏆 Resimulated League Tables",
    "💰 Club Damage Bill Ledger",
    "📈 Econometric Forecasting",
    "📊 Financial Distortions (Deloitte/Companies House)"
])

# TAB 1: Resimulated League Tables
with tab1:
    st.subheader("Interactive Season Standings: Official vs. Counterfactual")
    
    col_ctrl1, col_ctrl2 = st.columns([1, 2])
    with col_ctrl1:
        selected_season = st.selectbox("Select Season", df_titles["Season"].tolist(), index=len(df_titles)-1)
        scenario = st.radio("Counterfactual Model", [
            "Scenario A: Compliant City (FFP revenue cap applied)",
            "Scenario B: Organic City (Pre-takeover baseline trend continuation)"
        ])
    
    with col_ctrl2:
        title_row = df_titles[df_titles["Season"] == selected_season].iloc[0]
        st.info(f"""
        **Season {selected_season} Summary:**
        - **Official Champion**: {title_row['Actual_Champion']} ({title_row['Actual_Pts']} pts)
        - **Rightful Champion (Scenario A)**: 🏆 **{title_row['Scenario_A_Champion']}**
        - **Rightful Champion (Scenario B)**: 🏆 **{title_row['Scenario_B_Champion']}**
        - **Title Margin**: {title_row['Points_Margin']} pts
        """)
    
    # Generate Season Table Comparison
    season_table = pl_panel[pl_panel["Season"] == selected_season].copy().reset_index(drop=True)
    
    # Resimulate
    cf_row = df_cf[df_cf["Season"] == selected_season].iloc[0]
    sim_pts = cf_row["Scenario_A_Compliant_Pts"] if "Scenario A" in scenario else cf_row["Scenario_B_Organic_Pts"]
    
    resim_table = season_table.copy()
    resim_table.loc[resim_table["Team"] == "Manchester City", "Pts"] = sim_pts
    resim_table = resim_table.sort_values(by=["Pts", "GD"], ascending=[False, False]).reset_index(drop=True)
    resim_table["Rank"] = resim_table.index + 1
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown(f"**Official Premier League Table ({selected_season})**")
        st.dataframe(season_table[["Rank", "Team", "Pld", "W", "D", "L", "GF", "GA", "GD", "Pts"]].head(10), use_container_width=True)
    with col_t2:
        st.markdown(f"**Resimulated Table ({scenario.split(':')[0]})**")
        st.dataframe(resim_table[["Rank", "Team", "Pld", "W", "D", "L", "GF", "GA", "GD", "Pts"]].head(10), use_container_width=True)

# TAB 2: Club Damage Bill Ledger
with tab2:
    st.subheader("Itemized Financial Damage Ledger by Affected Club")
    st.markdown("Includes direct UEFA Champions League prize and broadcast revenue lost, plus Premier League merit distributions.")
    
    col_d1, col_d2 = st.columns([3, 2])
    with col_d1:
        fig_bar = px.bar(
            df_damage,
            x="Total_Estimated_Financial_Damage_M",
            y="Club",
            orientation="h",
            text="Total_Estimated_Financial_Damage_M",
            color="Total_Estimated_Financial_Damage_M",
            color_continuous_scale="Reds",
            title="Total Estimated Financial Loss per Club (£M)"
        )
        fig_bar.update_layout(yaxis=dict(autorange="reversed"), height=420)
        fig_bar.update_traces(texttemplate='£%{text:.1f}M', textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)
    with col_d2:
        st.dataframe(df_damage, use_container_width=True, height=420)
        
    st.markdown("#### UEFA Champions League 5th-Place Displacements (2010/11 - 2023/24)")
    st.dataframe(df_ucl, use_container_width=True)
    
    if os.path.exists("outputs/motion/damage_bill_race.gif"):
        st.markdown("#### Animated Cumulative Damage Bill Progression")
        st.image("outputs/motion/damage_bill_race.gif", caption="Animated Damage Bill Progression (Looping Animation)", width=650)

# TAB 3: Econometric Forecasting
with tab3:
    st.subheader("Econometric Methodology & Structural Break Verification")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("#### Structural Break Tests (Chow F-Test & Bai-Perron)")
        st.dataframe(df_breaks, use_container_width=True)
        st.caption("P-values < 0.05 confirm rejection of structural stability around takeover and FFP introduction.")
    with col_e2:
        st.markdown("#### Dynamic Carryover Projections (ARIMAX)")
        fig_ts = go.Figure()
        fig_ts.add_trace(go.Scatter(x=df_cf["SeasonStart"], y=df_cf["Actual_Pts"], name="Actual City Pts", line=dict(color="#6CABDD", width=3)))
        fig_ts.add_trace(go.Scatter(x=df_cf["SeasonStart"], y=df_cf["Scenario_A_Compliant_Pts"], name="Scenario A (Compliant)", line=dict(color="#2A9D8F", dash="dash", width=2)))
        fig_ts.add_trace(go.Scatter(x=df_cf["SeasonStart"], y=df_cf["Scenario_B_Organic_Pts"], name="Scenario B (Organic)", line=dict(color="#E63946", dash="dot", width=2)))
        fig_ts.update_layout(title="Points Trajectories & Counterfactuals (1998-2024)", xaxis_title="Season", yaxis_title="Points", height=380)
        st.plotly_chart(fig_ts, use_container_width=True)

# TAB 4: Financial Distortions
with tab4:
    st.subheader("Audited Commercial Sponsorship & Wage Inflation")
    st.markdown("Deloitte Football Money League & Companies House Audited Accounts.")
    
    fig_fin = px.line(
        fin_panel,
        x="SeasonStart",
        y="Commercial",
        color="Team",
        markers=True,
        title="Commercial Sponsorship Revenue (£M): Manchester City vs. English Rivals"
    )
    fig_fin.add_vline(x=2008, line_dash="dash", line_color="gray", annotation_text="Takeover")
    fig_fin.add_vline(x=2011, line_dash="dash", line_color="red", annotation_text="Etihad Deal")
    st.plotly_chart(fig_fin, use_container_width=True)
    
    st.dataframe(fin_panel, use_container_width=True)
