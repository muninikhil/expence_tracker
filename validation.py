import math
import re
from datetime import datetime


def get_amount(prompt="Amount:"):
    while True:
        text=input(prompt).strip()
        try:
            value=float(text)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        if not math.isfinite(value) or value <=0:
            print("Amount must be a positive number.")
            continue
        return round(value, 2)

def get_date(prompt="enter the date (YYYY-MM-DD):", allow_blank=False):
    while True:
        text=input(prompt).strip()
        if text=="":
            if allow_blank:
                return None
            return datetime.today().strftime("%Y-%m-%d")
        
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        try:
            datetime.strptime(text, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            continue

        return text


def get_int(prompt):
    while True:
       text=input(prompt).strip()
       try:
              value=int(text)
              return value
       except ValueError:
              print("Invalid input. Please enter a valid integer.")
            
           