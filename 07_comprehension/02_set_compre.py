favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
# print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardmom", "Clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "Clove"],
}

unique_spcies = {spice for ingredients in recipes.values() for spice in ingredients} # in the first place the only name writens which we wants to value from in here the ingredients is middle way and spice is ultimated value to find out

print(unique_spcies)
