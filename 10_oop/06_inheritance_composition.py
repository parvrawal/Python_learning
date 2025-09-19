class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

#  Composition
class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()



'''
from typing import Type


class BaseChai:
    def __init__(self, chai_type: str):
        self.chai_type = chai_type

    def prepare(self) -> None:
        print(f"Preparing {self.chai_type} chai...")


class MasalaChai(BaseChai):
    def __init__(self, chai_type: str = "Masala"):
        super().__init__(chai_type)

    def add_spices(self) -> None:
        print("Adding cardamom, ginger, cloves.")


# Composition
class ChaiShop:
    chai_cls: Type[BaseChai] = BaseChai

    def __init__(self):
        # VS Code now knows this is a BaseChai (or subclass)
        self.chai: BaseChai = self.chai_cls("Regular")

    def serve(self) -> None:
        print(f"Serving {self.chai.chai_type} chai in the shop")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls: Type[BaseChai] = MasalaChai

    def __init__(self):
        super().__init__()
        # Re-type chai so VS Code knows it’s a MasalaChai
        self.chai: MasalaChai = self.chai  # type: ignore[assignment]


# Usage
shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai.add_spices()  # ✅ No VS Code error now

'''
