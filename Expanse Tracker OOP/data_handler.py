import json

FILE_PATH="data.json"

def load_expenses():
    try: 
        with open(FILE_PATH, "r") as file:
            expenses = json.load(file)
            return expenses
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
def save_expenses(expenses):
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)

