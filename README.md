# finance_health_checker

# 💸 Financial Health Checker

A simple and interactive Streamlit app to analyze your personal expenses, visualize trends, and get a financial health score — all from a CSV file of your spending.

---

## 📂 Features

- 📤 Upload a CSV file of your expenses
- 📊 View monthly spending summaries
- 📂 Visualize category-wise breakdown (food, rent, shopping, etc.)
- 🧠 Calculate a Financial Health Score based on your savings
- 💡 Supports dynamic income entry
- 🔎 Clean and easy-to-use UI

---

## 📁 Sample CSV Format

```csv
Date,Amount,Category,Description
2025-06-01,1200,Food,Groceries from D-Mart
2025-06-02,800,Transport,Auto fare
2025-06-05,1500,Entertainment,Movie + Snacks
2025-06-06,6000,Rent,Flat rent

How to Run
Clone the repo or download finance_tracker.py

Install dependencies:

bash
Copy
Edit
pip install streamlit pandas matplotlib
Run the app:

bash
Copy
Edit
streamlit run finance_tracker.py
Upload your expense CSV via the web interface.

🎯 Financial Health Score Logic
💚 Healthy: Savings > 30% of income

💛 Okay: Savings between 10%–30%

❤️ Critical: Savings < 10%


