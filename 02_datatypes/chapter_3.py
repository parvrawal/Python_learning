#  Interger 

black_tea_grams = 14
ginger_grams = 3


total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}")


milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
# // means i dont care about decimal number
print(f"While tea bags per pot: {bags_per_pot}")

base_flavor_strength = 2
scale_favctor = 3
power_flavour = base_flavor_strength **   scale_favctor
print(f"Scaled flavour strenght {power_flavour}")
# 2 * 2 * 2

total_tea_harvested = 1_000_000_000
print(f"Tea leaves: {total_tea_harvested}")
