'''
Each objects has its own entity it posses its own features, its own properties and does not bother other ones this is exactly the namespaces and the concept of the  namespaces in the world of the python object oriented programming
'''


class Chai:
    origin = "India"
    #when the variables goes under classes its called properties

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)


# creating objects from class chai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False
print("Class" ,Chai.is_hot)
print("Masala", masala.is_hot)
# every objects having their own namespace which does not affect others object also as classes default

masala.flavor = "Masala"
print(masala.flavor)