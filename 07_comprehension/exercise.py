'''
Smart Inventory Filter
You are building a Smart Inventory Filter for a retail store.

Tasks:

Process a list of product dictionaries, where each product has name, price, and category.

Use different types of comprehensions to:

Extract names of products priced below ₹500 using list comprehension.

Extract all unique categories using set comprehension.

Create a name-to-price mapping using dictionary comprehension.

Generate a list of discounted prices using a generator expression and convert it to a list.

Return all four outputs as a tuple.


'''

# This function will be tested automatically.
# Do not change the function name or parameters.


"""
    items: A list of dictionaries, each representing a product with keys:
        - "name": str
        - "price": int
        - "category": str
    
    Returns:
        - List of names of affordable products (pric e < 500)
        - Set of unique categories
        - Dictionary of product name to price mapping
        - Generator expression converted to list of prices after applying 10% discount
"""

def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    
    # Write your code below this line
    below_price = [item["name"] for item in items if item["price"] < 500]
    unique_categories = {categorie["category"] for categorie in items}
    product_details = {item["name"] : item["price"] for item in items}
    discount_price = list((int(item["price"] * 0.9) for item in items))
    return (below_price, unique_categories, product_details ,discount_price)
