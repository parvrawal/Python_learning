'''
Reducing Code Duplication

You're managing orders and want to print each customer's name along with the type of chai they ordered
Task:
- Write a function print_order(name, chai_type)
- Call it multiple times for different customers
'''

def print_order(name, chai_type): #parameter
    print(f"{name} ordered {chai_type} chai!")

print_order("Aman", "masala") # argument
print_order("Luffy", "ginger") # argument
print_order("Avana", "Tulsi") # argument

