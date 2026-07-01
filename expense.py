import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

HEADERS = ["ID", "Date", "Category", "Description", "Amount"]


# -----------------------------
# Create CSV File
# -----------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


# -----------------------------
# Generate Expense ID
# -----------------------------
def generate_id():
    initialize_file()

    with open(FILE_NAME, "r") as file:
        rows = list(csv.reader(file))

    if len(rows) == 1:
        return 1

    last_id = int(rows[-1][0])
    return last_id + 1


# -----------------------------
# Add Expense
# -----------------------------
def add_expense():

    initialize_file()

    print("\n========== Add Expense ==========\n")

    print("Categories")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Bills")
    print("5. Entertainment")
    print("6. Education")
    print("7. Healthcare")
    print("8. Other")

    categories = {
        "1": "Food",
        "2": "Travel",
        "3": "Shopping",
        "4": "Bills",
        "5": "Entertainment",
        "6": "Education",
        "7": "Healthcare",
        "8": "Other"
    }

    choice = input("\nSelect Category : ")

    if choice not in categories:
        print("Invalid Category")
        return

    description = input("Description : ")

    try:
        amount = float(input("Amount : ₹"))
    except:
        print("Invalid Amount")
        return

    expense_id = generate_id()

    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            expense_id,
            date,
            categories[choice],
            description,
            amount
        ])

    print("\nExpense Added Successfully.\n")


# -----------------------------
# View Expenses
# -----------------------------
def view_expenses():

    initialize_file()

    print("\n============== Expense History ==============\n")

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        total = 0

        count = 0

        for row in reader:

            count += 1

            total += float(row[4])

            print(
                f"""
ID          : {row[0]}
Date        : {row[1]}
Category    : {row[2]}
Description : {row[3]}
Amount      : ₹{row[4]}
---------------------------------------------
"""
            )

        if count == 0:
            print("No Expenses Found.\n")

        else:
            print(f"Total Records : {count}")
            print(f"Total Expense : ₹{total:.2f}\n")


# -----------------------------
# Delete Expense
# -----------------------------
def delete_expense():

    initialize_file()

    expense_id = input("Enter Expense ID : ")

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        for row in reader:

            if row[0] == expense_id:
                found = True
                continue

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(header)

        writer.writerows(rows)

    if found:
        print("Expense Deleted Successfully\n")
    else:
        print("Expense Not Found\n")


# -----------------------------
# Update Expense
# -----------------------------
def update_expense():

    initialize_file()

    expense_id = input("Enter Expense ID : ")

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        for row in reader:

            if row[0] == expense_id:

                found = True

                print("\nCurrent Details")

                print(row)

                row[3] = input("New Description : ")

                row[4] = input("New Amount : ")

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(header)

        writer.writerows(rows)

    if found:
        print("Expense Updated Successfully\n")
    else:
        print("Expense ID Not Found\n")