'''
You're preparing an order summary with customer names and their total bill.
Task:
-Use two lists: one for names and one for bills.
-Print: "[Name] paid Rs[amount]"
'''
# zip = zip(*iterables, strict=False) Iterate over several iterables in parallel, producing tuples with an item for each one
names = ["Luffy", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")

