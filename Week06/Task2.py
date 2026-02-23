
#TASK 2

import csv
from datetime import datetime

def log_to_csv(filename, command, target, result, status):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, command, target, result, status])


def read_csv_log(filename):

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))