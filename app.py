import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

st.title("Customer Churn Dashboard")

# Filter
contract = st.selectbox(
    "Choose Contract",
    ["All", "Month-to-month", "One year", "Two year"]
)

if contract != "All":
    df = df[df["Contract"] == contract]

# Numbers
total = len(df)
churned = len(df[df["Churn"] == "Yes"])
rate = churned / total * 100

st.write("Total Customers:", total)
st.write("Churned Customers:", churned)
st.write("Churn Rate:", round(rate, 2), "%")

# Churn chart
chart = df["Churn"].value_counts().reset_index()
chart.columns = ["Churn", "Customers"]

fig = px.bar(chart, x="Churn", y="Customers", text="Customers")
st.plotly_chart(fig)

# Contract chart
chart2 = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).reset_index(name="Churn Rate")

fig2 = px.bar(
    chart2,
    x="Contract",
    y="Churn Rate",
    text=chart2["Churn Rate"].round(2).astype(str) + "%"
)

st.plotly_chart(fig2)
