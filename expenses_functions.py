"""
File: main.py
Author: Cameron Carlisle
Date Created: 26/07/2024
Last Update: 18/03/2025
Description: Main script for the expense tracker application. Handles user input for expenses,
             stores them in a JSON file, and provides functionality to view and manage expenses.
Usage: Run this script to start the expense tracker application.
"""

import json
import os
import sys
from modules_for_tracker import opening_options, date_function, category_function, amount_function, calculate_total_expenses

# Set the working directory to the script's location
location = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(location)

# Global variables to store expenses and track the last expense item number
expenses = {}
expense_item_number = 0

def main():
    """
    Main function to run the expense tracker application.
    """
    opening_options()
    read_expenses_from_json()
    enter_expenses()
    print("Exiting program.")

def enter_expenses():
    """
    Prompts the user to enter expenses and stores them in the global expenses dictionary.
    Exits when the user enters '0' for the expense name.
    """
    global expense_item_number

    while True:
        name = input("Enter the name of the expense (or 0 to exit): ").title()
        if name == '0':
            break

        date = date_function()
        category = category_function()
        amount = amount_function()
        description = input("Enter a description of the expense: ").capitalize()

        # Add the expense to the dictionary
        expenses[str(expense_item_number)] = {
            "name": name,
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        expense_item_number += 1
        write_expense_to_json()
        calculate_total_expenses()

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

def write_expense_to_json():
    """
    Writes the expenses dictionary to a JSON file.
    """
    with open("expense_tracker.json", "w") as file:
        json.dump(expenses, file, indent=4)

if __name__ == "__main__":
    main()
