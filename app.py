
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Primetrade.ai Alpha Dashboard", layout="wide")

st.title("📊 Hyperliquid Trader Behavior & Sentiment Analytics")
st.markdown("Interactive analysis tracking how market fear and greed impact trader profiles.")

# Sidebar Controls
st.sidebar.header("Dashboard Filters")
sentiment_filter = st.sidebar.selectbox(
    "Select Market Mood Focus", 
    ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
)

# Mock stats component for visualization demonstration 
st.subheader(f"🎯 Insights Profile for {sentiment_filter} Conditions")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Systemic Win Rate Threshold", value="68.2%" if "Greed" in sentiment_filter else "60.1%")
with col2:
    st.metric(label="Target Market Volume Index", value="$8,975 USD" if "Fear" in sentiment_filter else "$5,371 USD")
with col3:
    st.metric(label="Risk Action Multiplier", value="0.5x Scale Down" if "Fear" in sentiment_filter else "Unrestricted")

st.info("💡 **Hiring Team Note:** To execute this live dashboard locally, pull down the repo and run: `streamlit run app.py` from your terminal.")
