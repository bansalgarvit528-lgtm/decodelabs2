Task 2

# 💰 Smart Expense Tracker Pro

A professional **Python-based Expense Management System** developed for internship, portfolio, and interview purposes. This project helps users efficiently manage their daily expenses, monitor budgets, analyze spending habits, and generate reports with interactive visualizations.

---

# 📌 Project Overview

Smart Expense Tracker Pro is a modular console-based application built using Python. It allows users to securely manage their personal expenses by providing features such as expense tracking, budgeting, reporting, dashboard analytics, data visualization, PDF report generation, backup, and logging.

The project demonstrates practical implementation of Python programming concepts including modular programming, file handling, data analysis, visualization, and report generation.

---

# 🎯 Project Objectives

- Digitally record daily expenses.
- Categorize expenses for better financial management.
- Monitor monthly spending.
- Generate professional reports.
- Visualize financial data using charts.
- Practice real-world Python development.
- Build a portfolio-quality project for internships and interviews.

---

# ✨ Features

## 🔐 User Authentication

- User Registration
- User Login
- Credential Validation
- JSON-based User Storage

---

## 💳 Expense Management

- Add Expense
- View Expenses
- Update Expense
- Delete Expense
- Auto Generate Expense ID
- Date-wise Expense Entry
- Category-wise Expense Entry

---

## 📂 Expense Categories

- 🍔 Food
- 🚌 Travel
- 🛍 Shopping
- 💡 Bills
- 🎬 Entertainment
- 📚 Education
- 🏥 Healthcare
- 📦 Other

---

## 📊 Reports & Analytics

- Expense Summary
- Category-wise Report
- Highest Expense
- Lowest Expense
- Average Expense
- Search by Category
- Search by Date
- Export Report

---

## 📈 Dashboard

The dashboard provides real-time financial insights including:

- Monthly Budget
- Total Expenses
- Remaining Budget
- Highest Expense
- Average Expense
- Total Transactions
- Top Spending Category
- Budget Utilization

---

## 📉 Data Visualization

Interactive charts using Matplotlib:

- Pie Chart
- Bar Chart
- Monthly Expense Trend
- Top 5 Highest Expenses

---

## 📄 PDF Report Generation

Generate a professional PDF report containing:

- Expense Records
- Expense Summary
- Categories
- Amount Details

---

## 💾 Backup System

- Automatic Backup
- Prevents Data Loss
- Easy Recovery

---

## 📝 Logging System

Maintains activity logs such as:

- User Login
- Expense Added
- Expense Updated
- Expense Deleted
- Report Generated
- PDF Generated

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Analysis |
| Matplotlib | Data Visualization |
| CSV | Expense Storage |
| JSON | User Authentication |
| ReportLab | PDF Generation |
| VS Code | Development Environment |

---

# 📁 Project Structure

```text
SmartExpenseTracker/

│
├── main.py
├── login.py
├── expense.py
├── reports.py
├── dashboard.py
├── charts.py
├── pdf_report.py
├── backup.py
├── logger.py
│
├── users.json
├── expenses.csv
├── budget.txt
├── Expense_Report.pdf
│
├── requirements.txt
├── README.md
│
└── screenshots/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/SmartExpenseTracker.git
```

## Open Project

```bash
cd SmartExpenseTracker
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 📂 Expense Data Format

```csv
ID,Date,Category,Description,Amount
1,01-07-2026,Food,Burger,200
2,01-07-2026,Travel,Metro,80
3,01-07-2026,Shopping,Shoes,2500
```

---

# 📊 Workflow

```text
Start
   │
   ▼
User Login/Register
   │
   ▼
Expense Management
   │
   ▼
CSV Storage
   │
   ▼
Reports
   │
   ▼
Dashboard
   │
   ▼
Charts
   │
   ▼
PDF Report
   │
   ▼
Exit
```

---

# 🧩 Module Description

## main.py

Acts as the central controller of the application.

Responsibilities:

- Display Main Menu
- Handle Navigation
- Connect All Modules
- Logout

---

## login.py

Handles user authentication.

Functions:

- Register User
- Login User
- Validate Credentials
- Store User Information

---

## expense.py

Core module of the project.

Features:

- Add Expense
- View Expense
- Update Expense
- Delete Expense
- Expense ID Generation

---

## reports.py

Performs expense analysis using Pandas.

Features:

- Expense Summary
- Category Report
- Highest Expense
- Lowest Expense
- Average Expense
- Search by Category
- Search by Date
- Export Report

---

## dashboard.py

Displays financial overview.

Includes:

- Budget Tracking
- Remaining Budget
- Average Expense
- Top Category
- Total Transactions

---

## charts.py

Generates graphical analysis.

Charts Available:

- Pie Chart
- Bar Chart
- Monthly Trend
- Top Expenses

---

## pdf_report.py

Creates PDF reports from expense records.

---

## backup.py

Creates backups of expense data for recovery.

---

## logger.py

Maintains project activity logs.

---

# 🧠 Python Concepts Used

## Core Python

- Variables
- Operators
- Loops
- Conditional Statements
- Functions
- Modules

## Data Structures

- Lists
- Dictionaries
- Tuples

## File Handling

- CSV
- JSON

## Exception Handling

- try
- except

## Libraries

- Pandas
- Matplotlib
- ReportLab

---

# 📷 Suggested Screenshots

Add screenshots inside the **screenshots/** folder.

Example:

```
screenshots/
│
├── login.png
├── dashboard.png
├── expense_history.png
├── pie_chart.png
├── bar_chart.png
├── monthly_trend.png
├── pdf_report.png
```

---

# 🚀 Future Enhancements

- SQLite Database
- Flask Web Application
- Django Version
- Mobile Application
- AI Expense Prediction
- OCR Receipt Scanner
- Cloud Backup
- Email Reports
- Multi-user Support

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- Python Programming
- Modular Programming
- File Handling
- Data Analysis
- Data Visualization
- Report Generation
- CRUD Operations
- Budget Management
- Software Project Structure

---

# 💼 Resume Description

**Smart Expense Tracker Pro** is a modular Python-based expense management system developed to simplify personal financial tracking. The application includes secure user authentication, expense CRUD operations, budget management, dashboard analytics, PDF report generation, and interactive data visualization using Pandas and Matplotlib. The project follows modular software architecture and demonstrates practical implementation of real-world Python programming concepts.

---

# 📌 GitHub Topics

```
python
expense-tracker
python-project
finance
budget-management
pandas
matplotlib
csv
json
reportlab
dashboard
analytics
portfolio-project
internship-project
```

---

# 👨‍💻 Author

**Garvit Bansal**

Python Developer | AI & ML Enthusiast | Open Source Learner

---

# ⭐ If you found this project useful, consider giving it a star!
