import shutil
from datetime import datetime

def backup():

    filename = "backup_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv"

    shutil.copy(
        "expenses.csv",
        filename
    )

    print("Backup Created.")