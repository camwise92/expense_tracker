# File: modules_for_tracker.py
# Author: Cameron Carlisle
# Date Created: 26/07/2024
# Last Update: 18/03/2025
# Description: Main module for tracking expenses. Handles user input, stores expenses in a JSON file,
#              and provides functionality to calculate totals and filter expenses by category or date.

import json
import sys
import os
from datetime import datetime

# Clear the console for better readability
os.system("cls" if os.name == "nt" else "clear")

# Global variables to store expenses and track the last expense item number
expenses = {}
expense_item_number = 1

def amount_function():
    """
    Prompts the user to enter an amount and validates the input.
    Returns:
        float: The validated amount.
    """
    while True:
        try:
            amount = input("Enter the amount: ")
            if amount.replace(".", "").isdigit():  # Allow decimal points
                return float(amount)
            else:
                raise ValueError
        except ValueError:
            print("Invalid format. Please enter numbers and a decimal point only.")

def category_function():
    """
    Prompts the user to enter a category and validates the input.
    Returns:
        str: The validated category.
    """
    category_list = ["Store", "Online", "Bills", "Misc"]
    while True:
        try:
            category = input("Enter the category (Store, Online, Bills, Misc): ").title()
            if category in category_list:
                return category
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid category '{category}'. Please choose from: {', '.join(category_list)}")

def date_function():
    """
    Prompts the user to enter a date and validates the format.
    Returns:
        str: The validated date in 'YYYY-MM-DD' format.
    """
    while True:
        try:
            date = input("Enter the date of expense (DD-MM-YYYY): ")
            d = datetime.strptime(date, '%d-%m-%Y')
            return d.strftime('%Y-%m-%d')  # Convert to standard format
        except ValueError:
            print(f"Invalid date entered - '{date}'. Please use the format DD-MM-YYYY.")

def write_expense_to_json():
    """
    Writes the expenses dictionary to a JSON file.
    """
    with open("expense_tracker.json", "w") as file:
        json.dump(expenses, file, indent=4)

def read_expenses_from_json():
    """
    Reads expenses from a JSON file and initializes the global variables.
    If the file doesn't exist, it creates a new one.
    """
    global expenses, expense_item_number
    try:
        with open("expense_tracker.json", "r") as file:
            expenses = json.load(file)
        last_expense_number = list(expenses)[-1]
        expense_item_number = int(last_expense_number) + 1
    except FileNotFoundError:
        print("New expense tracker created.\n")
        expenses = {}

def calculate_total_expenses():
    """
    Calculates and prints the total amount of all expenses.
    """
    try:
        with open("expense_tracker.json", "r") as file:
            data = json.load(file)
        
        total = sum(float(expense['amount']) for expense in data.values())
        print(f"Current total: £{total:.2f}")
    except FileNotFoundError:
        print("No expenses found. Please add expenses first.")

def opening_options():
    """
    Displays the opening menu and prompts the user to create/open a file or exit.
    """
    while True:
        print("Expense Tracker\n==============\n")
        create_or_open_file = input("Do you wish to create/open a file? Y/N ").upper()
        if create_or_open_file == "Y":
            read_expenses_from_json()
            break
        elif create_or_open_file == "N":
            sys.exit("Exiting Program.")
        else:
            print("Invalid Input.")

# Main program logic
if __name__ == "__main__":
    opening_options()
    # Add more functionality here, such as adding expenses, viewing reports, etc.
