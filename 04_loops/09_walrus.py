# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 13

# if (remainder := value % 5):
#     print(f"Not divisibl, remainder is {remainder}")

# available_sizes = ["small", "medium", "large"]

# if(requested_sizw := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_sizw} chai")
# else:
#     print(f"Size is unavailable - {requested_sizw}")



flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ",flavors)

while (flavor := input("Chosse your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You chosse {flavor} chai")