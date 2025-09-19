class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

#code duplication
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level 


#Explicit call
# class GingerChai(Chai):
#     def __init(self, type_, strength, spice_level):
#         Chai.__init__(self, type, strength)
#         self.spice_level = spice_level


#super()
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level

