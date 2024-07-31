"""
Author: Cameron
Description : Expense tracker extra functions
Date: 26/07/2024

# Sum function uses a recursiv search to fid a dictionary within a dictionary util it find the key it needs to find.
# Could reimplement it to use an input to then find something 
"""

import json
import os
import sys

location = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(location)

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
    print(values)
   


# Done so now wnat to take the list and convert the items into floats and return a sum of that list