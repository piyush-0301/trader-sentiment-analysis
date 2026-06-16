
# Trader Performance vs Market Sentiment (Hyperliquid Analysis)

This repository contains the completed Round-0 Assignment for the Data Science / Analytics Intern role at Primetrade.ai. The project explores the quantitative relationship between crypto market sentiment (Bitcoin Fear & Greed Index) and real trader execution behavior and performance on Hyperliquid. 

## 📁 Repository Structure
```text
├── images/
│   ├── sentiment_pnl_analysis.png
│   ├── trading_frequency_vs_winrate.png
│  
├── notebooks/
│   └── sentiment_analysis.ipynb
├── app.py
├── README.md
└── requirements.txt

🛠️ Setup & Local Execution
To replicate this environment, inspect the analysis notebook, or run the interactive dashboard script locally, follow the steps below:

Clone the repository:
git clone https://github.com/piyush-0301/trader-sentiment-analysis.git

Install required dependencies:
pip install -r requirements.txt

Launch the Interactive Dashboard (Bonus Milestone):
streamlit run app.py

🔬 Methodology & Data Preparation
Data Pipeline: Standardized 2,644 historical market sentiment frames and aligned them directly with 211,224 localized transaction data rows from Hyperliquid.

Alignment Matrix: Handled high-frequency Timestamp IST data points, normalising transactional timestamps down to daily matchable date strings (YYYY-MM-DD). Missing closing metrics were cleaned and imputed with zero values to maintain database integrity.

Feature Engineering: Extracted critical daily KPIs per account including: daily_pnl, trade_count, avg_trade_size_usd, and conditional is_profitable direction tags.

Behavioral Segmentation: Applied statistical splits to categorize unique user accounts into distinct structural archetypes:

Hyper-Active Traders: High-velocity scalpers trading rapid order flow.

Patient Traders: Lower-frequency swing accounts looking for larger, selective price moves.

🧠 Core Insights (Part B Findings)
1. The Overtrading Panic Trap (Extreme Fear)
Under macro market panic (Extreme Fear), trading volume dramatically scales up to its highest baseline across the entire dataset—averaging 133.75 trades per account per day. However, this hyper-activity results in subpar returns ($4,619.43 average daily PnL), proving that traders systematically over-trade and churn capital inefficiently during market panics.

2. The Momentum Rider Phenomenon (Hyper-Active Archetype)
Hyper-Active accounts operate with incredible predictive edge during high-velocity, trending market environments. Under Extreme Greed conditions, this segment peaks in execution efficiency—achieving a remarkable 78.49% win rate and generating $5,918.65 in average daily PnL. Conversely, they severely decay on standard Greed days ($2,293.01 PnL) due to over-brokering low-volatility, flat ranges.

3. The Contrarian Sniper Phenomenon (Patient Archetype)
Patient accounts display a completely inverse performance matrix. They struggle to find an edge in trending environments (dropping to an abysmal 43.50% win rate during Extreme Greed). However, on normal Greed days, they hit a maximum performance sweet spot, extracting an outstanding $6,663.11 average daily PnL. This proves they rely on massive risk-to-reward ratios rather than high raw win rates to achieve outsized returns.

💡 Actionable Strategy Formulations (Part C)
Based on the empirical evidence extracted above, the following programmatic trading engine constraints are recommended:

Rule 1 (Hyper-Active Velocity Brake): When market sentiment metrics shift to a standard Greed or Neutral regime, the exchange should dynamically reduce maximum allowed order velocity caps or adjust maker/taker trading fee tiers for the Hyper-Active trader cluster.

Rationale: Data proves their performance collapses to its absolute lowest ($2,293.01 PnL) trying to scalp non-trending, choppy environments.

Rule 2 (Patient Trend Risk Buffer): When sentiment hits an Extreme Greed state, trigger automated platform alerts or dynamically scale down maximum position size limits specifically for the Patient trader cluster.

Rationale: Patient traders hold a strong structural edge on standard Greed days ($6,663.11 PnL), but their performance falls off drastically during Extreme Greed because their mean-reversion habits cause them to fight explosive, runaway momentum trends.

🚀 Completed Advanced Bonus Milestones
1. Predictive Machine Learning Model
Trained an optimized Random Forest Classifier to forecast next-day trader profitability using integrated sentiment and volume footprints.

Model Accuracy: 69.02%

Profitable Class (1) Precision / Recall: 72% / 79%

Strategic Utility: Proves that combining market sentiment with basic position velocity yields highly significant predictive signals regarding whether a trading profile will successfully capture capital on a given day.

2. Behavioral Clustering Archetypes
Deployed an unsupervised machine learning pipeline (K-Means Clustering) using scaled data features to automatically segment user accounts into algorithmic scalpers, whale swing accounts, and consistent earners, eliminating manual parameters.

3. Lightweight Streamlit Dashboard
Programmed an interactive user interface (app.py) mapping performance stats across various market moods to make the extracted insights easy to explore.

