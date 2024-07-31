"""
Author: Cameron
Description : Expense tracker
Date: 26/07/2024

"""
import modules_for_tracker
import json
from datetime import datetime
import os
import sys
location = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(location)
  
def main():
    print("Expense Tracker\n==============\n")
    read_expenses_from_json()
    enter_expenses()
    modules_for_tracker.sum(expenses)
    

    

expenses = {}
expense_item_number = 0

def enter_expenses():
    while True:
        global expense_item_number  

        # expense, date(use format), category, amount, description
       
        name = input("Enter the name of the expense (or 0 to exit):")
        if name == '0':
            break
        
        date = modules_for_tracker.date_function()
        category = modules_for_tracker.category_function()
        amount = modules_for_tracker.amount_function()
        description = input("Enter a description of the expense: ")

        expenses.update({str(expense_item_number): {
            "name": name,
            "date": date,
            "category": category,
            "amount": amount,
            "description": description}
        })

        expense_item_number+=1
        write_expense_to_json()

        
def read_expenses_from_json():
    try:
        global expenses
        global expense_item_number
        with open("expense_tracker.json", "r") as file:
            expenses = json.load(file)
        last_expense_number = list(expenses)[-1]
        expense_item_number = int(last_expense_number)+1
    except FileNotFoundError:
        print("New expense tracker created.\n")

def write_expense_to_json():
    with open("expense_tracker.json", "w") as file:
        json.dump(expenses, file, indent=4)


if __name__ == "__main__":
    main()

# I AM MAKING A CHANGE TO SEE IF I CAN UPLOAD THIS AND HOW GIT WORKS
