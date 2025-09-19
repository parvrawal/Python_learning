class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

#it will call the first class which you are inheriting
class D(C, B):
    pass

cup = D()
print(cup.label)
print(D.__mro__)  #dandar


#  Method Resolution Order.