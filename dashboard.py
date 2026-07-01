import pandas as pd
import os

FILE_NAME = "expenses.csv"
BUDGET_FILE = "budget.txt"


# -------------------------------
# Load Expense Data
# -------------------------------
def load_data():

    if not os.path.exists(FILE_NAME):
        return None

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            return None

        return df

    except:
        return None


# -------------------------------
# Set Monthly Budget
# -------------------------------
def set_budget():

    while True:

        try:
            budget = float(input("\nEnter Monthly Budget (₹): "))

            with open(BUDGET_FILE, "w") as file:
                file.write(str(budget))

            print("\nBudget Saved Successfully.\n")
            break

        except:
            print("Invalid Budget Amount")


# -------------------------------
# Get Budget
# -------------------------------
def get_budget():

    if not os.path.exists(BUDGET_FILE):
        return 0

    try:

        with open(BUDGET_FILE, "r") as file:
            return float(file.read())

    except:
        return 0


# -------------------------------
# Progress Bar
# -------------------------------
def progress_bar(percent):

    total = 30

    filled = int(total * percent / 100)

    return "█" * filled + "-" * (total - filled)


# -------------------------------
# Dashboard
# -------------------------------
def dashboard():

    df = load_data()

    if df is None:

        print("\nNo Expense Data Available.\n")
        return

    budget = get_budget()

    total = df["Amount"].sum()

    highest = df["Amount"].max()

    average = df["Amount"].mean()

    transactions = len(df)

    category = df.groupby("Category")["Amount"].sum().idxmax()

    remaining = budget - total

    percent = 0

    if budget > 0:
        percent = (total / budget) * 100

    print("\n")
    print("=" * 60)
    print("             SMART EXPENSE TRACKER DASHBOARD")
    print("=" * 60)

    print(f"\nMonthly Budget      : ₹{budget:.2f}")
    print(f"Total Expense       : ₹{total:.2f}")
    print(f"Remaining Budget    : ₹{remaining:.2f}")
    print(f"Highest Expense     : ₹{highest:.2f}")
    print(f"Average Expense     : ₹{average:.2f}")
    print(f"Transactions        : {transactions}")
    print(f"Top Category        : {category}")

    if budget > 0:

        print("\nBudget Utilization")

        print(progress_bar(percent))

        print(f"{percent:.2f}% Used")

    if budget > 0:

        if percent >= 100:
            print("\n🔴 ALERT : Budget Exceeded!")

        elif percent >= 80:
            print("\n🟠 WARNING : Approaching Budget Limit")

        else:
            print("\n🟢 Excellent Budget Control")

    print("=" * 60)