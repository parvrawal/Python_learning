class ChaiOrder:
    def __init__(self, type_, size):
        # Constructor
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {(self.type).upper()} chai"
    
order = ChaiOrder("Masala", 200) # Instance of the class
print(order.summary())

order_two = ChaiOrder("ginger", 220)
print(order_two.summary())