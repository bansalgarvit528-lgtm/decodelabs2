import pandas as pd
import os

FILE_NAME = "expenses.csv"


# ----------------------------------------
# Load Expense Data
# ----------------------------------------
def load_data():

    if not os.path.exists(FILE_NAME):
        print("Expense file not found.")
        return None

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("\nNo Expense Records Found.\n")
            return None

        return df

    except Exception:
        print("Unable to read expense file.")
        return None


# ----------------------------------------
# Overall Expense Summary
# ----------------------------------------
def expense_summary():

    df = load_data()

    if df is None:
        return

    print("\n================ EXPENSE SUMMARY ================\n")

    total = df["Amount"].sum()
    average = df["Amount"].mean()
    maximum = df["Amount"].max()
    minimum = df["Amount"].min()

    print(f"Total Transactions : {len(df)}")
    print(f"Total Expense      : ₹{total:.2f}")
    print(f"Average Expense    : ₹{average:.2f}")
    print(f"Highest Expense    : ₹{maximum:.2f}")
    print(f"Lowest Expense     : ₹{minimum:.2f}")

    print("\n===============================================\n")


# ----------------------------------------
# Category Wise Report
# ----------------------------------------
def category_report():

    df = load_data()

    if df is None:
        return

    print("\n=========== CATEGORY REPORT ===========\n")

    report = df.groupby("Category")["Amount"].sum()

    for category, amount in report.items():

        print(f"{category:<20} ₹{amount:.2f}")

    print("\n=======================================\n")


# ----------------------------------------
# Highest Expense
# ----------------------------------------
def highest_expense():

    df = load_data()

    if df is None:
        return

    row = df.loc[df["Amount"].idxmax()]

    print("\n========== HIGHEST EXPENSE ==========\n")

    print(f"ID          : {row['ID']}")
    print(f"Date        : {row['Date']}")
    print(f"Category    : {row['Category']}")
    print(f"Description : {row['Description']}")
    print(f"Amount      : ₹{row['Amount']}")

    print("\n=====================================\n")


# ----------------------------------------
# Lowest Expense
# ----------------------------------------
def lowest_expense():

    df = load_data()

    if df is None:
        return

    row = df.loc[df["Amount"].idxmin()]

    print("\n========== LOWEST EXPENSE ==========\n")

    print(f"ID          : {row['ID']}")
    print(f"Date        : {row['Date']}")
    print(f"Category    : {row['Category']}")
    print(f"Description : {row['Description']}")
    print(f"Amount      : ₹{row['Amount']}")

    print("\n====================================\n")


# ----------------------------------------
# Search by Category
# ----------------------------------------
def search_category():

    df = load_data()

    if df is None:
        return

    category = input("Enter Category : ").strip()

    result = df[df["Category"].str.lower() == category.lower()]

    if result.empty:
        print("\nNo Expense Found.\n")
        return

    print(result.to_string(index=False))


# ----------------------------------------
# Search by Date
# ----------------------------------------
def search_date():

    df = load_data()

    if df is None:
        return

    date = input("Enter Date (DD-MM-YYYY) : ")

    result = df[df["Date"] == date]

    if result.empty:
        print("\nNo Record Found.\n")
        return

    print(result.to_string(index=False))


# ----------------------------------------
# Export Report
# ----------------------------------------
def export_report():

    df = load_data()

    if df is None:
        return

    report = df.groupby("Category")["Amount"].sum().reset_index()

    report.columns = ["Category", "Total Expense"]

    report.to_csv("monthly_report.csv", index=False)

    print("\nReport Exported Successfully.")
    print("File Name : monthly_report.csv\n")