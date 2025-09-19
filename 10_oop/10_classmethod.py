class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size  = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size": "Large"})

order2 = ChaiOrder.from_string("Ginger-Low-Small")

order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
    


'''
🔹 1. @staticmethod

Belongs to the class, but does not get self or cls automatically.

It behaves like a normal function inside a class, used for utility/helper code.

Cannot access or modify class state or instance state.


2. @classmethod

Belongs to the class and gets cls (the class itself) as the first argument.

Can access and modify class variables (shared across all objects).

Often used as alternative constructors or when behavior depends on the class.

'''