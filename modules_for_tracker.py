
import json
import sys
import os
os.system("cls")
from datetime import datetime


def amount_function():
    while True:
        try:
            amount = input("Enter the amount: ")
            if (amount.isalpha()) == False and "," not in amount :
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid format. Please type numbers and decimal point only.")
    return amount
        
def category_function():
    category_list = ["Store", "Online", "Bills", "Misc"]
    while True:
        try:
            category = input("Enter the category (Store, Online, Bills, Misc ): ").title()
            if category in category_list:
                break
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid category {category}. Please type from this list: Store, Online, Bills, Misc") 
    return category

def date_function():
    while True:
        try:
            date = (input("Enter the date of expense (DD-MM-YY): "))
            d = datetime.strptime(date, '%d-%m-%Y')
            date = d
            break
        except ValueError:
            print(f"Invalid date entered - {date}, please try again.")
    
    return(str(date).split()[0])

    

def write_expense_to_json():
    with open("expense_tracker.json", "w") as file:
        json.dump(expenses, file, indent=4)

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

def sum(data):
    with open("expense_tracker.json", "r") as file:
        data = json.load(file)
    def find_key_values(data, target_key):
        values = []
        def recursive_search(d):
            if isinstance(d, dict):
                for key, value in d.items():
                    if key == target_key:
                        values.append(value)
                    if isinstance(value, dict):
                        recursive_search(value)
                    elif isinstance(value, list):
                        for item in value:
                            if isinstance(item, dict):
                                recursive_search(item)
        recursive_search(data)
        return values
                
    key_to_find = 'amount'
    values = find_key_values(data,key_to_find)
    values = [float(x) for x in values]
    
    sum = 0
    for transaction in values:
        sum += transaction

    print(f"Current total: {sum}")


def opening_options():
    while True:
        print("Expense Tracker\n==============\n")
        create_or_open_file = input("Do you wish to create/open a file? Y/N ").upper()
        if create_or_open_file == "Y":
            break     
        elif create_or_open_file == "N":
            sys.exit("Exiting Program.")
        else:
            print("Invalid Input.")
            

    
'''
want to write a function that will go into parts of dict and return sum of things:

sum value of amount - and return it in currency almost done jusr nee d to return £ sign

how many items are store, online, bills, misc could use same func as sum but have if statement 
so if key to find equals bills do this and add bills to list
elif its misc add to list etc
then return how many was in each

to do: think about a menu with options. 
a clear function to cleqn up the comsole, 
try except into sum functiom. test it and try to break it 
give sum of values in certain month 

go into the date and ask how may expenses were in a day, a year or a month - number of expenses and value'''