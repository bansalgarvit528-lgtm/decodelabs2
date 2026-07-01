import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "expenses.csv"


def load_data():
    if not os.path.exists(FILE_NAME):
        print("Expense file not found.")
        return None

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No Expense Records Found.")
            return None

        return df

    except Exception as e:
        print("Error:", e)
        return None


# -------------------------------
# Pie Chart
# -------------------------------
def pie_chart():

    df = load_data()

    if df is None:
        return

    category = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(
        category,
        labels=category.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution by Category")
    plt.axis("equal")
    plt.show()


# -------------------------------
# Bar Chart
# -------------------------------
def bar_chart():

    df = load_data()

    if df is None:
        return

    category = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.bar(category.index, category.values)

    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=20)

    plt.tight_layout()
    plt.show()


# -------------------------------
# Monthly Trend
# -------------------------------
def monthly_trend():

    df = load_data()

    if df is None:
        return

    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    monthly = df.groupby(
        df["Date"].dt.strftime("%b-%Y")
    )["Amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(
        monthly.index,
        monthly.values,
        marker="o"
    )

    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# -------------------------------
# Top 5 Expenses
# -------------------------------
def top_expenses():

    df = load_data()

    if df is None:
        return

    top = df.sort_values(
        by="Amount",
        ascending=False
    ).head(5)

    plt.figure(figsize=(10, 5))

    plt.bar(
        top["Description"],
        top["Amount"]
    )

    plt.title("Top 5 Highest Expenses")
    plt.xlabel("Description")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=20)

    plt.tight_layout()
    plt.show()