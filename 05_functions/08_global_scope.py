chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
    kitchen()

front_desk()
print("Final global chai: ", chai_type)

# global is the referance of to global object from anywhere and if you just want to excess  just above the function then nonlocal is your friend