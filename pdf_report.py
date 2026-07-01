from reportlab.platypus import SimpleDocTemplate, Table
import pandas as pd

def generate_pdf():

    df = pd.read_csv("expenses.csv")

    pdf = SimpleDocTemplate("Expense_Report.pdf")

    data = [list(df.columns)] + df.values.tolist()

    table = Table(data)

    pdf.build([table])

    print("PDF Report Generated Successfully.")