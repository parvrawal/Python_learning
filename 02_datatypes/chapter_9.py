#set
essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

#union or pip
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

#interseaction or common
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

#frozenset