'''
Improving Tracebility

Your shop adds a 10% VAT on every order.
You want this to be consistent and traceable.
Task:
-Write add_vat(price, vat_rate)
-Use it to compute final prices for 3 orders
'''

def add_vat(price, vat_rate):
    return price * (100+ vat_rate)/100

orders = [100, 15, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Orignial: {price}, final with VAT: {final_amount}")