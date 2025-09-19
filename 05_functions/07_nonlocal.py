chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    # non local means from inside to inside function you just targeting inside the function
    print("After kitchen update ", chai_type)

update_order()