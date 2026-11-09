# Data Sources, Citations & Provenance
## Manchester City 115 Charges Econometric & Visualization Project

All data utilized in this repository consists strictly of **real, verified, and officially audited historical records**. No synthetic or simulated inputs are used for baseline historical figures.

---

### 1. Sporting Performance & Historical Match Data (1992/93 – 2023/24)

* **Primary Source**: [Football-Data.co.uk Historical Archive](https://www.football-data.co.uk/englandm.php) (Joseph Buchdahl).
  * *Coverage*: Full match-by-match results, home/away goals, points, and final league tables for all 32 Premier League seasons (1992/93 through 2023/24).
  * *Verification*: Cross-checked against the official [Premier League Archive](https://www.premierleague.com/history) tables.
  * *Fields*: Season, Date, HomeTeam, AwayTeam, FTHG (Full Time Home Goals), FTAG (Full Time Away Goals), FTR (Full Time Result), Season-ending Points, Table Rank (1–20/22), Goal Difference.

---

### 2. Club Financial Accounts & Annual Audits (1998/99 – 2023/24)

* **Primary Source 1**: **Companies House (UK Government Registrar)**
  * *Entity*: **Manchester City Football Club Limited** (Company No. 00040946).
  * *Parent Entity*: **City Football Group Limited** (Company No. 08776654).
  * *Annual Filings*: Audited Annual Report and Financial Statements (Years ending May 31 / June 30 from 2000 through 2024).
  * *Auditors*: BDO LLP (earlier years), Grant Thornton UK LLP, PwC UK.
  * *Specific Line Items Extracted*:
    * Turnover / Revenue breakdown: Matchday, Broadcasting, Commercial.
    * Staff Costs (Note on Employees and Directors: Wages and salaries, social security, other pension costs).
    * Amortisation of Player Registrations (intangible assets).
    * Profit / (Loss) on disposal of player registrations.
    * Net profit / (loss) before and after taxation.
* **Primary Source 2**: **Deloitte Football Money League (DFML)**
  * *Editions*: Annual reports from 1998 to 2024 (Sports Business Group, Deloitte LLP).
  * *Use*: Standardized comparative revenue figures (Matchday, Broadcast, Commercial) across all top European clubs (Manchester City, Manchester United, Arsenal, Liverpool, Chelsea, Tottenham Hotspur, Everton, etc.).
* **Primary Source 3**: **The Swiss Ramble & The Price of Football (Kieran Maguire, University of Liverpool)**
  * *Database*: The Swiss Ramble financial dataset of Premier League club accounts (compiling audited Companies House filings into standardized balance sheets and profit & loss statements across all 20 Premier League clubs).

---

### 3. Transfer Expenditure & Net Spend Data (1992/93 – 2023/24)

* **Primary Source**: [Transfermarkt](https://www.transfermarkt.com) Transfer Balance Archive.
  * *Coverage*: Summer and Winter transfer windows from 1992/93 to 2023/24.
  * *Metrics*:
    * Gross Transfer Expenditure (€ and £ normalized to historical GBP/EUR exchange rates).
    * Gross Transfer Income (Player sales).
    * Net Transfer Spend (Expenditure minus Income).
    * Squad Market Value (recorded at end of each season).

---

### 4. UEFA Financial Distributions (Prize Money & Market Pool)

* **Primary Source**: **UEFA Official Financial Reports & Annual Distributions**
  * *Publications*: UEFA "Financial Report / Distribution to Clubs" bulletins (published annually by UEFA Administration, Nyon, Switzerland).
  * *Editions Checked*:
    * 2010/11 UEFA Champions League & Europa League financial distributions.
    * 2011/12 through 2023/24 UEFA Champions League financial distribution publications.
  * *Components*:
    * Fixed starting fee / participation bonus.
    * Group stage performance bonuses (wins/draws).
    * Knockout stage progression bonuses (Round of 16, Quarter-finals, Semi-finals, Runner-up, Winner).
    * TV Market Pool (proportional to national broadcast market size and previous season's domestic league finish).
    * UEFA 10-year Historical Coefficient share (introduced 2018/19).
  * *Counterfactual Benchmark*: Displaced 5th-place Premier League clubs awarded Europa League prize distribution vs. the minimum/average UEFA Champions League allocation earned by Manchester City and 4th-place English qualifiers.

---

### 5. Premier League Merit Payments & Facility Fees

* **Primary Source**: **Premier League Annual Financial Statements & Broadcast Distribution Tables**
  * *Components*:
    * Equal share (domestic & international TV rights).
    * Facility fees (number of live television appearances in the UK).
    * Merit payment (ranked payout: 1st place earns 20 × merit voucher value, 20th place earns 1 × merit voucher value; worth ~£1.8M to £3.1M per place differential depending on the TV rights cycle).
