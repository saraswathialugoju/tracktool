import csv
import os
from datetime import datetime

# Define the CSV file to store expenses
CSV_FILE = "expenses.csv"

# Function to create the CSV file if it doesn't exist
def create_csv_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount"])

# Function to add an expense
def add_expense(date, description, amount):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])

# Function to generate a monthly report
def generate_monthly_report(year, month):
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        expenses = [row for row in reader if row["Date"].startswith(f"{year}-{month:02}")]

    total_expenses = sum(float(expense["Amount"]) for expense in expenses)

    print(f"Monthly Report for {year}-{month:02}")
    print("Date       | Description         | Amount")
    print("-" * 40)

    for expense in expenses:
        print(f"{expense['Date']} | {expense['Description']:<20} | ${expense['Amount']}")

    print("-" * 40)
    print(f"Total expenses: ${total_expenses:.2f}")

# Main menu
def main():
    create_csv_file()
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. Generate Monthly Report")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter a description: ")
            amount = input("Enter the amount: $")
            add_expense(date, description, amount)
            print("Expense added successfully!")

        elif choice == "2":
            year = int(input("Enter the year (YYYY): "))
            month = int(input("Enter the month (MM): "))
            generate_monthly_report(year, month)

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
