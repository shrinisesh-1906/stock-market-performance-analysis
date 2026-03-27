import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Stock Market Performance Dashboard")

# Load datasets
stock_data = pd.read_csv("final_stock_data.csv")
yearly_returns = pd.read_csv("yearly_returns.csv")
monthly_returns = pd.read_csv("monthly_returns.csv")

# Sidebar filter
tickers = stock_data["Ticker"].unique()
selected_ticker = st.sidebar.selectbox("Select Stock", tickers)

filtered_data = stock_data[stock_data["Ticker"] == selected_ticker]

st.subheader(f"Stock Price Trend: {selected_ticker}")

fig = px.line(filtered_data, x="date", y="close", title="Stock Price Over Time")
st.plotly_chart(fig)

st.subheader("Top Performing Stocks (Yearly)")

top5 = yearly_returns.sort_values("yearly_return", ascending=False).head(5)
fig2 = px.bar(top5, x="Ticker", y="yearly_return", title="Top 5 Stocks")
st.plotly_chart(fig2)

st.subheader("Worst Performing Stocks")

bottom5 = yearly_returns.sort_values("yearly_return").head(5)
fig3 = px.bar(bottom5, x="Ticker", y="yearly_return", title="Bottom 5 Stocks")
st.plotly_chart(fig3)

st.subheader("Monthly Trend")

fig4 = px.line(monthly_returns, x="month", y="close", color="Ticker")
st.plotly_chart(fig4)