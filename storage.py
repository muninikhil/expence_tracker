import json
import os

DATE_DIR="date"
DATA_FILE=os.path.join(DATE_DIR,"expenses.json")

def load_data():
    try:
        with open (DATA_FILE,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data. The file may be corrupted.")
        return []

def save_data(data):
    os.makedirs(DATE_DIR, exist_ok=True)
    with open(DATA_FILE,"w") as f:
        json.dump(data,f,indent=4)