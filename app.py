import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Voltas Financial Dashboard", layout="wide")

df = pd.read_csv("company_financials_clean.csv")

st.title("Financial Dashboard: Voltas")

# KPI cards
c1, c2, c3 = st.columns(3)
c1.metric("Latest Sales (Cr)", f"{df['Sales'].iloc[-1]:,.0f}")
c2.metric("Latest Net Profit (Cr)", f"{df['Net_Profit'].iloc[-1]:,.0f}")
c3.metric("Latest OPM %", f"{df['OPM_Percent'].iloc[-1]:.1f}%")

st.markdown("---")

# Chart 1: Sales & Net Profit trend
st.subheader("Sales & Net Profit Trend")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['Period'], df['Sales'], marker='o', label='Sales')
ax1.plot(df['Period'], df['Net_Profit'], marker='o', label='Net Profit')
ax1.legend()
plt.xticks(rotation=45)
st.pyplot(fig1)

# Chart 2: OPM % bar chart
st.subheader("Operating Profit Margin (%)")
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.bar(df['Period'], df['OPM_Percent'], color='teal')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Chart 3: Box plot of Net Profit by Profit Trend
st.subheader("Net Profit Distribution by Profit Trend")
fig3, ax3 = plt.subplots(figsize=(6, 4))
df.boxplot(column='Net_Profit', by='Profit_Trend', ax=ax3)
plt.title("")
plt.suptitle("")
st.pyplot(fig3)

st.markdown("---")

# Model comparison table
st.subheader("Model Comparison: Predicting Profit Trend")
results = pd.DataFrame({
    'Model': ['Logistic Regression', 'Decision Tree'],
    'Accuracy': [0.75, 0.75]
})
st.table(results)
st.caption("Note: Based on only 13 quarters of data with a ~4-row test split. Accuracy figures are indicative and not statistically robust due to the small sample size.")

st.markdown("---")
st.caption("Data source: Screener.in | Company: Voltas Ltd")
