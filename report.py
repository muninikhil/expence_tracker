from datetime import datetime
def get_month_input():
    
    while True:
        text = input("Month (YYYY-MM), Enter for current month: ").strip()
        if text == "":
            return datetime.today().strftime("%Y-%m")
        try:
            datetime.strptime(text, "%Y-%m")
            return text
        except ValueError:
            print("Use the format YYYY-MM, for example 2026-11.")
def category_totals(expenses, month):
    
    totals = {}
    for e in expenses:
        if e["date"].startswith(month):
            totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals
def show_monthly_summary(expenses):
    month = get_month_input()
    totals = category_totals(expenses, month)
    if not totals:
        print(f"No expenses found for {month}.")
        return
    grand_total = sum(totals.values())
    print(f"\nSummary for {month}")
    print("-" * 40)
    for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        percent = amount / grand_total * 100
        print(f"{category:<15}{amount:>10.2f}  ({percent:.1f}%)")
    print("-" * 40)
    print(f"{'Total':<15}{grand_total:>10.2f}")
    top = max(totals, key=totals.get)
    print(f"Highest spending category: {top}")