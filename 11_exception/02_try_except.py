chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("the key that you are trying to acess does not exists")


print("Hello chai code")
