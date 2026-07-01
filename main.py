from pdf_report import generate_pdf
from database import create_tables
from charts import (
    pie_chart,
    bar_chart,
    monthly_trend,
    top_expenses
)
from dashboard import dashboard, set_budget
from reports import (
    expense_summary,
    category_report,
    highest_expense,
    lowest_expense,
    search_category,
    search_date,
    export_report
)
from login import login, register
from expense import (
    add_expense,
    view_expenses,
    delete_expense,
    update_expense
)
create_tables()
def reports_menu():

    while True:

        print("\n========== REPORTS ==========")
        print("1. Expense Summary")
        print("2. Category Report")
        print("3. Highest Expense")
        print("4. Lowest Expense")
        print("5. Search by Category")
        print("6. Search by Date")
        print("7. Export Report")
        print("8. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            expense_summary()

        elif choice == "2":
            category_report()

        elif choice == "3":
            highest_expense()

        elif choice == "4":
            lowest_expense()

        elif choice == "5":
            search_category()

        elif choice == "6":
            search_date()

        elif choice == "7":
            export_report()

        elif choice == "8":
            break

        else:
            print("Invalid Choice")
            
def charts_menu():

    while True:

        print("\n========== CHARTS ==========")
        print("1. Pie Chart")
        print("2. Bar Chart")
        print("3. Monthly Trend")
        print("4. Top 5 Expenses")
        print("5. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            pie_chart()

        elif choice == "2":
            bar_chart()

        elif choice == "3":
            monthly_trend()

        elif choice == "4":
            top_expenses()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")
            
def expense_menu():

    while True:

        print("\n======================================")
        print("      SMART EXPENSE TRACKER PRO")
        print("======================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Reports")
        print("6. Dashboard")
        print("7. Charts")
        print("8. Set Monthly Budget")
        print("9.  Generate PDF Report")
        print("10. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_expense()

        elif choice == "4":
            delete_expense()
            
        elif choice == "5":
            reports_menu()
            
        elif choice == "6":
            dashboard()
            
        elif choice == "7":
            charts_menu()    
            
        elif choice == "8":
            set_budget()  
            
        elif choice == "9":
            generate_pdf()                    
            
        elif choice == "10":
            print("Logged Out Successfully.\n")
            break

        else:
            print("Invalid Choice")


while True:

    print("\n===================================")
    print(" SMART EXPENSE TRACKER PRO ")
    print("===================================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        register()

    elif choice == "2":

        if login():
            expense_menu()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")