"""
Visualization Engine for Substack Publication
Produces publication-quality 300 DPI PNG and SVG charts in outputs/figures/
"""

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd
import numpy as np

OUTPUT_DIR = os.path.join("outputs", "figures")
PROCESSED_DIR = os.path.join("data", "processed")
TABLES_DIR = os.path.join("outputs", "tables")

# Styling Configuration
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["axes.edgecolor"] = "#cccccc"
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["grid.color"] = "#eeeeee"
plt.rcParams["grid.linestyle"] = "--"

# Palette
MC_BLUE = "#6CABDD"
MC_DARK = "#1C2C5B"
RED_ALERT = "#E63946"
GOLD_TROPHY = "#D4AF37"
ACCENT_GREEN = "#2A9D8F"
GRAY_TEXT = "#4A4E69"

def plot_counterfactual_points():
    cf_path = os.path.join(TABLES_DIR, "arimax_carryover_results.csv")
    if not os.path.exists(cf_path):
        return
    df = pd.read_csv(cf_path)
    
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    
    years = df["SeasonStart"]
    
    # Shaded Regulatory Eras
    ax.axvspan(1998, 2008, color="#F1FAEE", alpha=0.6, label="Pre-Takeover Baseline")
    ax.axvspan(2009, 2017, color="#FFE8D6", alpha=0.6, label="115 Charges Window (2009-2017)")
    ax.axvspan(2018, 2023, color="#EDE0D4", alpha=0.5, label="Carryover Era (2018-2023)")
    
    # Plot Trajectories
    ax.plot(years, df["Actual_Pts"], marker="o", color=MC_BLUE, linewidth=3, label="Actual Manchester City Points")
    ax.plot(years, df["Scenario_A_Compliant_Pts"], marker="s", linestyle="--", color=ACCENT_GREEN, linewidth=2.2, label="Scenario A: Compliant FFP Bound")
    ax.plot(years, df["Scenario_B_Organic_Pts"], marker="^", linestyle=":", color=RED_ALERT, linewidth=2.2, label="Scenario B: Organic Pre-2008 Trajectory")
    
    # Highlight Centurions and key titles
    ax.annotate("100 Pts (Centurions)", xy=(2017, 100), xytext=(2014.5, 103),
                arrowprops=dict(facecolor=MC_DARK, arrowstyle="->", lw=1),
                fontweight="bold", color=MC_DARK, fontsize=10)
    ax.annotate("First Title (89 Pts)", xy=(2011, 89), xytext=(2008.5, 92),
                arrowprops=dict(facecolor=MC_DARK, arrowstyle="->", lw=1),
                fontweight="bold", color=MC_DARK, fontsize=10)
    
    ax.set_title("Manchester City: Actual vs. Counterfactual Points Trajectories (1998–2024)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Season Starting Year", fontsize=11, labelpad=10)
    ax.set_ylabel("Premier League Points", fontsize=11, labelpad=10)
    ax.set_ylim(30, 110)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    
    ax.legend(frameon=True, facecolor="white", edgecolor="#cccccc", fontsize=10, loc="lower right")
    plt.tight_layout()
    
    fig.savefig(os.path.join(OUTPUT_DIR, "counterfactual_points_timeline.png"), dpi=300)
    fig.savefig(os.path.join(OUTPUT_DIR, "counterfactual_points_timeline.svg"))
    plt.close()
    print("[+] Saved counterfactual_points_timeline.png")

def plot_commercial_revenue_explosion():
    fin_path = os.path.join(PROCESSED_DIR, "club_financials_panel.csv")
    if not os.path.exists(fin_path):
        return
    df = pd.read_csv(fin_path)
    
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    
    clubs = ["Manchester City", "Arsenal", "Liverpool", "Tottenham Hotspur", "Everton"]
    colors = {
        "Manchester City": MC_BLUE,
        "Arsenal": "#EF0107",
        "Liverpool": "#C8102E",
        "Tottenham Hotspur": "#132257",
        "Everton": "#003399"
    }
    
    for club in clubs:
        sub = df[df["Team"] == club].sort_values("SeasonStart")
        if not sub.empty:
            lw = 3.5 if club == "Manchester City" else 1.8
            alpha = 1.0 if club == "Manchester City" else 0.7
            zorder = 5 if club == "Manchester City" else 2
            ax.plot(sub["SeasonStart"], sub["Commercial"], marker="o", markersize=5,
                    color=colors.get(club, "#555555"), linewidth=lw, alpha=alpha, label=club, zorder=zorder)
            
    # Highlight 2008 takeover and Etihad deal
    ax.axvline(2008, color="#888888", linestyle="--", lw=1.2, label="Abu Dhabi Takeover (2008)")
    ax.axvline(2011, color=RED_ALERT, linestyle=":", lw=1.5, label="Etihad £400M Deal (2011)")
    
    ax.set_title("The Commercial Sponsorship Explosion: Manchester City vs. English Peers", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Season Starting Year", fontsize=11, labelpad=10)
    ax.set_ylabel("Commercial / Sponsorship Revenue (£M)", fontsize=11, labelpad=10)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("£{x:,.0f}M"))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    
    ax.legend(frameon=True, facecolor="white", edgecolor="#cccccc", fontsize=10, loc="upper left")
    plt.tight_layout()
    
    fig.savefig(os.path.join(OUTPUT_DIR, "commercial_revenue_vs_peers.png"), dpi=300)
    fig.savefig(os.path.join(OUTPUT_DIR, "commercial_revenue_vs_peers.svg"))
    plt.close()
    print("[+] Saved commercial_revenue_vs_peers.png")

def plot_rival_financial_damage():
    dmg_path = os.path.join(TABLES_DIR, "club_damage_bill_summary.csv")
    if not os.path.exists(dmg_path):
        return
    df = pd.read_csv(dmg_path)
    
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    
    y_pos = np.arange(len(df))
    bars = ax.barh(y_pos, df["Total_Estimated_Financial_Damage_M"], color="#2B2D42", height=0.65, edgecolor="#111111", lw=0.5)
    
    # Highlight top 3 victims
    if len(bars) > 0: bars[0].set_color("#E63946") # Arsenal
    if len(bars) > 1: bars[1].set_color("#457B9D") # Spurs
    if len(bars) > 2: bars[2].set_color("#E63946") # Liverpool
    
    for i, v in enumerate(df["Total_Estimated_Financial_Damage_M"]):
        ax.text(v + 3, i, f"£{v:.1f}M", va="center", fontweight="bold", fontsize=10, color="#1D3557")
        
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df["Club"], fontsize=11, fontweight="medium")
    ax.invert_yaxis()
    ax.set_xlabel("Estimated Cumulative Financial Loss (£M)", fontsize=11, labelpad=10)
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("£{x:,.0f}M"))
    ax.set_xlim(0, max(df["Total_Estimated_Financial_Damage_M"]) * 1.15)
    
    ax.set_title("Cumulative Financial Damage Bill by Club (Lost UCL Prize Pool + Domestic Merit)", fontsize=13, fontweight="bold", pad=15)
    plt.tight_layout()
    
    fig.savefig(os.path.join(OUTPUT_DIR, "rival_financial_damage_bar.png"), dpi=300)
    fig.savefig(os.path.join(OUTPUT_DIR, "rival_financial_damage_bar.svg"))
    plt.close()
    print("[+] Saved rival_financial_damage_bar.png")

def plot_synthetic_control():
    scm_path = os.path.join(TABLES_DIR, "synthetic_control_trajectory.csv")
    if not os.path.exists(scm_path):
        return
    df = pd.read_csv(scm_path)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8.5), dpi=300, sharex=True, gridspec_kw={"height_ratios": [2, 1]})
    
    years = df["SeasonStart"]
    
    # Panel 1: Trajectory
    ax1.plot(years, df["Actual_City_Pts"], marker="o", color=MC_BLUE, lw=2.8, label="Actual Manchester City")
    ax1.plot(years, df["Synthetic_City_Pts"], marker="s", linestyle="--", color="#457B9D", lw=2.2, label="Synthetic Manchester City (Donor Pool Weighted)")
    ax1.axvline(2008, color=RED_ALERT, linestyle=":", lw=1.8, label="Intervention / Takeover (2008)")
    
    ax1.set_ylabel("Premier League Points", fontsize=11)
    ax1.set_title("Synthetic Control Method: Actual City vs. Synthetic Peer Counterfactual", fontsize=13, fontweight="bold")
    ax1.legend(loc="upper left", frameon=True)
    
    # Panel 2: Treatment Gap
    ax2.bar(years, df["Treatment_Effect_Gap"], color=np.where(df["Treatment_Effect_Gap"] >= 0, RED_ALERT, "#457B9D"), alpha=0.85, width=0.7)
    ax2.axhline(0, color="#333333", lw=0.8)
    ax2.axvline(2008, color=RED_ALERT, linestyle=":", lw=1.8)
    ax2.set_ylabel("Treatment Effect Gap (Pts)", fontsize=11)
    ax2.set_xlabel("Season Starting Year", fontsize=11)
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(2))
    
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "synthetic_control_gap.png"), dpi=300)
    fig.savefig(os.path.join(OUTPUT_DIR, "synthetic_control_gap.svg"))
    plt.close()
    print("[+] Saved synthetic_control_gap.png")

def plot_var_impulse_response():
    irf_path = os.path.join(TABLES_DIR, "var_impulse_response.csv")
    if not os.path.exists(irf_path):
        return
    df = pd.read_csv(irf_path)
    
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    h = df["Horizon_Years"]
    ax.plot(h, df["Points_Response_to_Wage_Shock"], marker="o", color=MC_BLUE, lw=2.5, label="Points Response to Wage Shock")
    ax.plot(h, df["Points_Response_to_Commercial_Shock"], marker="s", linestyle="--", color=RED_ALERT, lw=2.2, label="Points Response to Commercial Shock")
    ax.axhline(0, color="#666666", linestyle=":", lw=1)
    
    ax.set_title("Vector Autoregression (VAR): Orthogonalized Impulse Response to Spending", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Forecast Horizon (Seasons Ahead)", fontsize=11, labelpad=10)
    ax.set_ylabel("Impulse Response in League Points", fontsize=11, labelpad=10)
    ax.legend(frameon=True)
    plt.tight_layout()
    
    fig.savefig(os.path.join(OUTPUT_DIR, "var_impulse_response.png"), dpi=300)
    fig.savefig(os.path.join(OUTPUT_DIR, "var_impulse_response.svg"))
    plt.close()
    print("[+] Saved var_impulse_response.png")

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating all publication figures for Substack...")
    plot_counterfactual_points()
    plot_commercial_revenue_explosion()
    plot_rival_financial_damage()
    plot_synthetic_control()
    plot_var_impulse_response()
    print("All Substack publication figures generated successfully!")
