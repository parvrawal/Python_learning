'''
Splitting Complex Tasks

You're creating a monthly report for a cafe's sales.
Instead of putting all logic in one place, break it down.

Task:
-Write a function generate_report() that calls:
-Fetch_sales()
-filter_valid_orders()
-summarize_date()
'''

def fetch_sales():
    print("Fetching the sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")

generate_report()