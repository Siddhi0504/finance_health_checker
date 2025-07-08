import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Financial Health Checker")

uploaded_file = st.file_uploader("Upload your expenses in CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    st.subheader("Raw Data")
    st.dataframe(df)

      # Monthly expenses
    monthly_total = df.groupby('Month')['Amount'].sum()
    st.subheader("🗓️ Monthly Expenses")
    st.bar_chart(monthly_total)

    # Category spending
    category_total = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    st.subheader("📂 Spending by Category")
    st.bar_chart(category_total)

    # Financial health score
    income = st.number_input("Enter your monthly income (₹)", value=15000)
    total_spent = df['Amount'].sum()
    savings = income - total_spent
    savings_percent = (savings / income) * 100

    if savings_percent > 30:
        score = "Healthy 💚"
    elif savings_percent >= 10:
        score = "Okay 💛"
    else:
        score = "Critical ❤️"

    st.subheader("💡 Financial Health Summary")
    st.write(f"**Total Spent:** ₹{total_spent}")
    st.write(f"**Savings:** ₹{savings} ({savings_percent:.2f}%)")
    st.write(f"**Financial Health Score:** {score}")
