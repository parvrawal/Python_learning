class Chaicup:
    size = 150 #ml

    def describe(self):
        #  self is  the referance of all the property defining in here, after passing self you can refer anything which within class
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))